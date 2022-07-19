#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import datetime

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:

    while True:
        audio = r.listen(source)

        #recognizes speech using google as a service (this works online)
        text = r.recognize_google(audio)

        if str(text).lower() == "what time is it":
            Time = datetime.datetime.now().strftime("%I:%M:%S")
            print(Time)
        
        #print(text)


