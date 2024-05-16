import eel
import os
import subprocess
import json
from pytube import YouTube

eel.init('web')


def convertToJSON(dict):
    return json.dumps(dict)

def getDescription(yt):
    for n in range(6):
        try:
            description =  yt.initial_data["engagementPanels"][n]["engagementPanelSectionListRenderer"]["content"]["structuredDescriptionContentRenderer"]["items"][1]["expandableVideoDescriptionBodyRenderer"]["attributedDescriptionBodyText"]["content"]            
            return description
        except:
            continue
    return False

def getResolutions(yt):
    resolutions = set()
    for stream in yt.streams:
        resolutions.add(stream.resolution)
    resolutions = [int(x.rstrip('p')) for x in resolutions if x is not None]
    resolutions.sort()
    print(resolutions)
    return resolutions

@eel.expose
def downloadYTVideo(url, res):
    print('Descargando video:', url, res)
    yt = YouTube(url)
    yd = yt.streams.filter(res=res).first()
    downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    yd.download(downloads_folder)

    downloaded_video_path = os.path.join(downloads_folder, yd.default_filename)

    # Abrir la carpeta de descargas después de la descarga
    subprocess.Popen(f'explorer /select,"{downloaded_video_path}"')

@eel.expose
def getVidInfo(url):
    yt = YouTube(url)
    vidInfo = {'title': yt.title, 'views': yt.views, 'author': yt.author, 'desc': getDescription(yt), 'thumbnailURL': yt.thumbnail_url, 'resolutions': getResolutions(yt)}
    return convertToJSON(vidInfo)


eel.start('index.html', size=(800,600), mode='default', host='0.0.0.0')