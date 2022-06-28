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
    
    #User used to choose the quality sound
    #Now the audio is downloaded by default in 128kbps
    fileForFiltering = str(my_video.streams.filter(abr=str(128)+"kbps"))
    
    #Update: These are extra steps. Maybe it will be useful 
    #in the future for choose quality in a simplier method
    #Identify the stream tag
    mime = str(fileForFiltering).find("mime") #this is their positions
    itag = fileForFiltering[16:mime-2]

    #Prepare audio for download
    downlo = my_video.streams.get_by_itag(int(itag))

    #Downloading
    downlo.download()
    """
    Change format of the file mp3 instead mp4 for some cases
    Warning: Maybe format won't change if the title of the 
    video in YT have special characters. But file will still be 
    only audio file
    """
    fileName = my_video.title
    #These replace section is because windows do not accept certain
    #characters in the name of the files 
    fileName = fileName.replace("/","")
    fileName = fileName.replace("\"","")
    fileName = fileName.replace(".","")
    fileName = fileName.replace("|","")
    fileName = fileName.replace(":","")

    fileNameMp4 = fileName + ".mp4"
    print(fileName)
    verifyExistenceOfMp4 = exists(fileNameMp4)
    #Verify the existence because I do not want change the format of the webm 
    #It we change the webm to mp3, it will be a trash file
    if verifyExistenceOfMp4:
        rename(fileNameMp4, fileName+".mp3")

