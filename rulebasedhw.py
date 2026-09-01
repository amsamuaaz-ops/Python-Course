import re
import random
from colorama import Fore, init

init(autoreset=True)


weather = {
    "london": "Cloudy, 18°C",
    "paris": "Sunny, 21°C",
    "tokyo": "Partly cloudy, 24°C",
    "dubai": "Sunny, 35°C",
    "new york": "Clear, 23°C",
    "sydney": "Sunny, 20°C"
}


news = [
    "New travel routes are being introduced in several major cities.",
    "Many travelers are choosing sustainable travel options.",
    "Popular tourist locations are preparing for more visitors."
]


local_times = {
    "london": "8:00 PM",
    "paris": "9:00 PM",
    "tokyo": "4:00 AM",
    "dubai": "11:00 PM",
    "new york": "3:00 PM",
    "sydney": "5:00 AM"
}


def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def matches_keyword(text, keywords):
    pattern = r"\b(" + "|".join(map(re.escape, keywords)) + r")\b"
    return re.search(pattern, text) is not None


def weather_information():

    print(Fore.CYAN + "TravelBot: Which city?")
    city = normalize_input(input(Fore.YELLOW + "You: "))

    if city in weather:
        print(
            Fore.GREEN +
            f"TravelBot: Weather in {city.title()}: {weather[city]}"
        )
    else:
        print(
            Fore.RED +
            "TravelBot: Sorry, I don't have weather information "
            "for that city."
        )


def show_news():

    print(Fore.CYAN + "TravelBot: Travel News:")

    for item in news:
        print(Fore.GREEN + "- " + item)


def local_time():

    print(Fore.CYAN + "TravelBot: Which city?")
    city = normalize_input(input(Fore.YELLOW + "You: "))

    if city in local_times:
        print(
            Fore.GREEN +
            f"TravelBot: Local time in {city.title()}: "
            f"{local_times[city]}"
        )
    else:
        print(
            Fore.RED +
            "TravelBot: Sorry, I don't have the local time "
            "for that city."
        )


def show_help():

    print(Fore.MAGENTA + "\nI can:")

    print(
        Fore.GREEN +
        "- Give weather information (say 'weather')"
    )

    print(
        Fore.GREEN +
        "- Give travel news (say 'news')"
    )

    print(
        Fore.GREEN +
        "- Give local time (say 'time')"
    )

    print(
        Fore.CYAN +
        "Type 'exit' or 'bye' to end.\n"
    )


def chat():

    print(Fore.CYAN + "Hello! I'm TravelBot.")

    name = input(Fore.YELLOW + "Your name? ")
    name = normalize_input(name)

    print(
        Fore.GREEN +
        f"Nice to meet you, {name.title()}!"
    )

    show_help()

    while True:

        user_input = input(
            Fore.YELLOW + f"{name.title()}: "
        )

        user_input = normalize_input(user_input)

        weather_keywords = [
            "weather",
            "forecast",
            "temperature"
        ]

        news_keywords = [
            "news",
            "update",
            "updates"
        ]

        time_keywords = [
            "time",
            "clock",
            "local"
        ]

        help_keywords = [
            "help"
        ]

        exit_keywords = [
            "exit",
            "bye",
            "goodbye"
        ]

        if matches_keyword(user_input, weather_keywords):
            weather_information()

        elif matches_keyword(user_input, news_keywords):
            show_news()

        elif matches_keyword(user_input, time_keywords):
            local_time()

        elif matches_keyword(user_input, help_keywords):
            show_help()

        elif matches_keyword(user_input, exit_keywords):
            print(Fore.CYAN + "Safe Travels BYE!!")
            break

        else:
            print(
                Fore.RED +
                "TravelBot: Please Rephrase it"
            )


if __name__ == "__main__":
    chat()
