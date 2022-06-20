from pytube import YouTube


def video_download(url):
    my_video = YouTube(url)
    my_video = my_video.streams.get_by_itag(22)
    my_video.download()
    fileName = my_video.title
    fileName = fileName.replace("/","")
    fileName = fileName.replace("\"","")
    fileName = fileName.replace(".","")
    print(fileName)
