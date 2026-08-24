import colorama
from colorama import Fore,Style
from textblob import TextBlob


colorama.init()

print(f"{Fore.CYAN} \==--WELCOME TO SENTIMENT SPY!--==/ {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}===Please enter your name===")

if not user_name:
    user_name = "Mystrey Agent"

convertion_history = []

print(f"\n{Fore.CYAN}Hello Agent{user_name}!")

print(f"Type a sentence and i will analyze your sentences from textblob and show your sentiment")
print(f"Type{Fore.YELLOW}reset{Fore.CYAN},{Fore.YELLOW}history{Fore.CYAN},"
      f"or {Fore.YELLOW}exit{Fore.CYAN}to quiet")

while True:
    user_input = input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a valid command or some text {Style.RESET_ALL}")
        continue

    if user_input.lower =="exit":
        print(f"\n{Fore.BLUE}Exiting sentiment spy.FARWELL AGENT")

    elif user_input.lower == "reset":
        convertion_history.clear()
        print(f"{Fore.CYAN}ALL CONVERTION HISTORY CLEARED")

    elif user_input.lower == "history":
        if not convertion_history:

          print(f"{Fore.CYAN}No convertion history yet{Style.RESET_ALL}")

        else:
              print(f"{Fore.CYAN}Convertion history{Style.RESET_ALL}")
              for idx, (text, poliarty, sentiment_type) in enumerate(convertion_history,start=1):
                  if sentiment_type == "Positive":
                      color = Fore.GREEN
                      emoji = ":)"

                  elif sentiment_type == "Negetive":
                      color = Fore.RED
                      emoji = ":("

                  else:
                      color = Fore.YELLOW
                      emoji = ":("

              
                  print(f"{idx}. {color}{emoji} {text} "

                   f"Polarity: {poliarty:.2f}, {sentiment_type}{Style.RESET_ALL}")

        continue

# Analyze sentiment
    poliarty = TextBlob(user_input).sentiment.polarity

    if poliarty > 0.25:
        sentiment_type = "Positive"

        color = Fore.GREEN

        emoji = "😊"

    elif poliarty < -0.25:

        sentiment_type = "Negative"

        color = Fore.RED

        emoji = "😞"

    else:

        sentiment_type = "Neutral"

        color = Fore.YELLOW

    emoji = "😭"



    convertion_history.append((user_input, poliarty, sentiment_type))



    print(f"{color}{emoji} {sentiment_type} sentiment detected! "

       f"Polarity: {poliarty:.2f}")