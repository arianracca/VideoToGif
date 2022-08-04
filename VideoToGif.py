from distutils import extension
from moviepy.editor import VideoFileClip
ext = str(input("Qué formato tiene el video que quieres hacer gif? (ejemplo: mp4, avi...) "))
videoName = str(input("Elije el nombre de tu video de Origen (en la carpeta del programa en ejecucion) "))
videoClip = VideoFileClip(videoName+"."+ext)
videoClip.write_gif(videoName+".gif")