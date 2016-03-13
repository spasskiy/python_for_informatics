fname = raw_input("Enter file name: ")

try:
	fh = open(fname,'r')
except:
	print 'Cannot open', fname, 'file'
	exit()

lst = list()

for line in fh:
	words_line = line.split()
	for word in words_line:
		if word not in lst:
			lst.append(word)

lst.sort()

print lst