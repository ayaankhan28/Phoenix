import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()#Creates a speech recognition object.

    with sr.Microphone() as source:# Opens a microphone as a source for audio input.
        print("Say something:")
        #recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        sr.pause_threshold = 1#pause
        audio = recognizer.listen(source)#captures audio

    try:
        text = recognizer.recognize_google(audio, language='en-in')#converts
        return ("You said:", text)
    except sr.UnknownValueError:
        return ("Could not understand audio.")
    except sr.RequestError as e:
        return (f"Error with the speech recognition service: {e}")


