#Modules 
from video_720p_or_less_downloader import video_download as vd720OrL   
from audio_downloader import audio_download as ad
 #We need another algorithm for higher resolutions than 720p
from video_download_superior import highResolutionVideo as hRV     

if __name__ == "__main__":

    url = "https://www.youtube.com/watch?v=lZ5gIk98Dfs"   #Digimon Tamers op

    #Input for what the user want to download
    formatDownload=int(input("Do you want download \"video\"(1) or \"audio\"(2)? (Write ONLY THE NUMBER)\n"))

    #User chose download only audio
    if formatDownload == 2:
        file_links = open("links.txt","r")
        Lines = file_links.readlines()
        arrayWithURLs=[]
        for line in Lines:
            #line=str(line)
            ad(str(line),str(128))

    #User chose video 
    if formatDownload == 1:
        print("Choose the quality you want? (Write ONLY the index)\n")
        print("WARNING: QUALITY ABOVE 720p DOWNLOAD TIME IS CONSIDERABLY LONGER")
        print("1. 144p")
        print("2. 360p")
        print("3. 720p")
        print("4. Better than 720p")
        quality = int(input("Write ONLY the index:\n"))

        #144, 360 and 720 use the same method
        if quality == 1 or quality ==2 or quality == 3:
            vd720OrL(url, quality)
        
        #High quality requires download video, then download audio
        if quality == 4:
            hRV(url)
    