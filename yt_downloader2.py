from pytube import *
import os
os.system('cls')

link = input("Enter the youtube video link : ")
quality = input("Enter quality of the video (360p, 480p, 720p, 1080p): ")
yt = YouTube(link)

print("Downloading .....")

try:
    video_download = yt.streams.filter(resolution = quality , file_extension = "mp4")
    video_download.first().download()
except:
    print("Some Error!")
print('Task Completed!')






#suggested_Url = https://www.youtube.com/watch?v=d1YBv2mWll0