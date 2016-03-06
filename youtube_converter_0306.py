
import tkFileDialog; from Tkinter import Tk; import re; import os


#secondconverter
#this turns the minute-hour notation of the Youtube file into 
#something fave-align can deal with. We need this for faveconverter to work
def secondconverter (timestamp):
    #groups: hours, minutes, seconds, miliseconds
    splitter=re.compile('(\d+)\:(\d\d)\:(\d\d)\,(\d+)')
    result=splitter.findall(timestamp)
    #we do the math
    seconds=int(result[0][0])*3600+int(result[0][1])*60+int(result[0][2])
    return (str(seconds)+"."+result[0][3])


#final version converter
#this takes a Youtube .sbv file and turns it into a 
#tab-delimited .txt file that fave-align can read
def faveconverter (speaker, filetype="srt"):
    #this supposedly gets useless windows out of the way
    Tk().withdraw()
    print "Please supply a folder containing your files"
    #filelocation=askopenfilename()
    directory=tkFileDialog.askdirectory()
    print directory
    files=[i for i in os.listdir(directory) if not i.startswith(".")]
    #print "inputfiles: ", filelocation
    print "files to be processed\n", ",".join(files)
    os.chdir(directory)
    for fili in files:
        inputfile=open(os.path.join(directory, fili), "r")
        youtubetranscript=inputfile.read()
        #we set up the regexes to identify individual tier entries: two numbers
        #followed by text
        #youtube has a ".:, downsub a ","
        timestamp="\d\d\:\d\d\:\d\d\,\d+"
        annotationfinder=re.compile("("+timestamp+") --> ("+(timestamp)+")\n(.*?)\n\d", re.DOTALL)
        annotations=annotationfinder.findall(youtubetranscript)
        print "number of annotations:", len(annotations)
        #outputfile=open(fili.replace("."+filetype, "_faved2.txt"), "a")
        outputfile=open(fili+"_faved.txt", "a")
        #this should be a func
        for item in annotations:
          starttime=secondconverter(item[0])
          endtime=secondconverter(item[1])
          transcription=item[2]
          #print starttime, endtime, transcription[:5]
          outputfile.write(speaker+"\t\t"+starttime+"\t"
              +endtime+"\t"+transcription.replace("\n", " ")+"\n"
              )
        print "output done"
        print "outputfile:" ,outputfile
        inputfile.close()
        outputfile.close()


faveconverter("donald")

###https://developers.google.com/youtube/v3/docs/captions
##this is what downsub gives us 
##1
##00:00:00,000 --> 00:00:09,640
##mr. Donald J truck
##
##2
##00:00:09,640 --> 00:00:15,120
##thank you everybody thank you


#converting audio in python
#http://stackoverflow.com/questions/1246131/python-library-for-converting-files-to-mp3-and-setting-their-quality


