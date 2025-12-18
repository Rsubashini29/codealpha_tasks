def chatbot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi!"
    elif "how are you" in message:
        return "I'm fine, thanks!"
    elif "bye" in message:
        return "Goodbye!"
    else:
        return "I don't understand that. Try 'hello', 'how are you', or 'bye'."

print("Welcome to the Chatbot! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot: " + response)
    if "bye" in user_input.lower():
        break