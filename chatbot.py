
import datetime

print("===================================")
print("       PYTHON VIRTUAL ASSISTANT")
print("===================================")

print("Hello! Welcome to my chatbot.")
print("Type 'bye' to exit.")

while True:
    message = input("\nYou: ").lower().strip()

    if message in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif message == "how are you":
        print("Bot: I am fine! Thank you.")

    elif message == "what is your name":
        print("Bot: My name is Python Assistant.")

    elif message == "what can you do":
        print("Bot: I can answer basic questions.")

    elif message == "who created you":
        print("Bot: I was created by Muskan using Python.")

    elif message == "what is python":
        print("Bot: Python is a popular programming language.")

    elif message == "date":
        print("Bot:", datetime.datetime.now().strftime("%d-%m-%Y"))

    elif message == "time":
        print("Bot:", datetime.datetime.now().strftime("%I:%M %p"))

    elif message == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't know the answer yet.")
        print("Bot: Please try asking something else.")
