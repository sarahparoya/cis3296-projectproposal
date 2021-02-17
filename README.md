##### Sarah Paroya
##### CIS 3296: Individual Project Proposal
##### February 27th, 2020
# Discord MusicBot

## Project Abstraction
Discord is a popular messaging platform where you can create servers and channels for people to join and chat in. The concept of the MusicBot allows you to be able to add the bot to your desired server and listen to music together with the other people in your server. The MusicBot would be most likely pulling music from YouTube or another popular streaming service. 

## Project Relevance
This project would involve multiple concepts and learning goals this class introduces to us. Such as, object-oriented design, test driven development, project management, and version control. 
## Conceptual Design
For the completed project, using the bot would be integrated with the actual discord application. To use the bot, it would be added to the server as a bot and used through commands. The commands would be done through the text chat using a special character such as ‘?’. For example, say I wanted to play a certain song I would use the command “!play [song name].” The bot would then stream the song in the voice channel. 
## Background
This discord bot requires the host to have python 3 and discord.py (Discord’s python API) installed before use. The initial planned features/commands include:
- !connect [channel name]: connects bot to the desired voice channel <p>
- !disconnect: disconnects bot from voice channel. <p>
- !play [song name, link, title, keyword, etc.]: plays the audio of the requested YouTube video<p>
  - If wanting to use multiple streaming sites (such as Spotify, SoundCloud, etc.) will need to have specific commands for each streaming site, but for right now I’ll most likely start with YouTube. <p>
- !pause: pauses current song<p>
- !resume: resume the paused song<p>
- !stop: stops playing current song<p>
## Required Resources
- Most likely using Python 3 <p>
-  [Discord's Python API](https://discordpy.readthedocs.io/en/latest/ "Discords Python API") <p>
- This project would require a discord server for testing.
