import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3
import show_attendance
import takeImage
import trainImage
import automaticAttedance

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "./haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "./Trainner.yml"
)
trainimage_path = "./TrainingImage"
studentdetail_path = (
    "./studentdetails.csv"
)
attendance_path = "./Attendance"


window = Tk()
window.title("Attendance Home")
window.geometry("1280x720")
dialog_title = "Quit"
dialog_text = "Are you sure want to quit?"
window.configure(background="white")

def del_sc1():
    sc1.destroy()

def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.title("Warning!")
    sc1.configure(background="white")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment No. and Name Requried",
        fg="blue",
        bg="white",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="Ok",
        command=del_sc1,
        fg="blue",
        bg="white",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

a = tk.Label(
    window,
    text="Attendance System Using Face Recognition",
    bg="white",
    fg="blue",
    bd=10,
    font=("arial", 35),
)
a.pack()

def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Image")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="white")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="white", relief=RIDGE, bd=10, font=("arial", 35))
    titl.pack(fill=X)
    titl = tk.Label(
        ImageUI, text="Register Student", bg="white", fg="green", font=("arial", 30),
    )
    titl.place(x=270, y=12)

    a = tk.Label(
        ImageUI,
        text="Enter Details",
        bg="white",
        fg="blue",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No.",
        width=10,
        height=2,
        bg="white",
        fg="blue",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="white",
        fg="blue",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="white",
        fg="blue",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="white",
        fg="blue",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Status",
        width=10,
        height=2,
        bg="white",
        fg="blue",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="white",
        fg="blue",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("times new roman", 18),
        bg="white",
        fg="blue",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="white",
        fg="blue",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)

r = tk.Button(
    window,
    text="Register New Student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="white",
    fg="blue",
    height=2,
    width=17,
)
r.place(x=320, y=360)

def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

r = tk.Button(
    window,
    text="Record Attendance",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="white",
    fg="blue",
    height=2,
    width=17,
)
r.place(x=640, y=360)

def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="white",
    fg="blue",
    height=2,
    width=17,
)
r.place(x=960, y=360)
r = tk.Button(
    window,
    text="Exit",
    bd=10,
    command=quit,
    font=("times new roman", 16),
    bg="white",
    fg="blue",
    height=2,
    width=17,
)
r.place(x=640, y=560)

window.mainloop()
