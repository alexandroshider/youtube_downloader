#from pytube import YouTube
import pytube
#os package used for change format in some audio files
from os.path import exists
from os import rename 

#parameter
#url: URL of the video
def audio_download(url):  
    
    #Make a YouTube video object
    my_video = pytube.YouTube(url)
    
    #Filter all streams for getting the audio formats
    audioList = my_video.streams.filter(type="audio")    
    
    #convert in list for easy format and view, and take out data from them
    audioList = list(audioList) 

    #User choose the quality sound 
    fileForFiltering = str(my_video.streams.filter(abr=str(128)+"kbps"))

    #Identify the stream tag
    mime = str(fileForFiltering).find("mime") #this is their positions
    itag = fileForFiltering[16:mime-2]

    #Prepare audio for download
    downlo = my_video.streams.get_by_itag(int(itag))

    #Downloading
    downlo.download()

    #Change format of the file mp3 instead mp4 for some cases
    fileName = my_video.title
    fileName = fileName.replace("/","")
    fileName = fileName.replace("\"","")
    fileName = fileName.replace(".","")
    fileNameMp4 = fileName + ".mp4"
    print(fileName)
    verifyExistenceOfMp4 = exists(fileNameMp4)
    #Verify the existence because I do not want change the format of the webm 
    #It we change the webm to mp3, it will be a trash file
    if verifyExistenceOfMp4:
        rename(fileNameMp4, fileName+".mp3")

