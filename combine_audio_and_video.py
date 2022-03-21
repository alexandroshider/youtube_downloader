from moviepy import editor

def combine_audio_video_HD(audioTitle, videoTitle):

    videoClip = editor.VideoFileClip(videoTitle)
    audioClip = editor.AudioFileClip(audioTitle+".mp3")

    finalClip = videoClip.set_audio(audioClip)
    finalClip.write_videofile(audioTitle+".mp4", fps=50)