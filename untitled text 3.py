import codecs

try:
	codecs.lookup("trr")
except LookupError, err:
	print "Make sure you have picked the right encoding for your file.\nIt is currently set to {}. Common formats are \'utf-8\' or \'ascii\'.".format("assi")
	raise LookupError, err