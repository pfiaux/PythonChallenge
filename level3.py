# Python Challenge Level 3
# http://www.pythonchallenge.com/pc/def/equality.html


# use Reg exp to tryyy
import re

inputfile = open("./level3_data.txt")
data = ""

#for line in inputfile:
#	data = data + line.strip()

pattern = "[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]"

matches = re.findall(pattern, inputfile.read())

for match in matches:
	print match