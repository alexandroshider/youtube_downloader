from pytube import YouTube

#URL link of the video (or music you want to download)
url="https://www.youtube.com/watch?v=pW9MJdTnl5E"

#Make a YouTube video
my_video = YouTube(url)

#Filter all streams for getting the audio formats
audioList = my_video.streams.filter(type="audio")
#convert in list for easy format and view, and take out data from them
audioList = list(audioList) 


print("This are the audio qualities:")

#Extracting the audio kbps
for i in range(0,len(audioList)):   
    abr = str(audioList[i]).find("abr") #this is their positions
    kbps = str(audioList[i]).find("kbps") #find the end of the abr 
    print(str(audioList[i])[abr+5:kbps+4])

#User choose the quality sound 
qual = input("Choose a qualitie (only number)\n")
fileForFiltering = str(my_video.streams.filter(abr=qual+"kbps"))

#Identify the stream tag
mime = str(fileForFiltering).find("mime") #this is their positions
itag=fileForFiltering[16:mime-2]

#Prepare audio for download
descarga = my_video.streams.get_by_itag(int(itag))

#Downloading
descarga.download()

    