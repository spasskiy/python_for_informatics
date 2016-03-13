def get_hrs():
	hrs_raw = raw_input("Enter Hours: ")
	try:
		hrs = float(hrs_raw)
		if (hrs < 0):
			'Hours should be a positive number'
	except:
		print 'Hours should be a number'
	return hrs

def get_rate():
	rate_raw = raw_input("Enter Rate: ")
	try:
		rate = float(rate_raw)
		if (rate < 0):
			'Rate should be a positive number'
	except:
		print 'Rate should be a number'
	return rate

def computepay(hrs,rate):
	if hrs <= 40:
		pay = (hrs * rate)
	else:
		pay = (rate * ((hrs - 40) * 1.5 + 40))
	return pay


h = get_hrs()
r = get_rate()

p = computepay(h,r)

print p