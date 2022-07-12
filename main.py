import threading
from tkinter import *
from tkinter import font
from pytube import YouTube


root=Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Video downloader")
root.configure(bg="black")

Label(root, text="Youtube Video downloader",font="arial 20 bold",
    bg="black",fg="red").pack()

quality=IntVar()
Radiobutton(text="360p", value=1, variable=quality, padx=15, pady=10).place(x=130,y=210)
Radiobutton(text="720p", value=2, variable=quality, padx=15, pady=10).place(x=210,y=210)
Radiobutton(text="1080p", value=3, variable=quality, padx=15, pady=10).place(x=290,y=210)

link=StringVar()
Label(root,text="Paste the YouTube link here:",font="arial 15 bold",
    bg="black").place(x=40,y=40)
link_enter=Entry(root, width=50, textvariable=link).place(x=32,y=90)


def download_video():
    url=YouTube(str(link.get()))
    print(url.streams)
    video=url.streams[int(quality.get())]
    video.download()
    Label(root, text="DOWNLOADED",font="arial 13",bg="black",
    fg="red").place(x=195,y=250)

def download_audio():
    url=YouTube(str(link.get()))
    audio=url.streams.filter(only_audio=True)
    for i in audio:
        print("Formats: "+str(i))
    dwn=audio[1]
    dwn.download()
    Label(root, text="DOWNLOADED",font="arial 13",bg="black",
    fg="red").place(x=195,y=250)
    
Button(root,
    text="DOWNLOAD VIDEO",
    font="arial 15 bold",
    bg="pale violet red",
    padx=2,
    command=threading.Thread(target=download_video).start,
    fg="blue").place(x=170,y=150)

Button(root,
    text="DOWNLOAD ONLY AUDIO",
    font="arial 15 bold",
    bg="pale violet red",
    padx=2,
    command=threading.Thread(target=download_audio).start,
    fg="blue").place(x=145,y=180)


root.mainloop()
