#!/etc/bin/python

try:
    name = raw_input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
except:
    print 'Cannot open', name, 'file'
    exit()

count = 0
emails = dict()

for line in handle:
    line = line.strip()
    if line.startswith('From '):
        emails[line.split()[1]] = emails.get(line.split()[1], 0) + 1


email_max = None
email_max_count = None

for email,count in emails.items():
    if count is None or count > email_max_count:
        email_max = email
        email_max_count = count

print email_max, email_max_count
