import pyttsx3

engine = pyttsx3.init(driverName='sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("I will speak this text")
engine.runAndWait()



for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()