from tkinter import *
import time
myvar=True


def toggleButton():
    global myvar
    if myvar==True:
        label1.config(font="Imperial",text="New Text",background="lime")
    elif myvar==False:
        label1.config(font="Arial",text=input.get(),background="pink")
    myvar= not myvar

def toggleLabel():
    print(label1.cget("state"))
    if label1.cget("state")=="disabled":
        label1.config(state="active")
    elif label1.cget("state")=="active":
        label1.config(state="disabled")
        
        

window=Tk()
window.geometry("400x300")
#window.title="bu neden olmyor yav"
window.title("My first Tkinter")
label1=Label(text="deneme",state="disabled")
label1.pack()
#button1=Button(text="merhaba", command=lambda: label1.config(state="active"))
button1=Button(text="merhaba", command=toggleButton)
button2=Button(text="Test Label", command=toggleLabel)

input=Entry(width=20,bg="yellow", foreground="navyblue")
#input.insert(1,"sa\n")
input.insert(0,"default val")




button1.pack()
input.pack()
button2.pack()

window.mainloop()

