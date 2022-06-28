from pytube import YouTube


def video_download(url):
    #Make a YouTube object
    my_video = YouTube(url)
    #itag 22 is for downloading video in 720p
    my_video = my_video.streams.get_by_itag(22)
    #Right now the video or audio is donwload
    my_video.download()
    fileName = my_video.title
    fileName = fileName.replace("/","")
    fileName = fileName.replace("\"","")
    fileName = fileName.replace(".","")
    fileName = fileName.replace("|","")
    fileName = fileName.replace(":","")
    print(fileName)
