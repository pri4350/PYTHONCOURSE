import datetime
import time
# Greeting based on time of day


name = input("Swagat hai, enter your name: ")

presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning,", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon,", name)
elif 17 <= presentHour <= 20:
    print("Good evening,", name)
else:
    print("Good night,", name)

print("Namaste! Welcome to Your ChatBot 🤖")
print("You can ask me basic questions. Type 'bye' to exit from the Chatbot")

# Chatbot Memory (all keys lowercase)
responses = {
    "hello": "Hi, Welcome. How can I help you?",
    "how are you": "I am very fine. Thank you 😊",
    "who are you": "I am a smart AI chatbot 🤖",
    "motivate me": "Keep going. Every bug makes you a better developer 💪",
    "happy": "Great to hear that 😄",
    "Sad": "Cheer up! Every problem has a solution 🌈",
    "function kya hote hai": "Programming mein function ek chhota robot hota hai jo kaam karta hai.",
    "thank you": "You are welcome! If you have more questions, feel free to ask.",
    "what is python": "Python ek high-level programming language hai jo code ko asaan aur readable banati hai.",
    "bye": "Bye! Have a nice day 🌸",
    "help": "Sure! You can ask me questions like 'What is Python?', 'Who are you?', or 'Motivate me'.",
    "tum kaun ho": "Main Python se bana chatbot hoon 😊"

}

# Function to get response
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()

    # 👉 Time condition FIRST
    if "time" in userQuestion or "samay" in userQuestion:
        return "Current time is " + datetime.datetime.now().strftime("%I:%M %p")

    # 👉 Normal responses
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I am still learning 😊"

# Chat loop
while True:
    userInput = input("Please ask your question: ")

    if "bye" in userInput.lower():
        print("Bot Response: Bye! Have a nice day 🌸")
        break

    reply = getResponseOfBot(userInput)
    print("Bot Response:", reply)
    time.sleep(1)  # Simulate thinking time
    print("You can ask me another question or type 'bye' to exit.")

