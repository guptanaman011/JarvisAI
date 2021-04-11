import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good night sir!")
    speak("I am Jarvis. Please tell me how may I help you")

def takeCommand():
    # it takes microphone inout from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Sorry I didn't get you Please try again...")
        return "None"
    return query

def sendEmail(to, content):
    # less secure apps enable from your gmail account
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your-email", "your-password")
    server.sendmail('EMAIL', to, content)
    server.close()

if __name__ == "__main__":
        speak("hello")
        wishMe()
        while True:
            query = takeCommand().lower()

            # logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak('According to Wikipedia')
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open instagram' in query:
                webbrowser.open("instagram.com")

            elif 'play music' in query:
                music_dir = 'E:\\vinay module\\area under thre curve'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open pycharm' in query:
                pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
                os.startfile(pycharmPath)

            elif 'email to naman' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "MAIL"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry I am not able to send this email")
            elif 'shutdown jarvis' in query:
                speak("Thanks for you time sir. Have a good day")
                print("Shutting down...")
                break






