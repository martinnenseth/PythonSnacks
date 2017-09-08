import speech_recognition as sr
import pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


recognizer = sr.Recognizer()
recognizerInput = sr.Microphone()

try:
    print ("Hello, please be silent.")
    engine.say("Gretings, travler")
    with recognizerInput as source: recognizer.adjust_for_ambient_noise(source)
    format(recognizer.energy_threshold)
finally:
    engine.setProperty("voice", voices[1])
    engine.say("Thank you, please come again.")
    print ("Fucker!")
engine.runAndWait()

