from pynput.keyboard import Key, Controller
import speech_recognition as sr
from pywinauto import application
import time
time.sleep(1)
import pyaudio
import os
from flask import Flask, render_template, request
import pyttsx3

apply = Flask(__name__)


@apply.route("/")
def home():
    return render_template("index.html")


@apply.route("/speech", methods=['POST'])
def speech():
    output = request.form.get('button')
    if output == 'button':
        r = sr.Recognizer()
        keyboard = Controller()
        app = application.Application()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Now You Can Speak")
            audio = r.listen(source)
            text = r.recognize_google(audio) + " "
            if text == 'start ':
                app.start("Notepad.exe")
                while text != 'stop ':
                    print("Speak")
                    audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio) + " "
                        if text == 'stop ':
                            pass
                        elif text == 'next line ':
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                        elif text == 'select up ':
                            keyboard.press(Key.shift)
                            keyboard.press(Key.up)
                            keyboard.release(Key.up)
                            keyboard.release(Key.shift)
                        elif text == 'select down ':
                            keyboard.press(Key.shift)
                            keyboard.press(Key.down)
                            keyboard.release(Key.down)
                            keyboard.release(Key.shift)
                        elif (text == 'select left 5 ') or (text == 'select left five '):
                            keyboard.press(Key.shift)
                            for x in range(0, 6):
                                keyboard.press(Key.left)
                                keyboard.release(Key.left)
                            keyboard.release(Key.shift)
                        elif (text == 'select right 5 ') or (text == 'select right five '):
                            keyboard.press(Key.shift)
                            for x in range(0, 6):
                                keyboard.press(Key.right)
                                keyboard.release(Key.right)
                            keyboard.release(Key.shift)
                        elif text == 'select left ':
                            keyboard.press(Key.shift)
                            keyboard.press(Key.left)
                            keyboard.release(Key.left)
                            keyboard.release(Key.shift)
                        elif text == 'select right ':
                            keyboard.press(Key.shift)
                            keyboard.press(Key.right)
                            keyboard.release(Key.right)
                            keyboard.release(Key.shift)
                        elif text == 'left ':
                            keyboard.press(Key.left)
                            keyboard.release(Key.left)
                        elif text == 'right ':
                            keyboard.press(Key.right)
                            keyboard.release(Key.right)
                        elif text == 'up ':
                            keyboard.press(Key.up)
                            keyboard.release(Key.up)
                        elif text == 'down ':
                            keyboard.press(Key.down)
                            keyboard.release(Key.down)
                        elif (text == 'left five ') or (text == 'left 5 '):
                            for x in range(0, 6):
                                keyboard.press(Key.left)
                                keyboard.release(Key.left)
                        elif (text == 'right five ') or (text == 'right 5 ') or (text == 'write five '):
                            for x in range(0, 6):
                                keyboard.press(Key.right)
                                keyboard.release(Key.right)
                        elif (text == 'up five ') or (text == 'up 5 '):
                            for x in range(0, 6):
                                keyboard.press(Key.up)
                                keyboard.release(Key.up)
                        elif (text == 'down five ') or (text == 'down 5 '):
                            for x in range(0, 6):
                                keyboard.press(Key.down)
                                keyboard.release(Key.down)
                        elif text == 'copy ':
                            keyboard.press(Key.ctrl)
                            keyboard.press('c')
                            keyboard.release('c')
                            keyboard.release(Key.ctrl)
                        elif text == 'paste ':
                            keyboard.press(Key.ctrl)
                            keyboard.press('v')
                            keyboard.release('v')
                            keyboard.release(Key.ctrl)
                        elif text == 'cut ':
                            keyboard.press(Key.ctrl)
                            keyboard.press('x')
                            keyboard.release('x')
                            keyboard.release(Key.ctrl)
                        elif text == 'backspace ':
                            keyboard.press(Key.backspace)
                            keyboard.release(Key.backspace)
                        elif (text == 'backspace 5 ') or (text == 'backspace five '):
                            for x in range(0, 6):
                                keyboard.press(Key.backspace)
                                keyboard.release(Key.backspace)
                        elif (text == 'backspace 10 ') or (text == 'backspace ten '):
                            for x in range(0, 11):
                                keyboard.press(Key.backspace)
                                keyboard.release(Key.backspace)
                        elif text == 'undo ':
                            keyboard.press(Key.ctrl)
                            keyboard.press('z')
                            keyboard.release('z')
                            keyboard.release(Key.ctrl)
                        elif text == 'save ':
                            app.Notepad.menu_select("File -> SaveAs")
                            print("say name")
                            audio_1 = r.listen(source)
                            text_1 = r.recognize_google(audio_1)
                            app.SaveAs.edit.set_edit_text(text_1 + ".txt")
                            app.SaveAs.Save.click()
                        elif text == 'open ':
                            app.Notepad.menu_select("File ->Open")
                            print("say name")
                            audio_1 = r.listen(source)
                            text_1 = r.recognize_google(audio_1)
                            app.Open.edit.set_edit_text(text_1 + ".txt")
                            app.Open.Open.click()
                        elif text == 'intensify ':
                            app.Notepad.menu_select("Fotmat ->Font")
                            app.Font.edit.set_edit_text("Cooper")
                            app.Font.OK.click()
                        elif text == 'exit ':
                            app.Notepad.menu_select("File ->Exit")
                            break

                        else:
                            for char in text:
                                keyboard.press(char)
                                keyboard.release(char)
                                time.sleep(0.05)
                            engine = pyttsx3.init()
                            engine.say(text)
                            engine.runAndWait()
                    except:
                        return render_template("index.html")
                print("Stopped")
    return render_template("index.html")


if __name__ == "__main__":
    apply.run(debug=True, port=5555)