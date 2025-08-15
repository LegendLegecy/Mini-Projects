import pyttsx3


def speak(text):
    engine = pyttsx3.init("sapi5")
    voice = engine.getProperty("voices")
    engine.setProperty("voice", voice[1].id)
    engine.say(text)
    engine.runAndWait()

inp= input("\nEnter some thing:")
speak(inp)