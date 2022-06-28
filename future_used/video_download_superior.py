from pytube import YouTube
#We need to download the audio using the audio_downloader module
from audio_downloader import audio_download as aD
from obsolet.combine_audio_and_video import combine_audio_video_HD as cAV
#os is used change the names of the files and using a auxiliar name 
#then avoid that our video file be replaced with the audio file 
#that it is downloaded with mp4 format and then changed
from os import rename, remove

def highResolutionVideo(url):

    #youtube object 
    my_video = YouTube(url)

    #in a list save the streaming video
    videoList = my_video.streams.filter(type="video")
    videoList = list(videoList)

    print("Avaible resolutions:")
    indexResolution=1
    #List for saving the best resolutions by their itag
    theBestResolutionList=[]
    for i in range(0,len(videoList)):   
        res = str(videoList[i]).find("res") #this is their positions
        fps = str(videoList[i]).find("fps") #find the end of the abr 
        mime = str(videoList[i]).find("mime") #find the end of the abr 
        #Each stream object  has a "M", the stream with quality higher than 720p has this M in the 83th positon
        #This is how to identify that streamings
        mIdentifier   = (str(videoList[i]).find("M"))
        if mIdentifier == 83:        
            #Print the idexes for the user
            print(f"{indexResolution}. {str(videoList[i])[res+5:fps-2]}")
            indexResolution += 1
            #and save them in a list for later use, these are the itags of those streams
            theBestResolutionList.append(str(videoList[i])[mime-5:mime-2])
    
    #This conditional is for the cases where the video do not posses a quality better than 720p
    if theBestResolutionList == []:
        print("Video cannot be downloaded in higher quality than 720p")
        return

    #input time for resolution
    quality = int(input("Write the index of the quality you want:\n"))

    #from  the quality input, we choose the streaming by itag
    descarga = my_video.streams.get_by_itag(int(theBestResolutionList[quality-1]))

    #Download the streaming
    descarga.download()
    
    #change the name of the video file
    #this is for a problem with the audio file that it is downloaded as a mp4
    #so the audio file replaces the video file
    #auxiliar.mp4 protects the video file
    fileName = my_video.title
    #replacing characters that conflict with python
    fileName = fileName.replace("/","")
    fileName = fileName.replace("\"","")
    
    rename(fileName+".mp4", "auxiliar.mp4")
    print("")
    print("CHOOSE QUALITY WHOSE FORMAT IS AUDIO/MP3")
    #Function for now downloading the audio
    aD(url)
    #Function for merging the audio and video
    cAV(fileName,"auxiliar.mp4")
    #Remove files we do not ask for (muted video, only audio)
    remove("auxiliar.mp4")
    remove(fileName+".mp3")


