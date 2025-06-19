# Simple rule-based chatbot

def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye!")
            break
        else:
            print("🤖 Chatbot: I'm not sure how to respond to that.")

# Run the chatbot
chatbot()
