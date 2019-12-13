import sys
import os
import binascii
from tkinter import *
from tkinter.filedialog import askopenfilename

#global variables

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
