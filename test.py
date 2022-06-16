import os 
import re

direc =  "D:\SASS\yt_downloader"

for filename in os.listdir(direc):
    f = str(os.path.join(direc,filename))
    reguala = re.search(r".mp3$", f)
    if reguala:
        print("Hola mundo  ", f)
        os.remove(os.path.join(direc,filename))
    else:
        print("error not found  ", f)
