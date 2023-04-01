from pytube import YouTube
from tkinter import filedialog
from tkinter import *
import re
from tkinter import ttk


def validateUrl(url):
    urlYtRegEx = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$"
    if(re.match(urlYtRegEx, url)):
        return True
    return False

def handleVideo(videourl, window, text, elements):
    if(not validateUrl(videourl)):
        text["text"] = "Url invalida"
        text.grid(column=0, row=6)
        return
    else:
        text.grid_forget()

    #wait destination
    destination = selectPath()
    if(destination == ""):
        return
    
    #setting values for progress bar
    elements[0]["value"] = 0
    elements[0]["maximum"] = 100
    
    #setting callback for progress bar
    def on_progress(chunk, file_handle, bytes_remaining):
        elements[0]["value"] = int(percent(videos.filesize - bytes_remaining, videos.filesize))
        window.update_idletasks()    
    
    try:
        yt = YouTube(videourl, on_progress_callback=on_progress)
        videos = yt.streams.get_highest_resolution()
    except:
        text["text"] = "Error, este video es privado o no existe"
        text.grid(column=0, row=6)
        return

    #show progress bar
    for index, element in enumerate(elements):
        element.grid(column=0, row=int(index)+4)

    startDownload(videos, destination)

    #hide progress bar
    for element in elements:
        element.grid_forget()

    #wait download
    text["text"] = "Descarga finalizada"
    text.grid(column=0, row=6)


def startDownload(videos, destination):
    videos.download(destination)


def selectPath():
    return filedialog.askdirectory()


def percent(bytes_downloaded, filesize):
    perc = (float(bytes_downloaded) / float(filesize)) * float(100)
    return perc


def __init__():
    #main window
    window = Tk()
    window.title("Descargador de videos")
    window.geometry("300x200")
    label = Label(window, text="Descargador de videos", font=("Arial Bold", 20))
    label.grid(column=0, row=0)
    txt = Entry(window, width=40)
    txt.grid(column=0, row=1)

    #invalid url
    text = Label(window, text="Url invalida")

    #downloading bar
    progressDw = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    labelDw = Label(window, text="Descargando...")
    btnDw = Button(window, text="Cancelar", command=window.destroy)
    
    #dowload button
    btn = Button(window, text="Descargar", command=lambda: handleVideo(txt.get(), window, text, [progressDw,labelDw,btnDw]))
    btn.grid(column=0, row=2)

    #ejecutar ventana
    window.mainloop()


if __name__ == "__main__":
    __init__()