import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil 
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak('Welcome!')
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour >= 18 and hour<24:
        speak("Good evening")
    else:
        speak("Good Night")
    speak("Jarvis at your service. Please tell how can i help you?")
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Can you please say again")

        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', '123')
    server.sendmail('abc@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:\Users\vijaya\Jarvis\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" +usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()

        elif 'date' in query:
            date()
        
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendEmail(to, content)
                speak(content)
                speak("Email Sent Successfully!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")

        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ '.com')

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'E:\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember' in query:
            speak("What Should I remember?")
            data = takeCommand()
            speak("You said to me to remember that"+data )
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
    
        elif 'reminder' in query:
            remember = open('data.txt', 'r')
            speak("Here are your reminders " + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot taken successfully!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("My Pleasure!Good Bye!")
            quit()
    



        