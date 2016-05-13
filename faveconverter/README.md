## The Faveconverter

### Description
The Faveconverter converts various subtitle formats into tab-delimited .txt files to be used for vowel alignment in FAVE. 

It accepts [SubRip](https://en.wikipedia.org/wiki/SubRip), [Subviewer](https://en.wikipedia.org/wiki/SubViewer) or [VTT](https://developer.mozilla.org/en-US/docs/Web/API/Web_Video_Text_Tracks_Format) files and adapts them to the template required by the University of Pennsylvania's Forced Vowel Alignment and Extraction* ([FAVE](http://fave.ling.upenn.edu/)) algorithm. SubRip, Subviewer and VVT files are used for most online video subtitling e.g. on YouTube. 

The Faveconverter takes a folder as input and converts all the files contained in this folder. It will not replace any of the original files. Instead, it will create new .txt files consisting of the original file name plus the ending  "_faved.txt". 


Arguments:

    speaker_name -- the name or ID of the speaker; in the FAVE output, this will be the label of the main tier.

    file_type -- the formatting of the input file. Default ist "srt" (SubRip Text), also accepts Subviewer ("sub" or "sbv") and WebVTT ("vtt"). 

    file_encoding -- character encoding of the input file. Default is utf-8, but will accept anything Python can deal with. 

    speaker_id -- the speaker ID. An optional speaker identifier that will not be further processed by FAVE.  
    
    Additionally, the user will be asked to select a folder containing the input files via a graphical interface. 

*Rosenfelder, Ingrid; Fruehwald, Joe; Evanini, Keelan and Jiahong Yuan. 2011. FAVE (Forced Alignment and Vowel Extraction) Program Suite. http://fave.ling.upenn.edu.

The Faceconverter was developed for the [Texas English Linguistics Lab](http://www.texasenglish.org/) at [UT Austin](https://twitter.com/TexasSports). 


### How to run it
#### Preparations
It's easiest run to this script from the command line. 

On a Mac, all you need to do is open the Terminal (search for "Terminal.app" in the "Applications" folder). 
On Windows, you might have to install [Python](https://www.python.org/downloads/windows/) first and [change](http://www.anthonydebarros.com/2015/08/16/setting-up-python-in-windows-10/) the command line settings. 
Then you can use the command line tool (just type 'cmd' into the "All Programs" window). 

Download the script. You need [faveconverter_py2.py](https://github.com/patrickschu/txenglish/blob/master/faveconverter/faveconverter_py2.py) if you are running Python 2, [faveconverter_py3.py](https://github.com/patrickschu/txenglish/blob/master/faveconverter/faveconcerter_py3.py) if you are running Python 3. 
If you are unsure which version you have on your computer, type 

`python -V`

into the command line prompt. 

#### Running the script
After navigating to the right version of the script, click on "Raw" on the top right of the screen. Download the resulting textfile. Use the Terminal to navigate to the folder you saved the script in. If it is in Downloads, for instance, do this:

on the Mac:

`cd ~/User/Downloads`

on Windows:

`cd \Users\YOURUSERNAME\Downloads`

Hint: type `cd ..` to take a step back, `ls` on a Mac and `dir` on Windows to look at the contents of the folder you are in. Basic shell commands are listed for the Mac [here](https://www.git-tower.com/blog/command-line-cheat-sheet/) and for Windows [here](http://www.cs.columbia.edu/~sedwards/classes/2016/1102-spring/Command%20Prompt%20Cheatsheet.pdf).

Now you can run the script like so:

    python faveconverter_py2.py "Patrick"

where "Patrick" is the name of your speaker. Additional settings, to be added in this order after the speaker name, are

    file_type, file_encoding, speaker_id

where `file_type` is the formatting of the input file (default is `"srt"`, but accepts `"sub"`, `"sbv"`, `"vtt"` as well). Note that  the file name extension will usually co-incide with the formatting (i.e. a "srt" file will be called XYZ.srt) but it need not be so. The file might as well be called ".txt" or ".xx": changing the file name will not change the file formatting. `file_encoding` (default is `"utf-8"`) specifies the character encoding of the file; either `"utf-8"` or `"ascii"` should work for most English-language files. `speaker_id` is an optional column in the tab-delimited file that FAVE works with, but it is not part of the Praat-Textgrid FAVE returns. Default setting is `"default"`. 


#### Example
Thus, 

    python faveconverter_p2.py "Patrick" "sbv" "utf-8" "PP"

will work with an input file formatted according to the sbv specifications and encoded in UTF-8. The script will add "Patrick" as the speaker name, and "PP" as the speaker ID. 


### Etc.

Citation. 

Schultz, Patrick. Faveconverter: A tool for subtitle conversion, 2016, https://github.com/patrickschu/txenglish/tree/master/faveconverter [Online; accessed XXXX-XX-XX].

The MIT License (MIT)
Copyright (c) 2016 Patrick Schultz

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

