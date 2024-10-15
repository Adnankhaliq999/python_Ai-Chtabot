import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you":
    ["I'm doing well, thank you!", "I'm just a bot, but I'm fine!"],
    "what is your name":
    ["I am a chatbot created by [Adnan khaliq].", "My name is Chatbot."],
    "what can you do": [
        "I can chat with you and answer simple questions!",
        "I'm here to assist you with simple queries."
    ],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "what is the capital of france":
    ["The capital of France is Paris.", "It's Paris!"],
    "who is the president of usa": [
        "The current president of the USA is Joe Biden (as of 2024).",
        "It's Joe Biden."
    ],
    "what is 2 + 2": ["2 + 2 is 4.", "The answer is 4."],
    "what is the capital of japan":
    ["The capital of Japan is Tokyo.", "It's Tokyo!"],
    "what is python": [
        "Python is a popular programming language known for its simplicity and versatility.",
        "Python is a high-level programming language."
    ],
    "tell me a joke": [
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ],
}


def get_response(user_input):
    user_input = user_input.lower(
    )  # Convert user input to lowercase for better matching
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I don't understand that. Can you try asking something else?"


def chat():
    print(
        "Chatbot: Hello! I am your simple chatbot. Type 'goodbye' to end the chat."
    )
    while True:
        user_input = input("You: ")
        if user_input.lower() == "goodbye":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


# Run the chatbot
chat()
