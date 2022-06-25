#### (THIS PROJECT IS ON STAND BY. BUT YOU CAN DM ME VIA TWITTER IF YOU WANT TO COMMUNICATE WITH ME)

# YouTube Downloader

A repository to download videos and/or audio files from YouTube. 

## Getting Started

### Dependencies
* pytube 12.1.0
* os
### Installing
* Git clone repository
* requirements.txt
### Executing Program
You need to have main.py, audio_downloader.py, and video_720p_or_less_downloader.py 
in the same directory. Then you have a file called links.txt in the same directory,
where you put each URL from YouTube that you want to download. Finally, you execute 
main.py; in the CLI you write "1" or "2" depending on what format you want to download.

That's it. Your downloads are in the same directory than in the repository.

### NOTE
* If you have already downloaded the videos and then you want to download the audios, then the
program will replace all the videos in the links.txt with the audios. 

* In pytube 12.1.0 you need to modify cipher.py on the line 30 delete it and put
        var_regex = re.compile(r"^\$*\w+\W")
        
## Author
Alexandro Shider
