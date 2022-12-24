#!/usr/bin/env python3
from pytube import YouTube
import os
import re

print("Enter the Video link :")
link = input()
print("Enter the folder")
print(''' 1. Music
2. Educational.
3.tiktok.
4.Documentaries
5.Movies''')

folder = input()

if folder == "1":
    path = '/harry/Videos/Music/'
elif folder == "2":
    path = '/harry/Videos/Educational/'
elif folder == "3":
    path = '/harry/Videos/tiktok/'
elif folder == "4":
    path = '/harry/Videos/Documentaries/'
elif folder == "5":
    path = '/harry/Videos/movies/'


else:
    path = '/harry/Videos/'


SAVE_PATH = path


try:
    mv = YouTube(link)
    name = mv.title
    print(mv.streams.filter(resolution='720').order_by('resolution'))
    mvs = mv.streams.get_highest_resolution()
    # for i in mvs:
    #   if 'res' in i:
    #       print(i)
    # print(mv.streams.filter(file_extension='mp4'))

    print("Getting stream information")

    print("Downloading ->:", name)

    mvs.download(SAVE_PATH)

    print("Download Complete")
except Exception as err:
    print('''Invalid link
    or there is no internet''')
    print(err)
