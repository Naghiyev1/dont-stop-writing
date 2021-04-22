from tkinter import *

global _after_id
_after_id = None
global COUNT
COUNT = 10
global timer
timer = None

def handle_wait(event):
    # cancel the old job
    global _after_id
    global timer
    global COUNT
    if _after_id is not None:
        COUNT = 10
        window.after_cancel(_after_id)
        window.after_cancel(timer)
        timerlabel.config(text=COUNT)
    # create a new job
    timerlabel.config(text=COUNT)
    timer = window.after(1000, CountDown)
    _after_id = window.after(10000, DeleteText)

def CountDown():
    global COUNT
    global timer
    global _after_id
    COUNT -= 1
    timerlabel.config(text=COUNT)
    window.after_cancel(timer)
    if COUNT > 0:
        timer = window.after(1000, CountDown)
    else:
        _after_id = None

def DeleteText():
    editor.delete(1.0, END)
    global timer
    global COUNT
    window.after_cancel(timer)
    COUNT = 10
    timerlabel.config(text=COUNT)

def SavetoTXT():
    with open("text_dump.txt", "w") as file:
        file.write(editor.get(1.0, END))

# Interface
global window
window = Tk()
window.update()
window.title("The Creative Writing App")
window.config(padx=20, pady=10)
#labels
Mainlabel = Label(text="Sometimes a bit of pressure works wonders for creativity!", font=("Arial", 14))
Mainlabel.grid(row=0,column=0)
subtitlelabel = Label(text="If you stop typing for 10 seconds your work will disappear. Created for creative writers who want to write first drafts without worrying about editing or formatting.")
subtitlelabel.grid(row=1,column=0)
global timerlabel
timerlabel = Label(text=COUNT, font=("Arial", 14, "bold"))
timerlabel.grid(row=2, column=0)

#buttons
savebutton = Button(text="Save progress to TXT file", command=SavetoTXT)
savebutton.grid(row=4, column=0, sticky="E", pady=20)

#other widgets
global editor
editor = Text()
editor.grid(row=3,column=0)
editor.bind("<Key>", handle_wait)

window.mainloop()
