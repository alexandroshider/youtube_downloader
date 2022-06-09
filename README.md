I AM STILL WORKING IN THIS PROJECT. ANY IDEA OR SUGGESTION IS WELCOME.

With this repository you can download videos from You Tube. 
You can also download only the audio of the You Tube video if you want. 

Packages you need:
pytube 12.1.0
os

Notes: In pytube 12.1.0 you need to modify cipher.py on the line 30 delete it and put
        var_regex = re.compile(r"^\$*\w+\W")

Main branch: You can download a single audio or video using the url from YT
