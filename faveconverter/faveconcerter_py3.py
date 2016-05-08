import sys
import re
import os
import codecs
import tkinter.filedialog
from tkinter import Tk  

        

def main (speaker_name, file_type="srt", file_encoding = "utf-8", speaker_id="default"):
    """
    Converting various subtitle formats into a tab-delimited .txt file for vowel alignment.
    
    This script converts SubRip, Subviewer or VTT files to the formatting required by the Forced Vowel Alignment and Extraction (FAVE*) algorithm.
    
    Arguments:
    speaker_name -- the name of the main tier; this will be used for labeling by FAVE
    file_type -- the formatting of the input file. Default ist .srt (SubRip Text), but also accepts Subviewer (.sub or .sbv) and WebVTT (.vtt). 
    file_encoding -- character encoding of the input file. Default is utf-8 but will accept anything Python can deal with. 
    speaker_id -- the speaker ID is an optional line to identify the speaker but will not be used by FAVE.  
    
    *Rosenfelder, Ingrid; Fruehwald, Joe; Evanini, Keelan and Jiahong Yuan. 2011. FAVE (Forced Alignment and Vowel Extraction) Program Suite. http://fave.ling.upenn.edu.
    
    """ 
    inputchecker(file_type, file_encoding)
    Tk().withdraw()
    print("Please supply a folder containing your files")
    directory=tkinter.filedialog.askdirectory()
    print("We are working with the files in {}\n".format(directory))
    files=[i for i in os.listdir(directory) if not i.startswith(".")]
    print("Files to be processed\n", ",".join(files), "\n---\n")
    for fili in files:
        print(fili,": ", end=' ')
        inputfile=codecs.open(os.path.join(directory, fili), "r", file_encoding)
        transcript=inputfile.read()
        annotationfinder=re.compile("("+formatdict[file_type]['timestamp']+")"+formatdict[file_type]['separator']+"("+formatdict[file_type]['timestamp']+")"+formatdict[file_type]['text'], re.DOTALL)
        annotations=annotationfinder.findall(transcript)
        print("number of annotations:", len(annotations), end=' ')
        if len(annotations) < 1:
            print("\nWarning: No annotations found in file \'{}\'.\nMake sure you are using a well-formatted \'{}\' file. For a different file format, change the \'file_type\' setting.\n".format(fili, file_type)) 
        else:
            outputfile=open(os.path.join(directory, fili+"_faved.txt"), "a")
            for anno in annotations:
                starttime=secondconverter(anno[0], formatdict[file_type]['timesplit'])
                endtime=secondconverter(anno[1], formatdict[file_type]['timesplit'])
                transcription=re.sub("<.*?>", "", anno[2])
                outputfile.write(speaker_id+"\t"+speaker_name+"\t"+starttime+"\t"
                   +endtime+"\t"+transcription.replace("\n", " ")+"\n")
            print("; output file: ",os.path.join(directory, fili+"_faved.txt"), "\n")
            inputfile.close()
            outputfile.close()

# Helper functions

formatdict={
        "srt": {"timestamp":"\d\d\:\d\d\:\d\d\,\d+", "separator":" --> ", "text":r"\n(.*?)\n", "timesplit":"(\d\d)\:(\d\d)\:(\d\d)\,(\d+)"},
        "vtt": {"timestamp":"\d+:\d\d:\d\d\.\d{3}", "separator":" --> ", "text":r".*?\d%\n(.*?)\n\n", "timesplit":"(\d+)\:(\d\d)\:(\d\d)\.(\d{3})"},
         "sbv": {"timestamp":"\d+:\d\d:\d\d\.\d{3}", "separator":",", "text":r"\n(.*?)\n\n", "timesplit":"(\d+)\:(\d\d)\:(\d\d)\.(\d{3})"},
         "sub": {"timestamp":"\d+:\d\d:\d\d\.\d{3}", "separator":",", "text":r"\n(.*?)\n\n", "timesplit":"(\d+)\:(\d\d)\:(\d\d)\.(\d{3})"}
         }

def secondconverter (timestamp, regex):
    """ Converting the time stamps into the FAVE format """
    #groups: hours, minutes, seconds, miliseconds
    splitter=re.compile(regex)
    result=splitter.findall(timestamp)
    seconds=int(result[0][0])*3600+int(result[0][1])*60+int(result[0][2])
    return (str(seconds)+"."+result[0][3])


def inputchecker(file_type, file_encoding):
    """ Checking if input is valid """
    if formatdict.get(file_type, None) == None:
        raise KeyError ("{} is not a valid file type. This script accepts srt, sbv, and vtt files".format(file_type))
    try:
        codecs.lookup(file_encoding)
    except LookupError as err:
        raise LookupError ("Make sure you have picked a a valid encoding for your file.\nIt is currently set to \'{}\'. Common formats are \'utf-8\' or \'ascii\'.".format(file_encoding))
    

if __name__ == "__main__":
    main(*sys.argv[1:])




