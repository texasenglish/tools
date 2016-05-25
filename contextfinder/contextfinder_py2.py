import csv
import os
import nltk
import sys
import re



# utilities		
def locator(transcription, index, distance):
	'''extracts sounds a distance away from index (e.g. a vowel)'''
	if index+distance > -1 and index+distance < len(transcription):
		return transcription[index+distance]
	else:
		return "None"

# getting the dictionary
cmudict = nltk.corpus.cmudict.dict()


def main(file_name, vowel_column, word_column, pre_distance=-1, post_distance=1, dialect='excel', dict_file=None):
	'''
	Extract pre-vocalic and post-vocalic sounds based on CMU transcriptions. 
	Write to csv under column names pre-sound and post_sound.
	Note that it takes the first transcription if CMU has several options. 
	'''
	
	filename=file_name
	count = 1	
	datadict={}
	labeldict={}
	
	if dict:
		dictfile=open(dict_file, "r")
		for line in dictfile:
			labeldict[line.split(":")[0]]=line.split(":")[1].rstrip("\n")	
			print labeldict	
	
	#input
	with open(os.path.expanduser(file_name), "rU") as inputcsv:
		inputdicti=csv.DictReader(inputcsv, dialect=dialect)
		for row in inputdicti:
			datadict[count]=row
			count = count+1
	#iterate over rows
	for entry in datadict:
		vowel = datadict[entry][vowel_column]
		word = datadict[entry][word_column]
		transcript = [i for i in cmudict[word.lower()] if vowel in i]
		if len(transcript) < 1:
			print "\n---\nError in line {}:".format(entry)
			print "In the CMU dictionary, word {} does not contain the vowel {}".format(word, vowel)		
		else:
			transcript=transcript[0]
			vowelindex=transcript.index(vowel)
			datadict[entry]['cmu_transcription']=" ".join(transcript)
			datadict[entry]['pre_sound']=locator(transcript, int(vowelindex), int(pre_distance))
			datadict[entry]['post_sound']=locator(transcript, int(vowelindex), int(post_distance))
			datadict[entry]['pre_sound_label']=labeldict[locator(transcript, int(vowelindex), int(pre_distance))]
			datadict[entry]['post_sound_label']=labeldict[locator(transcript, int(vowelindex), int(post_distance))]
	#output
	if dict:
		outputfile=open(os.path.expanduser(filename.rstrip(".csv")+"_context_labels_added.csv"), "w")
	else:
		outputfile=open(os.path.expanduser(filename.rstrip(".csv")+"_context_added.csv"), "w")
	outputcsv=csv.writer(outputfile)
	header=datadict.values()[0].keys()
	outputcsv.writerow(header)
	for entry in datadict:
		if len(datadict[entry]) == len(header):
			outputcsv.writerow(datadict[entry].values())
		else:
			print "\n---\nWarning: Row {} not added to outputfile {}\n---\n".format(entry, outputfile.name)
	
	pre=set([datadict[i].get('pre_sound', None) for i in datadict])
	post=set([datadict[i].get('post_sound', None) for i in datadict])
	#print ",".join([str(s) for s in pre])
	print "\nThe following sounds occur in pre-vocalic position: \n{}".format("\n".join([str(s) for s in pre]))
	print "\nThe following sounds occur in post-vocalic position: \n{}".format("\n".join([str(s) for s in post]))
 	print "\nFinished. File written to ", outputfile.name
	
if __name__ == "__main__":
    main(*sys.argv[1:])
  
   
#just in case            
out_of_dict_words={}


           
