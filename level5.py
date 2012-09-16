# Python Challenge Level 5
# http://www.pythonchallenge.com/pc/def/peak.html

# Title: peak hell

# hint
# <!-- peak hell sounds familiar ? -->
# ok got it pickle...

# <peakhell src="banner.p"/>
# renamed banner.p level5_data.p

inputfile = open("./level5_data.p")
#data = inputfile.read()

import pprint, pickle

data1 = pickle.load(inputfile)
inputfile.close()
#pprint.pprint(data1)

for linedata in data1:
	line = ""
	for part in linedata:
		line += part[0]*part[1]
	print line
	