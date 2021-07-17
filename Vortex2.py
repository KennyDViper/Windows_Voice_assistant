import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')


voices = engine.getProperty('voices')

print(voices[1].id)

engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning User")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon User")
    else:
        speak("Good Evening User")
    speak("Vortex your AI, at your service sir!")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)

        print("Say that again please.....")
        return "None"
    return query

    
        

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia.......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to the wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'are you there' in query:
            speak("Always at your service Sir")
        elif 'how are you' in query:
            speak("Im good thank you sir")
        elif 'are you listening' in query:
            speak("Yes sir, you have my attention")
        
        else:
            speak("sorry sir didn't recognize that")
            
            
                  
        
    
    
