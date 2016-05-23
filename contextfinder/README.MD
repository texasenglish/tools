####The Contextfinder

The Contextfinder takes a file with speech sounds and uses the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) to add preceding and following sounds.

CSVFor instance, it can add the consonants preceding or following a vowel. Vowels must be transcribed according to the [ARPABET](https://en.wikipedia.org/wiki/Arpabet) conventions. 

Arguments

    file_name -- the name of the file to be processed. Use the full path e.g. '~/Downloads/dataset.csv'.
    variable_column -- the name of the column in your dataset that contains the ARPABET-transcribed sound of interest.
    word_column -- the name of the column in your dataset that contains the word containing the variable.
    pre_distance -- the distance from the variable to the preceding sound to be extracted. Defaults to -1, i.e. the immediately preceding sound
    post_distance -- the distance from the variable to the following sound to be extracted. Deafaults to 1, i.e. the immediately following sound
    dialect -- the formatting of the csv file, defaults to 'excel'. 


