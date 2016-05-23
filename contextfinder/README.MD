####The Contextfinder

The Contextfinder takes a file with speech sounds and uses the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) to add sounds preceding or following the sound of interest.

The Contextfinder accepts comma-separated and tab-delimited files. The dataset must contain  
-a column of variables transcribed according to the [ARPABET](https://en.wikipedia.org/wiki/Arpabet) conventions and 
-a column with the word the respective variable occurred in. 
For instance, if we have an instance of the word *high* and are interested in the performance of its vowel, we could list the transcribed vowel (AY1) in a column labeled *vowel* and the word *high* in a column labeled *word*. See below on how this would be reflected in the settings to the Contextfinder.  


Arguments

    file_name -- the name of the file to be processed. Use the full path e.g. '~/Downloads/dataset.csv'.
    variable_column -- the name of the column in your dataset that contains the ARPABET-transcribed sound of interest.
    word_column -- the name of the column in your dataset that contains the word containing the variable.
    pre_distance -- the distance from the variable to the preceding sound to be extracted. Defaults to -1, i.e. the immediately preceding sound
    post_distance -- the distance from the variable to the following sound to be extracted. Deafaults to 1, i.e. the immediately following sound
    dialect -- the formatting of the csv file, defaults to 'excel'. For tab-delimited files, set to 'excel-tab'

For example, if we were dealing with the spreadsheet described above, we might enter

    main('~/Downloads/dataset.csv','vowel', 'word')

This would return a spreadsheet with 
    
