## The Faveconverter

# Description
The script converts various subtitle formats into a tab-delimited .txt file for vowel alignment. 
It accepts SubRip, Subviewer or VTT files and adapts them to the formatting required by the University of Pennsylvania's Forced Vowel Alignment and Extraction ([FAVE](http://fave.ling.upenn.edu/)*) algorithm.


Arguments:

    speaker_name -- the name of the main tier; this will be used for labeling by FAVE

    file_type -- the formatting of the input file. Default ist .srt (SubRip Text), but also accepts Subviewer (.sub or .sbv) and WebVTT (.vtt). 

    file_encoding -- character encoding of the input file. Default is utf-8 but will accept anything Python can deal with. 

    speaker_id -- the speaker ID is an optional line to identify the speaker but will not be used by FAVE.  
    
    Additionally, the user will be asked to select a folder containing the files via a graphical interface. 

*Rosenfelder, Ingrid; Fruehwald, Joe; Evanini, Keelan and Jiahong Yuan. 2011. FAVE (Forced Alignment and Vowel Extraction) Program Suite. http://fave.ling.upenn.edu.

# How to run it
The script takes a folder as input and covnerts all the files in it. 
It will not replace any of the original files. 
It's easiest run this script from the command line. On an Mac, all you need to do is open the terminal. 
On Windows, you might have to install [Python](https://www.python.org/downloads/windows/) first and [change](http://www.anthonydebarros.com/2015/08/16/setting-up-python-in-windows-10/) the command line settings. 
Then you can use the command line tool (just type 'cmd' into the All Programs window). I will call this the Terminal for ease of reference. 
Download the script. You need a _py2.py if you are running Python 2, _py3.py if you are running Python 3. 
If you are unsure which one you have, type 

`python -V`

into the command line prompt. 

Then use the Terminal, navigate to the folder you saved it in. If it is in Downloads, for instance, do this:

`cd ~/User/Downloads`

on Windows 

`cd `

hit `cd ..` to take a step back, type `ls` to look at the folder you are in. 

Now you can run it like so:

    python faveconverter_py2.py "Patrick"

where "Patrick" is the name of your speaker. In addition to speaker name, you might have to change the settings for 




Thus, 





`python -V`
