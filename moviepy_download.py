from pytube import YouTube
import os
import subprocess
from moviepy.editor import VideoFileClip, AudioFileClip
from sys import argv
import time

link = argv[1]
yt = YouTube(link)

print("Titulo:", yt.title)
print("Views:", yt.views)

video = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
audio = yt.streams.filter(adaptive=True).filter(mime_type='audio/webm').first()

# Obtener la carpeta de descargas del usuario en Windows
downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')

# Descargar el video en la carpeta de descargas del usuario
video_path = os.path.join(downloads_folder, 'video_'+video.default_filename)
video.download(downloads_folder, 'video_'+video.default_filename)

# Descargar el audio en la carpeta de descargas del usuario
audio_path = os.path.join(downloads_folder, 'audio_'+audio.default_filename)
audio.download(downloads_folder, 'audio_'+audio.default_filename)

# Obtener la ruta completa del archivo descargado
downloaded_video_path = os.path.join(downloads_folder, 'video_'+video.default_filename)
downloaded_audio_path = os.path.join(downloads_folder, 'audio_'+audio.default_filename)

# Combinar video y audio
video_clip = VideoFileClip(downloaded_video_path)
audio_clip = AudioFileClip(downloaded_audio_path)

final_clip = video_clip.set_audio(audio_clip)

# Guardar el video con audio combinado
final_clip.write_videofile(os.path.join(downloads_folder, video.default_filename.split('.')[0]+'.mp4'), codec="h264_nvenc", audio_codec="aac")

# Eliminar archivos temporales
os.remove(downloaded_video_path)
os.remove(downloaded_audio_path)

# Abrir la carpeta de descargas después de la descarga
subprocess.Popen(f'explorer /select,"{downloads_folder}"')
