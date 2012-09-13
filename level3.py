# Python Challenge Level 3
# http://www.pythonchallenge.com/pc/def/equality.html



inputfile = open("./level3.txt")
data = ""
for line in inputfile:
	data = data + line.strip()
#data = inputfile.read()
#data = "1234567890"
inputfile.close()

length = len(data)
bfront = 0
front = 0
current = 0
back = 0
aback = 0

for i in range(3,length-3):
	front = data[i-3:i]
	current = data[i]
	back = data[i+1:i+4]
	# must be a lower case letter between 3 big ones
	if (front.isupper() and current.islower() and back.isupper()):
		# must be exactly 3 big ones on each side not 4!
		if (i == 3 or data[i-4].islower()) and (i==length-3 or data[i+5].islower()):
			print front, ">", current, "<", back #debug
	front = 0
	back = 0