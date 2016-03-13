# Use the file name mbox-short.txt as the file name

fname = raw_input("Enter file name: ")

try:
	fh = open(fname)
except:
	print 'Cannot open', fname, 'file'
	exit()

lines_count = 0
confidence_count = 0

for line in fh:
	line = line.strip()
	if line.startswith("X-DSPAM-Confidence:"):
		start_point = line.find(':') + 1
		confidence = float(line[start_point:].strip())
		lines_count = lines_count + 1
		confidence_count = confidence_count + confidence

confidence_avg = confidence_count / lines_count

print 'Average spam confidence:', confidence_avg