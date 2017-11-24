#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

GOOGLE_CLOUD_SPEECH_CREDENTIALS = ""

with open(r"/home/pi/Downloads/rpi-arm-raspbian-8.0-1.1.1/resources/voicehub-15fe71d0a718.json", "r") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

# recognize speech using Google Cloud Speech
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))