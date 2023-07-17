#!/usr/bin/env python3                                                                                

import speech_recognition as sr  
                                                                    
r = sr.Recognizer()   # getting audio from the microphone                                                                                 
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
