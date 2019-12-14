# Quick Guide

Convert 56 songs to .ogg format at 48kHz sampling rate. Run the python script and select the converted songs in the order you want.

Make sure none of the .ogg files have any images attached to them. This will cause 10+ second load times EVERY TIME the song changes in-game.

Replace the original Bgm.pck with the one created by the script.

# Examples
Example music packs I made using this script can be found at:

https://mega.nz/#F!6HhVSQgL!LOMuvu9xNF5OU9EjNP7Jmw

OR

https://drive.google.com/drive/folders/11t02L8Lfg7jC787Ls1a0pjxe2NsaesBO?usp=sharing

There are also alternate videos where I used ffmpeg to replace the music, as described below.

My music packs were made using music from the Date A Live anime and movie, replacing the tracks as best as I could while retaining the original feel of the music from the visual novel. I only left one track the same, because I couldn't find anything that fit the mood better.

All the packs I made are almost identical, with slight differences.
The main difference is that the ones marked as "With Vocals" have 5 songs with vocals in them, that can play when other characters might be talking. If you don't want to hear any singing in the background while characters might be talking, I made a pack replacing those songs with the instrumental or karaoke versions, when available, otherwise swapping with a different song entirely when not available.
The other difference is that I have high quality (320kbps) and low quality (112kbps) versions available of each. The original Bgm.pck used 112kbps files, so I figured I would provide that quality as well, incase you are short on harddrive space or something.

The original ending videos for each route all used the same song, and I felt like it would be more appropriate if each character had a different song play for their endings. I tried to pick songs that fit them best, but some characters were harder to find a song roughly 2 minutes long that fit their personality. A couple of the videos might look a tiny bit choppy (like Miku's) since I had to add or cut some frames to make the video the same length as the song I picked. Regardless, they turned out way better than the originals in my opinion. The opening video is also way more hype with the song I added.

I think they all turned out pretty good; I would recommend using them if you get tired of the original soundtrack, or, like me, you just want to listen to the awesome music from the anime.

For background music, replace ~\DATE A LIVE Rio Reincarnation\Data\Bgm.pck with the music pack of your choice.

For videos, replace the files in ~\DATE A LIVE Rio Reincarnation\Data\ENG\Movie\ with the files in New Videos (ENG).zip.

# Detailed Instructions

Choose 56 .ogg files (48.0kHz) to replace the original soundtrack 1:1.

Just order your music in the order you want to replace the original tracks and use this script, selecting them all at the same time when prompted.

The order they are selected in will determine which song is replaced.

This script will then output a file named Bgm.pck in the same folder the script is located.

Make sure they're in the right order in the file select "File name:" box before pressing Open. Sometimes it can order them weirdly depending on how you select them. Make sure it's right.

I recommend making a backup of your original Bgm.pck file, but it is relatively easy to restore if you mess something up as it is only about 50MB. You can download it from the above link in the Examples section.

Either run this script in a separate folder from your installation directory, or directly in the Data folder inside your installation path (which will then replace your original Bgm.pck file).

Replace ~installdir\DATE A LIVE Rio Reincarnation\Data\Bgm.pck with the Bgm.pck created from this script.

That's it.


# Extra

If you want to better figure out what exactly will replace what when making your own soundtrack, I recommend you download "Dragon UnPACKer" (https://www.elberethzone.net/dragon-unpacker.html).

You can use that program to rip the audio files from the original Bgm.pck that came with the game. It's what I used to figure a lot of this out.

It can also rip other common file types from other .pck files from not only this game, but others as well.

If you want to swap certain songs and not others, just rip the original audio files as mentioned above and use the ripped tracks you want to keep the same in your selection of 56 songs.

If you are looking for an audio converter, both MediaHuman (https://www.mediahuman.com/audio-converter/) and FreeMake (https://www.freemake.com/free_audio_converter/) are good and free.

I'm more partial to the UI of the MediaHuman audio converter, but both are good.

Unfortunately, replacing the music in Bgm.pck doesn't replace the music for the opening and ending videos. Such a shame :(
I won't be making a script to automate it, but you can easily change the video music yourself with something like ffmpeg (https://www.ffmpeg.org/).

All the videos are stored in ~installdir\DATE A LIVE Rio Reincarnation\Data\ENG\Movie\       — There are also Japanese (JPN) and Chinese (CHN) folders that contain separate movies—and other data—for those versions of the game.

They are .movie files which is essentially the same as a .mov. Just mux the video together with new audio and output as a .mov then rename to .movie

Example:
>`ffmpeg -i video.movie -i newsong.m4a -c copy -map 0:v:0 -map 1:a:0 output.mov`

Then just rename the output.mov to something like 1st_end01.movie and replace the original.

Audio should be AAC(m4a)(48kHz) format for this. No need to rename or convert the original .movie files when muxing. Actually, it won't play in-game if you convert it first, as I found out the hard way.

I made my own videos that can be found at the link above in the Examples section.

To the best of my knowledge, this script will only work with this specific .pck file for this specific game.

I went through the hex code of the original Bgm.pck and figured out what was what and made a script to automate recreating it with any (.ogg) song files.
The script is annotated if you want to see how it works. Easier to read with Notepad++ or any other code editor. Relatively straight-forward. Except for when it isn't.


# Notes
All audio files should have a sampling rate of 48.0kHz. 44.1kHz songs (CD Standard, and probably what your music files are) will sound slightly sped-up and higher pitched. Make sure to convert to 48kHz.

Any images tagged to the audio files will DRASTICALLY increase load times, creating lag and freezes where there would otherwise be none.

I recommend using a tag editor (https://github.com/Martchus/tageditor) or (https://sourceforge.net/projects/kid3/) to get rid of any pictures/metadata that the converted .ogg files may still have. Of course, a program like iTunes, Winamp, or foobar2000 can also do this, albeit less conveniently.

(With tageditor) DO NOT use the Delete button to delete all tags, as this will delete ALL tags and make the file unplayable, the game will then crash when trying to load it.
I found that some programs (like foobar2000) tended to leave stray empty bytes (rows and rows of 00s) behind in the song file when removing metadata or pictures. You may not care.

Removing ALL metadata is not strictly necessary, but removing the picture certainly is, assuming you enjoy not waiting 15 seconds every time the music changes in-game.

Audio volume can always be adjusted in-game if the songs you choose are too loud or quiet. I found myself turning the volume down by about 2 in the menu after using my music pack.

The original Bgm.pck had each song compressed to 112kbps, but there doesn't seem to be any bitrate limit in the game engine. Just has to be an .ogg.

I tested with up to 320kbps .ogg files and it worked fine. Only limit is the .ogg container itself, which caps at "10 quality" which is up to about 467-500kbps, I think.

My music packs are at both 112kbps and 320kbps so you can choose based on storage space or sound quality, whichever is more important to you.

Enjoy.
