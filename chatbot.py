import datetime

def chatbot_response(msg):
    msg = msg.lower().strip()

    # BASIC GREETINGS
    if msg in ["hi", "hello", "hey"]:
        return "Hello! 👋 Nice to meet you."

    elif msg in ["good morning"]:
        return "Good morning ☀️ Have a great day!"

    elif msg in ["good afternoon"]:
        return "Good afternoon 😊"

    elif msg in ["good evening"]:
        return "Good evening 🌆"

    # PERSONAL QUESTIONS
    elif msg in ["your name", "what is your name", "name"]:
        return "I'm a Python chatbot 🤖"

    elif msg in ["who created you", "creator"]:
        return "I was created by Sameer Bist using Python 🐍"

    elif msg in ["who are you"]:
        return "I'm a simple rule-based chatbot for learning purposes."

    # DAILY CONVERSATION
    elif msg in ["how are you", "how are you?"]:
        return "I'm doing well 😊 Thanks for asking!"

    elif msg in ["what are you doing"]:
        return "I'm chatting with you and learning 😄"

    elif msg in ["where are you from"]:
        return "I live inside your computer 💻"

    # UTILITY
    elif msg in ["time", "current time"]:
        return "Current time: " + datetime.datetime.now().strftime("%H:%M:%S")

    elif msg in ["date", "today date"]:
        return "Today's date: " + datetime.datetime.now().strftime("%d-%m-%Y")

    # HELP & ABILITY
    elif msg in ["help", "what can you do"]:
        return (
            "I can:\n"
            "- Chat with you\n"
            "- Answer simple questions\n"
            "- Tell date and time\n"
            "- Motivate you\n"
            "- Exit when you say bye"
        )

    # STUDY & MOTIVATION
    elif msg in ["motivate me", "motivation"]:
        return "Keep learning 💪 Every expert was once a beginner."

    elif msg in ["study tips"]:
        return "Practice daily, build projects, and never stop learning 📚"

    elif msg in ["python"]:
        return "Python is a powerful and beginner-friendly programming language 🐍"

    # FUN
    elif msg in ["joke"]:
        return "Why do programmers love Python? Because it’s easy to understand 😄"

    elif msg in ["thank you", "thanks"]:
        return "You're welcome 😊 Happy to help!"

    # EXIT
    elif msg in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye 👋 Have a nice day!"

    # DEFAULT
    else:
        return "I didn't understand that 🤔 Try typing 'help'."

print("🤖 Smart Rule-Based Chatbot")
print("Type 'help' to see options | Type 'bye' to exit")

while True:
    user_input = input("\nYou: ")
    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower() in ["bye", "exit", "quit", "goodbye"]:
        break
