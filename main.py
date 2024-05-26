import wikipedia
import speech_recognition as sr
import pyjokes
import pyttsx3
import datetime
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def speak_command():
    try:
        with sr.Microphone() as source:
            print('I am listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri', '')
                print(command)

    except:
        pass
    return command
def run_siri():
    command = speak_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('The current time is ' + time)
    elif 'who is ' in command or 'what is ':
        answer = command.replace('who is', '')
        answer = command.replace('what is', '')
        info = wikipedia.summary(answer, 1)
        print(info)
        speak(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        speak(pyjokes.get_joke())
    else:
        print("I can't understand you. Please say that again...")
        speak("I can't understand you. Please say that again...")

while True:
    run_siri()