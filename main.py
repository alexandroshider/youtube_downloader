#Modules for download video and audio
from video_720p_or_less_downloader import video_download as vd720OrL   
from audio_downloader import audio_download as ad
     

if __name__ == "__main__":

    #Input for what format user want to download
    formatDownload=int(input("Do you want download \"video\"(1) or \"audio\"(2)? (Write ONLY THE NUMBER)\n"))
    #Open file links.txt, tead all lines
    file_links = open("links.txt","r")
    Lines = file_links.readlines()  
    #loop for download video in each line.       
    for line in Lines:
    #User chose only audio
        if formatDownload == 2:
            ad(str(line))
    #User chose video
        if formatDownload == 1:
            vd720OrL(str(line))    