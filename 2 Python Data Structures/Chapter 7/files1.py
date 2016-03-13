# Use words.txt as the file name
fname = raw_input("Enter file name: ")

try:
	fh = open(fname)
except:
	print 'Cannot open', fname, 'file'
	exit()

for line in fh:
	print line.strip().upper()
	