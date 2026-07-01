import datetime
import random
import re

def clean_input(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation/symbols
    text = re.sub(r"[^\w\s]", "", text)

    # Remove extra spaces
    text = " ".join(text.split())

    return text

print("🤖 AI Chatbot Started! Type 'bye' to exit.\n")

while True:
    user_input = clean_input(input("You: "))

    # Greetings (hi, hiiii, heyyyy, helloooo)
    if (
        re.fullmatch(r"hi+", user_input)
        or re.fullmatch(r"hey+", user_input)
        or re.fullmatch(r"hello+", user_input)
    ):
        print("Bot: Hello! How can I help you today?")

    elif user_input in ["good morning", "gm"]:
        print("Bot: Good morning! Hope you have a great day.")

    elif user_input == "good afternoon":
        print("Bot: Good afternoon!")

    elif user_input in ["good night", "gn"]:
        print("Bot: Good night! Sleep well 😊")

    elif user_input == "how are you":
        print("Bot: I am fine! Thanks for asking.")

    elif user_input == "your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input == "help":
        print("Bot: I can greet you and answer basic questions.")

    elif user_input == "who made you":
        print("Bot: I was created by Vaidika Sharma.")

    elif user_input == "what can you do":
        print("Bot: I can chat, answer simple questions, and make your day better!")

    elif user_input == "are you human":
        print("Bot: No, I am a chatbot 🤖")

    elif user_input == "thank you":
        print("Bot: You're welcome!")

    elif user_input == "sorry":
        print("Bot: No worries!")

    elif user_input == "how is your day":
        print("Bot: My day is great! I love chatting.")

    elif user_input == "tell me a joke":
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs 😆",
            "Why did Python go to school? To improve its class 😂",
            "Debugging is like being the detective and the criminal at the same time 😅"
        ]
        print("Bot:", random.choice(jokes))

    elif user_input == "sing":
        print("Bot: La la la 🎵... Oops, I am not a singer.")

    elif user_input == "dance":
        print("Bot: *robot dance activated* 🤖💃")

    elif user_input == "motivate me":
        print("Bot: Keep learning! Every expert was once a beginner.")

    elif user_input == "exam stress":
        print("Bot: Stay calm, revise smartly, and take breaks!")

    elif user_input == "coding tips":
        print("Bot: Practice daily and don't fear errors.")

    elif user_input == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif user_input == "date":
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    elif user_input == "i am sad":
        print("Bot: Hope things get better soon. Keep smiling 😊")

    elif user_input == "i am happy":
        print("Bot: That's awesome! Keep smiling 😄")

    elif user_input == "bored":
        print("Bot: Try coding something fun today!")

    elif "college" in user_input:
        print("Bot: College life is all about learning and growth!")

    elif user_input == "i am tired":
        print("Bot: Take some rest and stay hydrated 😊")

    elif user_input == "i am stressed":
        print("Bot: You got this! Take one step at a time.")

    elif user_input == "i feel lonely":
        print("Bot: I'm here to chat with you 🤖")

    elif user_input == "i am excited":
        print("Bot: That's amazing! Enjoy the moment 😄")

    elif user_input == "what are you doing":
        print("Bot: Just waiting to chat with you!")

    elif user_input == "what should i eat":
        print("Bot: Maybe try something healthy and tasty 😋")

    elif user_input == "can i sleep":
        print("Bot: Yes, good sleep is important!")

    elif user_input == "weather":
        print("Bot: I can't check weather yet, but I hope it's nice outside!")

    elif user_input == "what is ai":
        print("Bot: AI means Artificial Intelligence, where machines mimic human thinking.")

    elif user_input == "python":
        print("Bot: Python is a beginner-friendly programming language.")

    elif user_input == "coding":
        print("Bot: Coding is fun once you start solving problems!")

    elif user_input == "debugging":
        print("Bot: Debugging means finding and fixing errors in code.")

    elif user_input == "flip a coin":
        print("Bot:", random.choice(["Heads! 🪙", "Tails! 🪙"]))

    elif user_input == "rock paper scissors":
        print("Bot: I choose", random.choice(["Rock 🪨", "Paper 📄", "Scissors ✂️"]))

    elif user_input == "roast me":
        print("Bot: Even your WiFi gives up faster than you 😆")

    elif user_input == "compliment me":
        print("Bot: You're doing great and learning every day 🌟")

    elif user_input == "2+2":
        print("Bot: 2 + 2 = 4")

    elif user_input == "motivation":
        print("Bot: Success comes from consistency, not perfection.")

    elif user_input == "study tips":
        print("Bot: Study in small sessions and take breaks.")

    elif user_input == "exam":
        print("Bot: Believe in yourself. Preparation beats fear!")

    elif user_input == "set goal":
        print("Bot: Great! What's your goal for today?")

    elif user_input == "remind me to study":
        print("Bot: Reminder: Study hard and make yourself proud!")

    elif user_input == "goodbye":
        print("Bot: Bye! Have a productive day 😊")

    elif "food" in user_input:
        print("Bot: Food makes everything better 😋")

    elif "friend" in user_input:
        print("Bot: Friends make life fun!")

    elif "study" in user_input:
        print("Bot: Stay focused, learning compounds over time!")

    elif "python" in user_input:
        print("Bot: Python is awesome for AI and automation!")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day 😊")
        break

    else:
        print("Bot: Sorry, I don't understand that.")