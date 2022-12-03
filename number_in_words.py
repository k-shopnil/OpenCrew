import os
from gtts import gTTS
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg

func_root = Tk()
from numcall import numcallmachine
from numcall import numcallmachine2

# gui logic here
func_root.geometry("1280x720")
func_root.minsize(480, 360)
func_root.maxsize(1920, 1080)
func_root.title("NumCall v1.0.9")


# title = Label(text="Number in Words", bg="#00FF00", fg="#ffffff",
#               padx="1280", font="blenderpro 19 bold")
# title.pack()
numbers_in_words_speech = ""


def submit():
    collector = numcallmachine(field.get())
    if collector != "":
        output.config(text="Your number would pronounce: \n " + collector)

    else:
        msg.showerror("Invalid Number", "Please enter numbers only!", icon="error")


def playback():
    acollector = numcallmachine2(field.get())
    language = 'en'
    aoutput = gTTS(text=acollector, lang=language, slow=False)
    aoutput.save("aoutput.mp3")
    conf = msg.askyesno(title="Listen", message="Do you want to hear it aloud?")
    if conf == True:
        os.system("aoutput.mp3")
    else:
        msg.showinfo(title="Feedback", message="Okay")


audiobtn = Button(func_root, text="Listen", command=playback)
audiobtn.pack(pady="60")
output = Label(func_root, text="", font="blenderpro 18", pady="50")
output.pack()
prompt = Label(func_root, text="Enter your number:", font="blenderpro 14")
prompt.pack(pady="50")
field = Entry(func_root)
field.pack(pady="50")
board = Button(func_root, text="Submit", command=submit)
board.pack()
status_bar = Label(text="Version - Beta", bg="#DC143C", fg="#ffffff",
                   font="blenderpro 11 bold")
status_bar.pack(anchor="s", side="bottom", fill=X)
j_image = Image.open('asset.jpg')
Out_j_image = ImageTk.PhotoImage(j_image)
imagery_b = Label(image=Out_j_image)
imagery_b.pack(fill=Y)

# b_image = PhotoImage(file="1.png")
# imagery_b = Label(image=b_image)
# imagery_b.pack()
# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
func_root.mainloop()
