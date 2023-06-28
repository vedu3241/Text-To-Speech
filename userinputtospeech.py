import os
from gtts import gTTS
from tkinter import *

window = Tk()
def convert():
    text = input_entry.get()
    output = gTTS(text=text,lang='en',slow=False)
    output.save('user.mp3')
    return os.system("start user.mp3")
   

window.title("Text To Speech Converter")
canvas= Canvas(window,width=600,height=300)
canvas.pack()


user_input = Label(
    window, text="Enter the text that you want to convert to speech: ")
canvas.create_window(250,160,window=user_input)
input_entry = Entry(window)
canvas.create_window(450,160,window=input_entry)

cnv_btn = Button(window, text="Convert",command = lambda:convert())
canvas.create_window(250,200,window=cnv_btn)

window.mainloop()
