#-----INSTRUCTIONS-----
#
#Choose 56 .ogg files (48.0kHz) to replace the original soundtrack 1:1.
#
#Just order your music in the order you want to replace the original tracks and use this script, selecting them all at the same time when prompted.
#The order they are selected in will determine which song is replaced.
#This script will then output a file named Bgm.pck in the same folder the script is located.
#
#Make sure they're in the right order in the file select "File name:" box before pressing Open. Sometimes it can order them weirdly depending on how you select them. Make sure it's right.
#
#I recommend making a backup of your original Bgm.pck file, but it is relatively easy to restore via integrity check if you mess something up as it is only about 50MB. I will also include a link to the original Bgm.pck along with some example music packs.
#
#Either run this script in a separate folder from your installation directory, or directly in the Data folder inside your installation path (which will then replace your original Bgm.pck file).
#
#Replace ~installdir~\DATE A LIVE Rio Reincarnation\Data\Bgm.pck with the Bgm.pck created from this script. That's it.
#
#Enjoy.
#
#
#-----EXTRA-----
#
#If you want to better figure out what exactly will replace what when making your own soundtrack, I recommend you download "Dragon UnPACKer" (https://www.elberethzone.net/dragon-unpacker.html).
#You can use that program to rip the audio files from the original Bgm.pck that came with the game. It's what I used to figure a lot of this out.
#It can also rip other common file types from other .pck files from not only this game, but others as well. ;)
#
#If you want to swap certain songs and not others, just rip the original audio files as mentioned above and use the ripped tracks you want to keep the same in your selection of 56 songs.
#
#If you are looking for an audio converter, both MediaHuman (https://www.mediahuman.com/audio-converter/) and FreeMake (https://www.freemake.com/free_audio_converter/) are good and free.
#I'm more partial to the UI of the MediaHuman audio converter, but both are good.
#
#Unfortunately, replacing the music in Bgm.pck doesn't seem to replace the music for the opening and ending videos. Such a shame :(
#I won't be making a script to automate it, but you can easily change the video music yourself with something like ffmpeg (https://www.ffmpeg.org/).
#
#All the videos are stored in ~installdir~\DATE A LIVE Rio Reincarnation\Data\ENG\Movie       — There are also Japanese (JPN) and Chinese (CHN) folders that contain separate movies—and other data—for those versions of the game.
#They are .movie files which is essentially the same as a .mov. Just mux the video together with new audio and output as a .mov then rename to .movie
#Example: "ffmpeg -i video.movie -i newsong.m4a -c copy -map 0:v:0 -map 1:a:0 output.mov" then rename the output.mov to something like 1st_end01.movie and replace the original.
#
#Audio should be AAC(m4a)(48kHz) format for these, since .mov are Apple video files. No need to rename or convert the original .movie files.
#There should be a link to a zip file containing the vids with better music in my guide...
#
#To the best of my knowledge, this script will only work with this specific .pck file for this specific game.
#I went through the hex code of the original Bgm.pck and figured out what was what and made a script to automate recreating it with any (.ogg) song files.
#This script is annotated if you want to see how it works. Easier to read with Notepad++ or any other code editor. Relatively straight-forward. Except for when it isn't.
#
#
#-----NOTES-----
#All audio files should have a sampling rate of 48.0kHz. 44.1kHz songs (CD Standard, and probably what your music files are) will sound slightly sped-up and higher pitched. Make sure to convert to 48kHz.
#
#Any images tagged to the audio files will DRASTICALLY increase load times, creating lag and freezes where there would otherwise be none.
#I recommend using a tag editor (https://github.com/Martchus/tageditor) or (https://sourceforge.net/projects/kid3/) to get rid of any pictures/metadata that the converted .ogg files may still have. Of course, a program like iTunes can also do this, albeit less conveniently.
#(With tageditor) DO NOT use the Delete button to delete all tags, as this will make the file unplayable and the game will crash when trying to load it.
#I found that some programs (like foobar2000) tended to leave stray empty bytes (rows and rows of 0s) behind in the song file when removing metadata and pictures. You may not care.
#Removing ALL metadata is not strictly necessary, but removing the picture certainly is, assuming you enjoy not waiting 15 seconds every time the song changes in-game.
#
#Audio volume can always be adjusted in-game if the songs you choose are too loud or quiet. I found myself turning the volume down by about 2 in the menu after using my music pack with music from the anime.
#
#The original Bgm.pck had each song compressed to 112kbps, but there doesn't seem to be any bitrate limit in the game engine. Just has to be an .ogg.
#I tested with up to 320kbps .ogg files and it worked fine. Only limit is the .ogg container itself, which caps at "10 quality" which is up to about 467-500kbps, I think.
#My music packs are at both 112kbps and 320kbps so you can choose based on storage space or sound quality, whichever is more important to you.
#
#
#I think the pack I made using anime music turned out great; I would recommend using it if you get tired of the original soundtrack, or, like me, you just want to listen to the awesome music from the anime.
#
#
#vvvvvvvvvv -----CODE----- vvvvvvvvvv

import sys
import os
import binascii
from tkinter import *
from tkinter.filedialog import askopenfilename

#globals variables

#Most of this assigns names to each song for the game engine to see. Some of this is still a mystery to me. I just know it's important.
beginningstuff = """46696C656E616D6520202020202020202020202028030000E0000000EA000000\
F4000000FE00000008010000120100001C01000026010000300100003A010000\
440100004E01000058010000620100006C01000076010000800100008A010000\
940100009E010000A8010000B2010000BC010000C6010000D0010000DA010000\
E4010000EE010000F8010000020200000C02000016020000200200002A020000\
340200003E02000048020000520200005C02000066020000700200007A020000\
840200008E02000098020000A2020000AC020000B6020000C0020000CA020000\
D4020000DE020000E8020000F2020000FC0200000603000062676D30312E736E\
640062676D30322E736E640062676D30332E736E640062676D30342E736E6400\
62676D30352E736E640062676D30362E736E640062676D30372E736E64006267\
6D30382E736E640062676D30392E736E640062676D31302E736E640062676D31\
312E736E640062676D31332E736E640062676D31342E736E640062676D31352E\
736E640062676D31362E736E640062676D31372E736E640062676D31382E736E\
640062676D32322E736E640062676D32332E736E640062676D32342E736E6400\
62676D32352E736E640062676D32362E736E640062676D32382E736E64006267\
6D33342E736E640062676D33352E736E640062676D33362E736E640062676D33\
372E736E640062676D33382E736E640062676D33392E736E640062676D34302E\
736E640062676D34312E736E640062676D34322E736E640062676D34332E736E\
640062676D34342E736E640062676D34352E736E640062676D34362E736E6400\
62676D34372E736E640062676D34382E736E640062676D34392E736E64006267\
6D35302E736E640062676D35312E736E640062676D35322E736E640062676D35\
332E736E640062676D35342E736E640062676D35352E736E640062676D35362E\
736E640062676D35372E736E640062676D35382E736E640062676D35392E736E\
640062676D36302E736E640062676D36312E736E640062676D36322E736E6400\
62676D36332E736E640062676D36342E736E640062676D36352E736E64006267\
6D36362E736E64005061636B20202020202020202020202020202020DC010000\
38000000"""


filePaths = []
songLengths = []
startingPositions = []
startingPositions.append(1288) #first location
songbuffers = []
endPosition = None


def printall(input): #was used for testing
	for a in input:
		print(a)
	
def reversehex(input): #input is a block of 8(4) hex bytes (string) and output is those bytes "reversed" (string)
	if len(input) != 8:
		return None
	n = 2
	hexblock = [input[i:i+n] for i in range(0, len(input), n)]
	reversal = hexblock[3] + hexblock[2] + hexblock[1] + hexblock[0]
	return reversal
	
def dectohex(input): #input is an array of decimal values, input is converted to string of hex values with length 8(4) with leading zeroes. This is technically considered bad programming because it modifies the input rather than returning altered values, but meh
	for i in range(len(input)):
		ch = format(input[i], 'x')
		input[i] = ((8-len(ch))*"0") + ch


#get songs with file menu
root = Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
files = askopenfilename(multiple=True,title="Select 56 Songs") 
var = root.splitlist(files)
for f in var:
    filePaths.append(f)
filePaths


#output test
# print("Files selected:")
# printall(filePaths)

	
#make sure 56 files were selected
if len(filePaths) != 56:
	input("Must select 56 songs. Quitting...")
	sys.exit(-1)


#check to see if all files are .ogg files and get length at the same time
for file in filePaths:
	f = open(file, "rb")
	ch = binascii.hexlify(f.read(4))
	ch = str(ch, 'utf-8')
	if ch != "4f676753": #this will always be the first 4 hex bytes of any .ogg music file.
		input("Only .ogg files will work. Quitting...")
		sys.exit(-1)
	songLengths.append(os.stat(file).st_size)
	f.close()


	
#output test
# print("Song lengths in decimal:")
# printall(songLengths)

	
#calculate starting positions in the resulting file and buffers
for i in range(len(songLengths)):
	endPosition = startingPositions[i] + songLengths[i] - 1
	buffer = endPosition - 8
	buffer = 16 - (buffer % 16)
	songbuffers.append(buffer)
	newstart = endPosition + buffer
	startingPositions.append(newstart)


#test
# print("Song starting positions in decimal:")
# printall(startingPositions)
# print("All buffers:")
# printall(songbuffers)


#convert decimal values to hex values
dectohex(songLengths)
dectohex(startingPositions)

#test
# print("Song lengths (in hex):")
# printall(songLengths)
# print("Song starting positions (in hex):")
# printall(startingPositions)


#reverse all song lengths and starting positions
#for some reason, all the lengths and positions were reversed inside the original .pck file, so I had to recreate that anomaly (e.g. 12 34 56 78 was 78 56 34 12)
for i in range(len(songLengths)):
	songLengths[i] = reversehex(songLengths[i])
	startingPositions[i] = reversehex(startingPositions[i])


#test
# print("Song lengths (reversed, in hex):")
# printall(songLengths)
# print("Song starting positions (reversed, in hex):")
# printall(startingPositions)


#check if Bgm.pck exists and open or create it	
try:
	f = open("Bgm.pck", "xb")
except IOError:
	f.close()
	while True:
		a = input("The output file (Bgm.pck) already exists, would you like to overwrite it? (y/n)")
		if a == "n":
			input("Exiting...")
			sys.exit()
		if a == "y":
			break
	f = open("Bgm.pck", "w+b")
	
#begin file write
#print("Beginning file write...")
f.write(binascii.unhexlify(beginningstuff))


#write song starting positions and lengths
for i in range(len(songLengths)):
	f.write(binascii.unhexlify(str(startingPositions[i])))
	f.write(binascii.unhexlify(str(songLengths[i])))

#buffer before start of songs
f.write(b'\x00' * 4)

#append songs and buffers to file
print("Writing songs to file...")
for i in range(len(filePaths)):
	song = open(filePaths[i], "rb")
	f.write(song.read())
	song.close()
	f.write(b'\x00' * (songbuffers[i]-1))
	
	
#final buffer
lastbuffer = 16 - (f.tell() % 16)
f.write(b'\x00' * lastbuffer)

f.close()

input("All done! Press the Any Key to exit...")
sys.exit(1)