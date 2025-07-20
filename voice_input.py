import speech_recognition as sr

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"📝 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return None
    except sr.RequestError:
        print("❌ Speech service error")
        return None