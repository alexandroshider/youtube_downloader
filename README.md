THIS PROJECT IS STAND BY. BUT YOU CAN DM ME VIA TWITTER IF YOU WANT
TO COMUNICATE WITH ME. 

With this repository you can download videos from You Tube. 
You can also download only the audio of the You Tube video if you want. 

##How to use it?
You need to have main.py, audio_downloader.py, and video_720p_or_less_downloader.py 
in the same directory. Then you have a file called links.txt in the same directory,
where you put each URL from YouTube that you wanna donwload. Finally, you execute 
main.py, in the CLI you write "1" or "2" depending of what format you want to download

That's it. Your downloads are in the same directory than in the repository.

NOTE: If you have already downloaded the videos and then you want to download the audios
program will replace all the videos in the links.txt by the audios. 

Packages you need:
pytube 12.1.0
os

Notes: In pytube 12.1.0 you need to modify cipher.py on the line 30 delete it and put
        var_regex = re.compile(r"^\$*\w+\W")

Main branch: You can download a single audio or video using the url from YT

