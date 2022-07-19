import pyttsx3
import datetime
import speech_recognition as sr 

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("this is jarvis")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is : "+Time)

#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is :")
    speak(date)
    speak(month)
    speak(year)

#date()

def greet():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning")
        speak("Jarvis at your service")
        time()
        date()
        speak("how may I help you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        speak("Jarvis at your service")
        time()
        date()
        speak("how may I help you")
    elif hour >= 18 and hour < 24:
        speak("Good Evening")
        speak("Jarvis at your service")
        time()
        date()
        speak("how may I help you")
    else:
        speak("Good Night")

greet()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Unable to get that, say that again please...")

        return "None"
    return query
takeCommand()