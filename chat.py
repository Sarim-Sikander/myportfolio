import streamlit as st

# Function to display the chat message
def display_chat_message(message):
    st.write(f"{message}")

# Function to handle the user's input
def handle_user_input(user_input):
    if user_input.lower() == "hi":
        display_chat_message("Hello! How can I help you today?")
    elif user_input.lower() == "who are you":
        display_chat_message("I am a chat assistant designed to assist users in contacting me for new jobs and to provide information about myself.")
    elif user_input.lower() == "how can i contact you":
        display_chat_message("You can contact me via email at example@example.com or by phone at +1 (123) 456-7890.")
    else:
        display_chat_message("I'm sorry, I don't understand your question. Can you please rephrase it?")

# Main function to run the app
def main():
    st.title("Chat Assistant")

    user_input = st.text_input("Type your message here:")

    if user_input:
        handle_user_input(user_input)