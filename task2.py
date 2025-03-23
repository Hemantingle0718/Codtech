import spacy
import nltk
from nltk.chat.util import Chat, reflections
import random

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# NLTK Chatbot pairs (simple response rules)
pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you today?", "Hi! What can I do for you?"]),
    (r"how are you", ["I'm doing great, thank you for asking!", "I'm good, how about you?"]),
    (r"what is your name?", ["I am a chatbot created to assist you.", "You can call me your assistant."]),
    (r"tell me about (.*)", ["Tell me more about what you're looking for regarding %1.", "I would love to help you with %1."]),
    (r"(.*) (location|city|place)(.*)", ["I can help with information about places, can you be more specific?"]),
    (r"(.*)", ["Sorry, I didn't quite get that. Could you rephrase?", "Could you clarify your question?"]),
]

# Initialize the chatbot with reflection (for personal pronouns)
chatbot = Chat(pairs, reflections)

# Function to process user input using spaCy for NLP
def process_input(user_input):
    # Use spaCy for Named Entity Recognition (NER)
    doc = nlp(user_input)
    entities = [ent.text for ent in doc.ents]
    
    if entities:
        response = f"I see you mentioned: {', '.join(entities)}. Can you tell me more?"
    else:
        response = "I'm still learning to recognize specific details. Could you clarify?"
    
    return response

# Function to handle chatbot interaction
def chat():
    print("Chatbot: Hello! I am your assistant. Type 'exit' to quit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # First, check for a response from NLTK chatbot
        response = chatbot.respond(user_input)
        
        if response:
            print("Chatbot:", response)
        else:
            # If no match from the NLTK chatbot, use spaCy to analyze the input
            print("Chatbot:", process_input(user_input))

# Run the chatbot
if __name__ == "__main__":
    chat()