from moviepy.editor import *
import os
from config import setting

setting = setting()
print("What is your file name including extension in the 'in' folder?")
name = input()
name = name.strip()
masterclip = VideoFileClip("./in/{0}".format(name))
clipName= masterclip.filename
clipNames = clipName.split("/")
clipName = clipNames[-1]
path = os.path.join("./out/",clipName)
try:
    os.makedirs(path)
except:
    print("folder already exists")
clipDuration = masterclip.duration
clipStart = 0
clipend = setting.clipLength
clipNum = 0

while clipend < clipDuration:
    clip = masterclip.subclip(clipStart,clipend)
    clip.write_videofile("./out/{0}/{1}.mp4".format(clipName,clipNum))

    clipNum = clipNum +1
    clipStart = clipStart + setting.clipLength
    clipend = clipend + setting.clipLength

clip = masterclip.subclip(clipStart)
clip.write_videofile("./out/{0}/{1}.mp4".format(clipName,clipNum))


clip.write_videofile("./out/1.mp4")