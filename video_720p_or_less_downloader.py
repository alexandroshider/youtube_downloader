from pytube import YouTube


def video_download(url,index):
    my_video = YouTube(url)
    if index == 1:
        my_video = my_video.streams.get_by_itag(17)
    
    elif index == 2:
        my_video = my_video.streams.get_by_itag(18)

    elif index == 3:
        my_video = my_video.streams.get_by_itag(22)

    my_video.download()
