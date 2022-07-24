import pyjokes as pyjokes
import pyttsx3
import webbrowser
import datetime
import speech_recognition as sr
import wikipedia
import os
import sys
import pywhatkit
e = pyttsx3.init('sapi5')
voice = e.getProperty('voices')


print(voice[0].id)
def speak(audio):
    e.say(audio)
    e.runAndWait()


def wish():
    h = int(datetime.datetime.now().hour)
    if h >= 0 and h < 12:
        speak("good morning het bro!!")
    elif h >= 12 and h < 18:
        speak("good afternoon het bro!!")
    else:
        speak("good evening het bro!!")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening bro speak what you say...')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing bro speak...")
            q = r.recognize_google(audio, language='en-in')
            print("user said :" + q)
        except Exception as e:
            print('say that please')
            return "None"
        return q


if __name__ == '__main__':
    wish()
    while True:
        q = command().lower()
        if 'wikipedia' in q:
            speak('searching.....')
            q = q.replace("wikipedia", "")
            r = wikipedia.summary(q, sentences=3)
            speak("according to wikipedia")
            speak(r)
            print(r)
        if 'hello' in q:
            say="hello, how can i help you ??"
            print('hello how can i helpp you ??')
            speak(say)
        elif 'who are you' in q:
            print('I am mini alexa a k a your virtual assistant master')
            speak('I am mini alexa a k a your virtual assistant master. how can i help you ??')
        elif 'can you do' in q:
            print('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
        open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google.How may i help you ??''')
            speak('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
        open different websites like insta gram, youtube,gmail, git hub, stack overflow and searches on google. How may i help you ??''')
        elif 'open google' in q:
            webbrowser.open("google.com")
        elif 'open youtube' in q:
            webbrowser.open("youtube.com")
        elif 'open facebook' in q:
            webbrowser.open("facebook.com")
        elif 'play' in q:
            song=q.replace('play','')
            pywhatkit.playonyt(song)
        elif "my location" in q:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("You must be somewhere near here, as per Google maps")
        elif 'open instagram' in q:
            print('opening instagram ...')
            speak('opening insta gram...')
            webbrowser.open_new('https://www.instagram.com/')
        elif 'open stack overflow' in q:
            print('opening stackoverflow ...')
            speak('opening stack overflow...')
            webbrowser.open_new('https://stackoverflow.com/')
        elif 'open github' in q:
            print('opening git hub ...')
            speak('opening git hub...')
            webbrowser.open_new('https://github.com/')
        elif 'locate ' in q:
            speak('locating ...')
            loc = q.replace('locate', '')
            if 'on map' in loc:
                loc = loc.replace('on map', ' ')
            url = 'https://google.nl/maps/place/' + loc + '/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of ' + loc)
            speak('Here is the location of ' + loc)
        elif 'on map' in q:
            speak('locating ...')
            loc = q.split(" ")
            print(loc[1])
            url = 'https://google.nl/maps/place/' + loc[1] + '/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of ' + loc[1])
            speak('Here is the location of ' + loc[1])

        elif 'location of' in q:
            speak('locating ...')
            loc = q.replace('find location of', '')
            url = 'https://google.nl/maps/place/' + loc + '/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of ' + loc)
            speak('Here is the location of ' + loc)
        elif 'what is' in q:
            name = q.replace('what is ', '')
            info = wikipedia.summary(name, 1)
            print(info)
            speak(info)
        elif 'who is ' in q:
            name = q.replace('who is', '')
            info = wikipedia.summary(name, 1)
            print(info)
            speak(info)
        elif 'what is ' in q:
            search = 'https://www.google.com/search?q=' + q
            print(' Here is what i found on the internet..')
            speak('searching... Here is what i found on the internet..')
            webbrowser.open(search)
        elif 'joke' in q:
            _joke = pyjokes.get_joke()
            print(_joke)
            speak(_joke)
        elif 'search' in q:
            search = 'https://www.google.com/search?q=' + q
            speak('searching... ')
            webbrowser.open(search)
        elif 'time' in q:
            stime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("time is :" + stime)
        elif 'open news' in q:
            webbrowser.open("https://www.gujaratsamachar.com/")
        elif 'thank you' in q:
            print("your welcome")
            speak('your welcome')
        elif 'stop' in q:
            print('good bye, have a nice day !!')
            speak('good bye, have a nice day !!')
            sys.exit()
        elif 'Bye' in q:
            print('good bye, have a nice day !!')
            speak('good bye, have a nice day !!')
            sys.exit()
