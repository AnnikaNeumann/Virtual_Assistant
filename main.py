import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import wikipedia

listener = sr.Recognizer()
#text to speech
engine = pyttsx3.init()
# get different voices for Data and change it by index
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Let me hear what you have to say...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Data' in command:
                command = command.replace('Data', "")
                print(command)

    except:
        pass
    return command


def run_data():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', "")
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with spot')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')


while True:
    run_data()
