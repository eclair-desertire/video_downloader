import threading
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


def download_video():
    url=YouTube(str(link.get()))
    print(url.streams)
    video=url.streams[2]
    video.download()
    Label(root, text="DOWNLOADED",font="arial 13",bg="#f2eee3",
    fg="red").place(x=185,y=210)

def download_audio():
    url=YouTube(str(link.get()))
    for i in url.streams:
        print("Formats: "+str(i))
    
Button(root,
    text="DOWNLOAD VIDEO",
    font="arial 15 bold",
    bg="pale violet red",
    padx=2,
    command=download_video,
    fg="blue").place(x=180,y=150)

Button(root,
    text="DOWNLOAD ONLY AUDIO",
    font="arial 15 bold",
    bg="pale violet red",
    padx=2,
    command=download_audio,
    fg="blue").place(x=180,y=180)


root.mainloop()