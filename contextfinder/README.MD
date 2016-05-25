##The Contextfinder

###Description
The Contextfinder takes a file with speech sounds and uses the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) to add sounds preceding and following the sound of interest.

The Contextfinder accepts comma-separated and tab-delimited files. It adds the columns 'pre_sound', 'post_sound' and 'cmu_transcription' to the spreadsheet and saves it as "ORIGINALNAME_context_added.csv". It also offers the option of adding labels to each sound, e.g. categories like voiced fricative. The initial dataset must contain 

* The variable_column: a column of any name containing the variables, transcribed according to  [ARPABET](https://en.wikipedia.org/wiki/Arpabet) conventions. 
* The word_column: a column of any name with the word the respective variable occurred in. 
* The spreadsheet may contain any number of additional columns. 

For instance, if we have an instance of the word *high* and are interested in the qualities of its vowel, we could enter the transcribed vowel (*AY1*) into a column labeled 'vowel' and the word *high* in a column labeled 'word'. See below on how this would be reflected in the settings of Contextfinder.  

    python contextfinder_py2.py file_name vowel_column word_column pre_distance=-1 post_distance=1 dialect='excel' dict_file=None

Arguments

    file_name -- the name of the file to be processed. Use the full path e.g. '~/Downloads/dataset.csv'.
    variable_column -- the name of the column in your dataset that contains the ARPABET-transcribed sound of interest.
    word_column -- the name of the column in your dataset that contains the word containing the variable from variable_column.
    pre_distance -- the distance from the variable to the preceding sound to be extracted. Defaults to -1, i.e. the immediately preceding sound.
    post_distance -- the distance from the variable to the following sound to be extracted. Deafaults to 1, i.e. the immediately following sound.
    dialect -- the formatting of the csv file, defaults to 'excel'. For tab-delimited files, set to 'excel-tab'.
    dict_file -- the path to a text file that matches sounds to labels, with one sound:label pair per line. See [below](https://github.com/patrickschu/txenglish/blob/master/contextfinder/README.MD#preparations) for formatting. 
    

###How to run it
>For general instructions on how to run Python scripts in a shell or how to get the settings right, please click [here](https://github.com/patrickschu/txenglish/edit/master/faveconverter/README.md). 

####Preparations

The file that matches sounds to labels needs to be formatted like this:
sound1:label
sound2:label
...
E.g.:
DH:vd_fricative
HH:vl_fricative
...

You need to have the Natural Language Toolkit installed for this to work. If you don't, simply type

    easy_install --user nltk
    python -m nltk.downloader ‘cmudict’

into the Terminal or Command Line Prompt to install. 

Note that there is a version of Contextfinder for [Python 2](https://github.com/patrickschu/txenglish/blob/master/contextfinder/contextfinder_py2.py) and one for [Python 3](https://github.com/patrickschu/txenglish/blob/master/contextfinder/contextfinder_py3.py). 

###Running it

For example, if we were dealing with the spreadsheet described above, we might enter

    python contextfinder_py2.py '~/Downloads/dataset.csv','vowel', 'word'

This returns a spreadsheet with all the sounds preceding and following the sounds given in the column 'vowel' in their respective 'word'. For the *AY0* in *high*, for instance, it adds *HH* (preceding sound) and *None* (following sound) to the columns 'pre_sound' and 'post_sound' respectively. It also enters the complete transcription *HH AY0* into a column called 'cmu_transcription'. Note that you need to use quotation marks around the variable_name and column_name when calling the Contextfinder. 

The following command extracts the sounds two characters away from the variable and works with a tab-delimited file. It extracts sounds with a distance of two - i.e. the sound pre-preceding the variable or two sounds after the variable:

    python contextfinder_py2.py '~/Downloads/dataset.csv','vowel', 'word', -2, 2, 'excel-tab'

While this returns *None* for both preceding and following sound in *high* because the word is too short, it returns an *AH0* as following sound in the word *highness* (ARPABET:  *HH AY1 N AH0 S*).

### Etc.

Citation. 

Schultz, Patrick. The Contextfinder: A tool for automatic extraction of linguistic context, 2016, https://github.com/patrickschu/txenglish/edit/master/contextfinder/ [Online; accessed XXXX-XX-XX].

The MIT License (MIT)
Copyright (c) 2016 Patrick Schultz

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
