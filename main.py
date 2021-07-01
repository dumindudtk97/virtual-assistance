import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()       # listner
engine = pyttsx3.init()           
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('I am your virtual asistant Shakira')		# initial response
engine.say('What can I do for you ?')
engine.runAndWait()

def talk(text):				#talk
    engine.say(text)
    engine.runAndWait()


def take_command():		# listen and take commands
    try:
        with sr.Microphone() as source:    #get code from microphone
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Shakira' in command:
                command = command.replace('Shakira', '')
                print(command)
    except:
        pass
    return command


def run_shakira():
    command = take_command()
    print(command)
    if 'search' in command:						#google search
        command = command.replace('search', '')
        pywhatkit.search(command)
    if 'play' in command:
        song = command.replace('play', '')			# play youtube videos
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')		# say time
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')			# wiki who is
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:						# wiki what is
        query = command.replace('what is', '')
        info = wikipedia.summary(query, 1)
        print(info)
        talk(info)
    elif 'hirushi' in command:						# whatsapp massaging
        pywhatkit.sendwhatmsg("+94785941314",'Good morning',18,40)
        print("Successfully Sent!")
    elif 'are you single' in command:			
        talk('I am in a relationship with you my love.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())						# jokes
    elif 'exit' in command:
        exit(0)
    else:										# if command not recognized
        talk('Please say the command again.')


while True:
    run_shakira()			# run
