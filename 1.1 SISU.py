import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine. setProperty("rate", 120)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("Hello I am Sisu, Desktop Voice Assistan")
    speak("sir, please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening....")
        speak("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak('Recognizing please wait')
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-US')
        print("User said: ",query)

    except Exception :
        
        print("...SORRY...\n")
        return "None"
    return query

def sendEmail(to, content):


    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Enter_your_email','enter_password')
    server.sendmail('Enter_your_email',to,content)
    server.close



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'your name' in query:
            query = query.replace("your name", "sisu")
            results = wikipedia.summary(query, sentences=2)
            speak("My name is sisu. it's S  I  S U.")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak("I'm great thanks.")
        
        elif 'search' in query:
            speak('Serching Wikipedia....')
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening Youtube....')
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("youtube.com")
        
        elif 'open google meet' in query:
            speak('Opening Google Meet....')
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("meet.google.com")
        
        elif 'open google' in str(query) or 'open chrome' in str(query):
            speak('Opening Google....')
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("google.com")

        elif 'open gmail' in str(query) or "open google mail" in str(query):
            speak('Opening Google Mail....')
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("gmail.com")

        elif 'open daffodil blc' in str(query) or 'open daffodil' in str(query) :
            speak('Opening DIU Blended Learning Center....')
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://elearn.daffodilvarsity.edu.bd/")

        elif 'play music' in query:
            music_path = 'E:\\ENGLISH   SONG\\English Rock'
            songs = os.listdir(music_path)
            print('playing...')
            print(songs)
            os.startfile(os.path.join(music_path,songs[0]))
            break

        elif 'the time' in query:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            
            print(f"sir, The time is : {now}")
            speak(f"sir, The time is : {now}")

        elif 'send email' in str(query) or 'send mail' in str(query):
            try:
                speak("To whom")
                to = input("Enter Email:")
                speak("What Should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception :
                print("Sorry Email has not sent at this moment try again")
                speak("Sorry Email has not sent at this moment try again")

        elif "exit" in str(query) or "bye" in str(query) or "sleep" in str(query):
            speak("OK sir, See you next time")
            break

        else:
            print("Not in list say the correct command")
            speak("Not in list say the correct command")




        
        

