#final version converter
#this takes a Youtube .sbv file and turns it into a #tab-delimited .txt file that fave-align can read
def faveconverter ():
	#importing stuff
	#these are just needed for the file choosing
	from tkFileDialog import askopenfilename
	from Tkinter import Tk
	import re
	#this supposedly gets useless windows out of the way
	Tk().withdraw()
	print "Please choose a .sbv file to convert"
	filelocation=askopenfilename()
	print "inputfile: ", filelocation
	inputfile=open(filelocation, "r")
	youtubetranscript=inputfile.read()
	#we set up the regexes to identify individual tier entries: two numbers followed by text
	timestamp="\d\:\d\d\:\d\d\.\d+"
	annotationfinder=re.compile("("+timestamp+"),("+(timestamp)+")\n(.*?)\n\n", re.DOTALL)
	annotations=annotationfinder.findall(youtubetranscript)
	print "number of annotations:", len(annotations)
	outputfile=open(filelocation.replace(".sbv", "_faved.txt"), "a")
	for item in annotations:
		starttime=secondconverter(item[0])
		endtime=secondconverter(item[1])
		transcription=item[2]
		#print starttime, endtime, transcription[:5]
		outputfile.write("default\t\t"+starttime+"\t"
			+endtime+"\t"+transcription.replace("\n", " ")+"\n"
			)
	print "output done"
	print "outputfile:" ,outputfile
	inputfile.close()
	outputfile.close()
