import webbrowser
import speech_recognition as sr
import subprocess

import lightcontroll.hue_lights as hl


from speech_recognition import Recognizer, Microphone

recognizer = Recognizer()


while True:
    with Microphone(2) as source:
        print("Réglage du bruit ambiant... Patientez...")
        recognizer.adjust_for_ambient_noise(source)
        print("Vous pouvez parler...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, None,"fr-FR")
            print("Vous avez dit : {}".format(command))
        
        except Exception as ex:
            print(ex)