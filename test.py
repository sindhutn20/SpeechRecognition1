from pynput.keyboard import Key, Controller
import speech_recognition as sr
from pywinauto import application
import time
time.sleep(1)
import pyaudio
import os
from flask import Flask, render_template, request
import pyttsx3

r = sr.Recognizer()
keyboard = Controller()
app = application.Application()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Now You Can Speak")
    app.start("Notepad.exe")
    audio = r.listen(source)
    text = r.recognize_google(audio) + " "
    try:
        app.NotePad.menu_select("File -> SaveAs")
        print("say name")
        audio_1 = r.listen(source)
        text_1 = r.recognize_google(audio_1)
        app.SaveAs.edit.set_edit_text(text_1 + ".txt")
        app.SaveAs.Save.click()
    except Exception as e:
        print("An error occurred:", str(e))
