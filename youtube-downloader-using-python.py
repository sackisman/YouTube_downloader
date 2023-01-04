from tkinter import *
from tkinter import filedialog
from pytube import YouTube





def getFolder():
    global folderDir
    filename=filedialog.askdirectory()
    folderDir.set(filename)
    print(filename)



def popupmsg(msg):
    popup=Tk()
    popup.title("Download status")
    Label(popup,text=msg).pack()
    Button(popup,text="Okay",command=popup.destroy).pack()
    popup.mainloop()

def downloadVideo():
     yt=YouTube(url.get())
     ss=yt.streams.get_highest_resolution().download(folderDir.get())
    #ydl_opts = {
    #'outtmpl': folderDir.get()+'/%(title)s.%(ext)s'
    #}
    #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     #   ss=ydl.download([url.get()])
    popupmsg("Your video downloaded to this folder : " +str(ss))

    #root or master widget

root=Tk()
root.title("OsakiDownloader")

folderDir=StringVar()

Label(root,text="Enter Youtube video url here: ").grid(row=0,column=0)

url=Entry(root)
url.grid(row=0,column=3)

Label(root,text="Save to :").grid(row=1)
Label(root,textvariable=folderDir).grid(row=1,column=2)
Button(root,text="Browse",command=getFolder,bg="blue").grid(row=1,column=3)
Button(root,text="Download",command=downloadVideo).grid(row=2,column=3)


mainloop()
