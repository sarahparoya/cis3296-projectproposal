##### Sarah Paroya

# **JukeBot**: _Discord Music Bot_
## Project Abstraction
Discord is a popular messaging platform where you can create servers 
and channels for people to join and chat in. The concept of JukeBot 
allows you to be able to add the bot to your desired server and listen 
to music together with the other people in your server. The music bot would
be most likely pulling music from YouTube, since YouTube provides an API we
would be able to work with. <p>
![projectproposal](https://user-images.githubusercontent.com/63789040/108932874-12b3d480-7618-11eb-9967-62d552e925ad.png)

## Project Relevance
This project would involve multiple concepts and learning goals 
this class introduces to us. We would be using object-oriented programming
with Python as our language. Also, testing and debugging are going to big parts
of this project, since there are many different features/commands that we would 
have to make sure are working. In addition, project management and version control
come into play as well since there are different features to work on. Also, I do 
have a set of commands to start off with, but there is definitely many ways we can 
expand this project, and we would need to make sure we're keeping track of all the 
different functionalities. 

## Conceptual Design
For the completed project, using the bot would be integrated with
the actual discord application. To use the bot, it would be added to 
the server as a bot and used through commands. The commands would be 
done through the text chat using a special character such as ‘!’. For 
example, say I wanted to play a certain song I would use the command
“!play [song name].” The bot would then stream the song in the voice
channel. To be able to listen to the song you would also have to be 
connected to the voice channel. 
## Background
This repository contains a very basic helloworld.py file, 
which connects the bot to the testing server and responds to all 
inputs starting with the character `!` with "Hello World".  
This discord bot requires the host to have Python 3 and discord.py 
(Discord’s python API) installed before use. The initial planned features/commands include:
- `!connect [channel name]:` connects bot to the desired voice channel <p>
- `!disconnect:` disconnects bot from voice channel. <p>
- `!play [song name, link, title, keyword, etc.]:` plays the audio of the requested YouTube video<p>
  - If wanting to use multiple streaming sites (such as Spotify, SoundCloud, etc.) will need to have specific commands for each streaming site, but for right now I’ll most likely start with YouTube. <p>
- `!pause:` pauses current song<p>
- `!resume`: resume the paused song<p>
- `!stop:` stops playing current song<p>
## Required Resources
-  Python 3
- Discord Account
-  [Discord's Python API](https://discordpy.readthedocs.io/en/latest/ "Discords Python API")
- [YouTube Data API](https://developers.google.com/youtube/v3/docs/search/list)
- [Discord Testing Server](https://discord.gg/nfv7TS5A) <p> <p>
![jukebot1](https://user-images.githubusercontent.com/63789040/108933445-2a3f8d00-7619-11eb-9ed5-8582f5bf3646.png)
![jukebot2](https://user-images.githubusercontent.com/63789040/108933453-2ca1e700-7619-11eb-8d27-8c4790ef8919.png)
