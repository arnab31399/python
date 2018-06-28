#gui

import tkinter

window=tkinter.Tk()
window.title("Hello")
window.geometry("400x400")
window.configure(background="#ff0000")#2 red 2 green 2 blue
lbl=tkinter.Label(window,text="Welcome  to GUI using tkinter",bg="green",fg="white")#obj of label background foreground
lbl.pack()## for display one after another
##
txt=tkinter.Entry(window,bg="black",fg="white")#Entry for textbox
txt.pack()
##
def disp():
    s=txt.get()
    s='Hello '+s
    lblresult.config(text=s)#text of the label chnge CONFIG FUNCTION   


b=tkinter.Button(window,text="Click",bg="cyan",fg="red",command=disp)
b.pack()
##
lblresult=tkinter.Label(window,text="",bg="green",fg="white")
lblresult.pack()
