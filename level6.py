# Python Challenge Level 6
# http://www.pythonchallenge.com/pc/def/channel.html

# Title: now there are pairs

# hint
# <-- zip -->

import zipfile
import re

channel = zipfile.ZipFile("level6_data.zip" ,"r")

#readme = channel.open("readme.txt","r")
#print readme.read()

start = "90052"
nothing = start

count = 0

list = channel.namelist()

print "zipfile comments", channel.comment

comments = ""
for info in channel.infolist():
	if len(info.comment) > 0:
		#print info.comment,
		comments += info.comment

print "".join(comments.split(" "))
# looks like oxygen to me...


#get all files without nohthings...
for file in list:
	data = channel.open(file,"r").read()
	if (len(re.findall(r"Next nothing is (\d+)", data)) < 1):
		print file, data

#follow the nothings
while 1:
	next_file = nothing + ".txt"
	file = channel.open(next_file, "r")
	next_nothing = file.read()
	numbers = re.findall(r"nothing is (\d+)", next_nothing)
	if len(numbers) < 1:
		print count, next_nothing
		break
	if len(numbers) > 1:
		print count, numbers
	nothing = numbers[0]
	#print count, next_nothing, nothing
	count+= 1





