## The Faveconverter

### Description
The Faveconverter converts various subtitle formats into tab-delimited .txt files for vowel alignment. 

It accepts SubRip, Subviewer or VTT files and adapts them to the template required by the University of Pennsylvania's Forced Vowel Alignment and Extraction* ([FAVE](http://fave.ling.upenn.edu/)) algorithm.

The script takes a folder as input and converts all the files in this folder. It will not replace any of the original files. Instead, it will create a new file that consists of the original file name plus the ending  "_faved.txt". 


Arguments:

    speaker_name -- the name of the main tier; this will be used for labeling by FAVE.

    file_type -- the formatting of the input file. Default ist .srt (SubRip Text), also accepts Subviewer (.sub or .sbv) and WebVTT (.vtt). 

    file_encoding -- character encoding of the input file. Default is utf-8 but will accept anything Python can deal with. 

    speaker_id -- the speaker ID. An optional speaker identifier that will not be further processed by FAVE.  
    
    Additionally, the user will be asked to select a folder containing the input files via a graphical interface. 

*Rosenfelder, Ingrid; Fruehwald, Joe; Evanini, Keelan and Jiahong Yuan. 2011. FAVE (Forced Alignment and Vowel Extraction) Program Suite. http://fave.ling.upenn.edu.


### How to run it
#### Preparations
It's easiest run this script from the command line. On a Mac, all you need to do is open the Terminal (search for "Terminal.app" in the "Applications" folder). 
On Windows, you might have to install [Python](https://www.python.org/downloads/windows/) first and [change](http://www.anthonydebarros.com/2015/08/16/setting-up-python-in-windows-10/) the command line settings. 
Then you can use the command line tool (just type 'cmd' into the All Programs window). 
Download the script. You need faveconverter_py2.py if you are running Python 2, faveconverter_py3.py if you are running Python 3. 
If you are unsure which version you have on your computer, type 

`python -V`

into the command line prompt. 

#### Running the script
Then use the Terminal to navigate to the folder you saved the script in. If it is in Downloads, for instance, do this:
on the Mac:

`cd ~/User/Downloads`

on Windows:

`cd `

Hint: hit `cd ..` to take a step back, type `ls` to look at the folder you are in. Basic command line commands are given for the Mac [here](https://www.git-tower.com/blog/command-line-cheat-sheet/) and for Windows [here](http://www.cs.columbia.edu/~sedwards/classes/2016/1102-spring/Command%20Prompt%20Cheatsheet.pdf).

Now you can run the script like so:

    python faveconverter_py2.py "Patrick"

where "Patrick" is the name of your speaker. Additional settings, to be added in this order after the speaker name, are

    file_type, file_encoding, speaker_id

where `file_type` is the formatting of the input file (default is `"srt"`, but accepts `"sub"`, `"sbv"`, `"vtt"` as well). `file_encoding` (default is `"utf-8"`) specifies the character encoding of the file; either `"utf-8"` or `"ascii"` should work for most English-language files. `speaker_id` is an optional column in the tab-delimited file that FAVE works with, but it is not part of the Textgrid FAVE returns. Default setting is `"default"`. 


#### Example
Thus, 

    python faveconverter_p2.py "Patrick" "sbv" "utf-8" "PP"

will work with an input file formatted according to the sbv specifications and is encoded in UTF-8. The script will add "Patrick" as the speaker name, and "PP" as the speaker ID. 


### Etc



