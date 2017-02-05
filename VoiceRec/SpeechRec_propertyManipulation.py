import pyttsx


engine = pyttsx.init()
voices = engine.getProperty("voices")
engine.getProperty("rate")
engine.setProperty('rate', 125)
engine.say("So cute they are! I love cute doggies, do you love cute doggies, Kristina?")
engine.runAndWait()

