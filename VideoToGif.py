# QRcodeWebPages.py - Flexible QR code maker.
# To run:
# certifi==2022.6.15
# charset-normalizer==2.1.1
# colorama==0.4.5
# decorator==4.4.2
# idna==3.3
# imageio==2.21.2
# imageio-ffmpeg==0.4.7
# moviepy==1.0.3
# numpy==1.23.2
# Pillow==9.2.0
# proglog==0.1.10
# requests==2.28.1
# tqdm==4.64.0
# urllib3==1.26.12

__version__ = "1.0"

import os
from setuptools import extension
from moviepy.editor import VideoFileClip

if __name__ == '__main__':
    print("""--->> BIENVENIDO A VIDEO TO GIF <<---
Con este programa podrás transformar un video en una imagen Gif animada.
El video del cual generará el GIF debe encontrarse en la carpeta del programa,
así podrá encontrarlo el programa cuando escribas su nombre.
""")
    ext = str(input("""Qué formato tiene el video de origen que
quieres convertir en gif? (ejemplo: mp4, avi...)
"""))
    video_name = str(input("""Elige el nombre de tu video de Origen
(en la carpeta del programa en ejecucion)
"""))
    folder = input("Ingrese la ruta de acceso a la Carpeta para Guardar el Archivo\n")
    video_clip = VideoFileClip(video_name+"."+ext)
    path_like_name = os.path.normpath(folder+"\\"+video_name+".gif")
    video_clip.write_gif(path_like_name)
    print("El archivo "+video_name+".gif fue guardado en la carpeta: "+folder)