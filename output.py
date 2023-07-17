import pyttsx3
engine = pyttsx3.init()

# convert this text to speech
text = "Hi, this is baymax your personal healthcare companion"
frequency = 120
engine.setProperty("rate", frequency)
engine.say(text)
# play the speech
engine.runAndWait()