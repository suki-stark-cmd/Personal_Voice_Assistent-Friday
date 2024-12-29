
import datetime
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import pyjokes
import wikipedia
import requests
from translate import Translator
import openai  # Install `openai` for ChatGPT integration

# OpenAI API Key (replace with your actual API key)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Friday, your Assistant. How can I help you?")


def takeCommand():
    """Listen to and recognize the user's voice command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query.lower()


def handleCommonQuestions(query):
    """Handle predefined common questions."""
    responses = {
        "how are you": "I'm fine, thank you for asking. How are you?",
        "who made you": "I was created by Abin and Jibin.",
        "what is love": "Love is an emotion that makes life beautiful.",
        "who are you": "I am Friday, your virtual assistant.",
        "why are you here": "I am here to assist you with tasks and answer your questions."
    }
    for key in responses:
        if key in query:
            speak(responses[key])
            return True
    return False


def askChatGPT(query):
    """Query OpenAI's ChatGPT API for a response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ]
        )
        answer = response['choices'][0]['message']['content']
        print(f"ChatGPT: {answer}")
        speak(answer)
    except Exception as e:
        print("Error querying ChatGPT:", e)
        speak("Sorry, I couldn't process your request. Please try again later.")


def openApplicationOrWebsite(query):
    """Open applications or websites based on the query."""
    if 'open youtube' in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif 'open facebook' in query:
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")
    elif 'open instagram' in query:
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")


def tellTime():
    """Tell the current time."""
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")


def translateText():
    """Translate text from English to Spanish and German."""
    speak("What should I translate?")
    text_to_translate = takeCommand()
    if text_to_translate != "None":
        translator = Translator(from_lang="english", to_lang="spanish")
        translation = translator.translate(text_to_translate)
        print(f"Spanish: {translation}")
        speak(f"In Spanish: {translation}")

        translator = Translator(from_lang="english", to_lang="german")
        translation = translator.translate(text_to_translate)
        print(f"German: {translation}")
        speak(f"In German: {translation}")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'open' in query:
            openApplicationOrWebsite(query)
        elif 'time' in query:
            tellTime()
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif 'translate' in query:
            translateText()
        elif handleCommonQuestions(query):
            continue
        elif 'search' in query or 'tell me about' in query:
            query = query.replace("search", "").replace("tell me about", "").strip()
            askChatGPT(query)
        elif 'bye' in query or 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a great day.")
            break
