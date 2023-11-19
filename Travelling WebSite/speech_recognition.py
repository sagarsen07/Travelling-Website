import speech_recognition as sr
import pyttsx3
import webbrowser
import os

a=pyttsx3.init('sapis5')
voice=a.getProperty('voices')
a.setProperty('voice',voice[1].id)

def speak(audio):
    a.say(audio)
    a.runAndWait()

def takeCommand():
    r=sr.recognizer()
    with sr.Microphone() as source:
        speak("you may give your command")
        r.pause_threhold=1
        audio=r.listen(source)
    try:
       print("recognizing....")
       query=r.recognize_google(audio,language='en-in')
       print(f"command is:{query}\n")
    except Exception as e:
        speak("please try to give another command")
        return "none"
    return query

if _name_== "_main_":
    while True:
        query=takeCommand().lower()
        if 'youtube'in query:
            webbrowser.open("youtube.com")
            speak("you may start watch videos on youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opened google")

        elif'open linkedin' in query:
            webbrowser.open("linkedin.com")
            speak("linkedin opened")

        elif 'open book' in query:
            codepath="H:\\Test\\Book.pdf"
            os.startfile(codepath)
            speak("this is your book")
