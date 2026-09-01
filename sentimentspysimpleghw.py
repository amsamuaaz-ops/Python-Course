import colorama
import time
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

conversation_history = []


def show_processing_animation():
    print(f"{Fore.CYAN}Analyzing", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print(Style.RESET_ALL)


def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    return polarity, sentiment_type, color, emoji


def execute_command(command):
    global conversation_history

    if command == "summary":
        if not conversation_history:
            print(f"{Fore.YELLOW}No sentiment data available yet.{Style.RESET_ALL}")
        else:
            positive = sum(1 for item in conversation_history if item[2] == "Positive")
            negative = sum(1 for item in conversation_history if item[2] == "Negative")
            neutral = sum(1 for item in conversation_history if item[2] == "Neutral")

            print(f"\n{Fore.CYAN}Sentiment Summary:{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Positive: {positive}{Style.RESET_ALL}")
            print(f"{Fore.RED}Negative: {negative}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Neutral: {neutral}{Style.RESET_ALL}")

    elif command == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}All conversation history cleared!{Style.RESET_ALL}")

    elif command == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")

            for idx, (text, polarity, sentiment_type) in enumerate(
                conversation_history, start=1
            ):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(
                    f"{idx}. {color}{emoji} {text} "
                    f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}"
                )

    elif command == "help":
        print(f"\n{Fore.CYAN}Available Commands:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}summary{Style.RESET_ALL} - Show sentiment summary")
        print(f"{Fore.YELLOW}reset{Style.RESET_ALL} - Clear all stored data")
        print(f"{Fore.YELLOW}history{Style.RESET_ALL} - Show previous messages")
        print(f"{Fore.YELLOW}help{Style.RESET_ALL} - Show available commands")
        print(f"{Fore.YELLOW}exit{Style.RESET_ALL} - Exit the chatbot")


def get_valid_name():
    while True:
        name = input(
            f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}"
        ).strip()

        if name and name.isalpha():
            return name

        print(
            f"{Fore.RED}Please enter a name using alphabetic characters only."
            f"{Style.RESET_ALL}"
        )


print(f"{Fore.CYAN}Welcome to Sentiment Spy!{Style.RESET_ALL}")

user_name = get_valid_name()

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(
    f"Type a sentence and I will analyze its sentiment.\n"
    f"Type {Fore.YELLOW}summary{Fore.CYAN}, "
    f"{Fore.YELLOW}reset{Fore.CYAN}, "
    f"{Fore.YELLOW}history{Fore.CYAN}, "
    f"{Fore.YELLOW}help{Fore.CYAN}, "
    f"or {Fore.YELLOW}exit{Fore.CYAN}.{Style.RESET_ALL}\n"
)

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(
            f"{Fore.RED}Please enter some text or a valid command."
            f"{Style.RESET_ALL}"
        )
        continue

    command = user_input.lower()

    if command == "exit":
        print(
            f"\n{Fore.BLUE}Exiting Sentiment Spy. "
            f"Farewell, Agent {user_name}!{Style.RESET_ALL}"
        )
        break

    elif command in ["summary", "reset", "history", "help"]:
        execute_command(command)
        continue

    show_processing_animation()

    polarity, sentiment_type, color, emoji = analyze_sentiment(user_input)

    conversation_history.append(
        (user_input, polarity, sentiment_type)
    )

    print(
        f"{color}{emoji} {sentiment_type} sentiment detected! "
        f"Polarity: {polarity:.2f}{Style.RESET_ALL}"
    )


positive = sum(1 for item in conversation_history if item[2] == "Positive")
negative = sum(1 for item in conversation_history if item[2] == "Negative")
neutral = sum(1 for item in conversation_history if item[2] == "Neutral")

summary = (
    f"Sentiment Analysis Report for {user_name}\n"
    f"----------------------------------------\n"
    f"Positive Sentiments: {positive}\n"
    f"Negative Sentiments: {negative}\n"
    f"Neutral Sentiments: {neutral}\n"
    f"Total Sentences Analyzed: {len(conversation_history)}\n"
)

print(f"\n{Fore.CYAN}{summary}{Style.RESET_ALL}")

filename = f"{user_name}_sentiment_analysis.txt"

with open(filename, "w") as file:
    file.write(summary)

print(
    f"{Fore.GREEN}Report saved as {filename}{Style.RESET_ALL}"
)