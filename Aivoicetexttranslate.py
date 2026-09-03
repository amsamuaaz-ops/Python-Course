import speech_recognition as sr
from googletrans import Translator


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nPlease speek in english now")
        audio = recognizer.listen(source)


    try:
        print("Recognizing Speach")
        text = recognizer.recognize_google(audio,language="en-US")
        print(f"You said: {text}")
        return text
    
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"API error:{e}")
    return ""

def translate_text(text,target_language="ur"):
    translator = Translator()
    translation = translator.translate(text , dest=target_language)
    print(f"Translated Text:{translation.text}")
    return translation.text


def display_language_options():
    print("\nAvalible transalion languages")
    print("1.Hindi(hi)")
    print("2.Tamil(ta)")
    print("3.Teluga(te)")
    print("4.Bengali(Bn)")
    print("5.Marathi(mr)")
    print("6.Gujrati(gu)")
    print("7.Malayalam(ml)")
    print("8.Punjabi(pa)")
    print("9.Urdu(ur)")

    choice = input("Please select a number to choose language(1-9)")
    language_dict = {
        "1":"hi",
        "2":"ta",
        "3":"te",
        "4":"bn",
        "5":"mr",
        "6":"gu",
        "7":"ml",
        "8":"pa",
        "9":"ur"
    }

    return language_dict.get(choice,"ur")


def main():
    target_language = display_language_options()

    original_text = speech_to_text()

    if original_text:
        translate_text(original_text,target_language=target_language)

if __name__ == "__main__":
    main()