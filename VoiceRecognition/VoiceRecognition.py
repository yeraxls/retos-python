import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()

def talk():
    mic = sr.Microphone()
    with mic as source:
        print("di algo:")
        audio = recognizer.listen(source)
    
    text = recognizer.recognize_sphinx(audio_data=audio, language="es-ES")

    print(f"has dicho: {text}")

    return text.lower()
if "amazon" in talk():
    engine.say("¿Qué quieres comprar en amazon?")
    engine.runAndWait()

    text = talk()

    webbrowser.open(f"https://www.amazon.es/s?k={text}") 