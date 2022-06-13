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

    
    print("This are the audio qualities:")
    print("NOTE: Some of them are not mp3")
    print("")
    print("kbps   format")
    #Extracting the audio kbps
    for i in range(0,len(audioList)):   
        abr = str(audioList[i]).find("abr") #this is their positions
        kbps = str(audioList[i]).find("kbps") #find the end of the abr 
        mimeType= str(audioList[i]).find("mime_type") #For finding the audio format

        #Extract audio format of the stream list
        audioFormat = str(audioList[i])[mimeType+11:abr-2]

        #In the object it is defined as mp4, but we gonna rewrite it as mp3
        if audioFormat == "audio/mp4":
            audioFormat = "audio/mp3"
        
        #Print kpbs and format of the stream
        print(str(audioList[i])[abr+5:kbps+4],"  ",audioFormat)

    #User choose the quality sound 
    qual = input("Choose a qualitie (only number)\n")
    fileForFiltering = str(my_video.streams.filter(abr=qual+"kbps"))

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

