import eel
import os
from pytube import YouTube

eel.init("web")

@eel.expose
def Saludar():
    return "Hola desde main.py"

@eel.expose
def download_yt_video(url):
    yt = YouTube(url)
    yd = yt.streams.get_highest_resolution()
    downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    yd.download(downloads_folder)

eel.start("index.html", size=(1000,800))