fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
	fh = open(fname,'r')
except:
	print 'Cannot open', fname, 'file'
	exit()

count = 0
emails = list()

for line in fh:
	line = line.strip()
	if line.startswith('From '):
		info = line.split()
		emails.append(info[1])
		count = count + 1

for email in emails:
	print email

print "There were", count, "lines in the file with From as the first word"

