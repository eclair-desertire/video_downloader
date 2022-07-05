from cgitb import text
from pydoc import plain
from tkinter import *
from tkinter import font
from pytube import YouTube



root=Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Video downloader")
root.configure(bg="#f2eee3")

Label(root, text="Youtube Video downloader",font="arial 20 bold",
    bg="#f2eee3",fg="red").pack()

link=StringVar()
Label(root,text="Paste the YouTube link here:",font="arial 15 bold",
    bg="#f2eee3").place(x=40,y=40)
link_enter=Entry(root, width=50, textvariable=link).place(x=32,y=90)


def downloader():
    YouTube(str(link.get())).streams.first().download()
    Label(root, text="DOWNLOADED",font="arial 13",bg="#f2eee3",
    fg="red").place(x=185,y=210)

Button(root,
    text="DOWNLOAD",
    font="arial 15 bold",
    bg="pale violet red",
    padx=2,
    command=downloader,
    fg="blue").place(x=180,y=150)



root.mainloop()