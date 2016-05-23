import csv
import os
import nltk

directory="~/Downloads"
inputfile="normeddata.csv"

#if header
count = 1	
datadict={}
with open(os.path.expanduser(os.path.join(directory,inputfile)), "rU") as inputcsv:
	inputdicti=csv.DictReader(inputcsv)
	for row in inputdicti:
		#associate row number with entry
		datadict[count]=row
		count = count+1


		
def locator(transcription, index, distance):
	print transcription, index, distance
	if index+distance > -1 and index+distance < len(transcription):
		return transcription[index+distance]
	else:
		return "None"
#if header:
#header=['speaker', 'file', 'vowel', 'context', "F1'", "F2'", "F3'", "F1' gl", "F2' gl", "F3' gl", 'where', 'gender', 'ethnicity']


#moveable: header, vowel name, context name, index of sound
cmudict = nltk.corpus.cmudict.dict()

def main():
	#datadict=inputreader
	outputfile=open(os.path.expanduser(os.path.join(directory,inputfile.rstrip(".csv")+"_context_added.csv")), "w")
	outputcsv=csv.writer(outputfile)
	
	for entry in datadict:
		vowel = datadict[entry]['vowel']
		word = datadict[entry]['context']
		transcript = [i for i in cmudict[word.lower()] if vowel in i]
		if len(transcript) < 1:
			print "\n---\nError in line {}:".format(entry)
			print "In the CMU dictionary, word {} does not contain the vowel {}".format(word, vowel)
			print "\n---\n"		
		else:
			transcript=transcript[0]
			vowelindex=transcript.index(vowel)
			datadict[entry]['cmu_transcription']=" ".join(transcript)
			datadict[entry]['pre_sound']=locator(transcript, vowelindex, -1)
			datadict[entry]['post_sound']=locator(transcript, vowelindex, +1)
	header=datadict.values()[0].keys()
	outputcsv.writerow(header)
	for entry in datadict:
		if len(datadict[entry]) == len(header):
			outputcsv.writerow(datadict[entry].values())
		else:
			print "\n---\nWarning: Row {} not added to outputfile {}\n---\n".format(entry, outputfile.name)
	
	pre=[datadict[i].get('pre_sound', None) for i in datadict]
	post=[datadict[i].get('post_sound', None) for i in datadict]
	print set(pre)
	print set(post)
	
	
				
				
				
			

	

main()




# for row in dati[1:len(dati)]:
#     foll_env=row[8]
#     #print foll_env
#     stress=stressdict.get(foll_env[len(foll_env)-1], "NONE")
#     hilo=hilodict.get(foll_env[:-1], "NONE")
#     backfront=frontbackdict.get(foll_env[:-1], "NONE")
#     #print stress
#     #print hilo
#     #print backfront
#     #print hilo+backfront
#     #print "-----------\n\n"
#     result=[stress, hilo, backfront, hilo+backfront]
#     row=row+result
#     #print row
#     output.write(",".join(row)+"\n")
    


def vowelfinder(transcription):
    #these are the vowels in the CMU dictionary
    vowels=["AA", "AH", "AW", "EH", "EY", "IH", "OW", "UH", "AE", "AO", "AY", "ER", "IY", "OY", "UW"]
    #this makes a list of primary stress vowels based on the vowels list above
    primestressvowels=[str(i+"1") for i in vowels]
    for sound in transcription:
        if sound in primestressvowels:
            #print sound
            return [transcription.index(sound)-1, transcription.index(sound), transcription.index(sound)+1]
   
   
            
out_of_dict_words={}

            
#vowel is the vowel, context the word
           
