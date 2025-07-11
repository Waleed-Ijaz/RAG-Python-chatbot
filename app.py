# chatbot_app.py

import json
import os
import requests
import streamlit as st
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

customer_id = os.getenv("VECTARA_CUSTOMER_ID")
api_key = os.getenv("VECTARA_API_KEY")
corpus_id = os.getenv("VECTARA_CORPUS_ID")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")


# Initialize Anthropic client
claude_client = Anthropic(api_key=anthropic_api_key)

# Function to generate query JSON for Vectara
def get_query_json(customer_id, corpus_id, query_value):
    query = {
        "query": [
            {
                "query": query_value,
                "num_results": 10,
                "corpus_key": [{"customer_id": customer_id, "corpus_id": corpus_id}],
            }
        ]
    }
    return json.dumps(query)

# Function to query Vectara
def query_vectara(customer_id, corpus_id, api_key, query):
    post_headers = {
        "customer-id": str(customer_id),
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.vectara.io/v1/query",
        data=get_query_json(customer_id, corpus_id, query),
        headers=post_headers
    )

    if response.status_code != 200:
        st.error(f"Query failed with code {response.status_code}, reason {response.reason}")
        return None
    return response.json()

# Function to generate a response using Claude
def generate_answer(chat_input):
    message = claude_client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": chat_input}]
    )
    return message.content

# Class to manage conversation memory
class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_interaction(self, user_input, bot_response):
        self.history.append({'user_input': user_input, 'bot_response': bot_response})

    def get_history(self):
        return " ".join([f"User: {entry['user_input']} | Bot: {entry['bot_response']}" for entry in self.history])

# Function to process chatbot interaction
def chatbot(input_text, memory):
    # Query Vectara first
    vectara_result = query_vectara(customer_id, corpus_id, api_key, input_text)

    if not vectara_result:
        return "No result returned from Vectara."

    # Extract relevant responses from Vectara
    extracted_texts = []
    for i, response_item in enumerate(vectara_result["responseSet"][0]["response"]):
        text = response_item["text"]
        document_index = response_item["documentIndex"]
        document_source = vectara_result["responseSet"][0]["document"][document_index]["id"]
        extracted_texts.append(f"{text} (Source: {document_source})")

    # Combine extracted texts with sources
    combined_text = "\n\n".join(extracted_texts)

    # Use conversation memory for context
    context = memory.get_history()

    # Generate input for Claude with memory and Vectara results
    chat_input = f"Context: {context}\n\nUser Query: {input_text}\n\nVectara Retrieved Response: {combined_text}\n\nAnswer the User Query and also give Sources at the end of the complete answer."
    claude_response = generate_answer(chat_input)

    # Add interaction to memory
    memory.add_interaction(input_text, claude_response)

    return claude_response

# Initialize conversation memory
memory = ConversationMemory()

# Streamlit app setup
st.title("RAG Chatbot")

# Input field for user query
user_input = st.text_input("You:", key="user_input")

# Chatbot response when input is provided
if user_input:
    bot_response = chatbot(user_input, memory)
    st.write(f"Bot: {bot_response}")


