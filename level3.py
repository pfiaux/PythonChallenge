# Python Challenge Level 3
# http://www.pythonchallenge.com/pc/def/equality.html


# use Reg exp to tryyy
import re

inputfile = open("./level3_data.txt")
data = ""

#for line in inputfile:
#	data = data + line.strip()

pattern = "[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]"

matches = re.findall(pattern, inputfile.read())

count = 0
for match in matches:
	print match[4]
	count+= 1
	
print "found:", count