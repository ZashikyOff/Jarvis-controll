import webbrowser
import speech_recognition as sr
import subprocess

import lightcontroll.hue_lights as hl

 
r = sr.Recognizer()

def open_youtube():
    print("url ytb")
    webbrowser.open("https://youtube.com")

def open_arknight():
    projectpath = 'C:\\Users\\mariu\\Desktop\\Jeux\\Arknights.lnk'
    subprocess.check_call( ('start',projectpath) , shell=True )

def open_steam():
    projectpath = 'C:\Program Files (x86)\Steam\steam.exe'
    subprocess.check_call( ('start',projectpath) , shell=True )

game = []

while True:
    with sr.Microphone(2) as source:
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, None,"fr-FR")
            print("You said this : {}".format(command))
            print(command[18:])
            if command == "Jarvis lumière en " + command[18:]:
                color = command[18:]
                hl.bycolor(color)
            if command == "Jarvis lumière en arc-en-ciel":
                hl.rainbow()
            # if command == "ouvre YouTube":
            #     open_youtube()
            # if command == "ouvre Steam":
            #     open_steam()
            # if command == "ouvre Arknights":
            #     open_arknight()

        except Exception as e:
            print(" ")