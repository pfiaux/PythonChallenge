# Python Challenge level 2
# http://www.pythonchallenge.com/pc/def/ocr.html


inputfile = open("./level2_data.txt")

freq = {}

rare = ""
count = 0

for line in inputfile:
	#print line
	for c in line:
		if freq.setdefault(c):
			freq[c] += 1
		elif c.isalpha(): # dictionaries don't keep order
			print c
		else:
			freq[c] = 1
inputfile.close()
			

for c in freq:
	if freq[c] < 10:
		print c, freq[c]
		rare += c

print rare
print sorted(rare)


#solution http://www.pythonchallenge.com/pcc/def/equality.html 