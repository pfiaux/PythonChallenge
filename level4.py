# Python Challenge Level 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php

# Title: follow the chain

# <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
# end. 400 times is more than enough. -->

# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# and the next nothing is 44827

# First Nothing 21345
# 16044 / 2  = 8022 could use as new start to save time
# 82684 is misleading could use 63579 as new start

import urllib
import re

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

# function to format url requests based on a nothing
def get_next_nothing( nothing ):
	#get page content
	url = base_url+"?%s" % urllib.urlencode({'nothing': nothing})
	result = urllib.urlopen(url).read()
	
	#parse number
	next_nothing = re.findall(r"\d+", result) #re option... probably slower
	# alternative
	# faster but messes up when numbers not surounded with spaces ( 1234. )
	#next_nothing = [int(s) for s in result.split() if s.isdigit()]
	
	#special actions depending on results
	if (len(result) > 29):
		print "n: ", nothing, "=", result
	if len(next_nothing)==0:
		if result == "Yes. Divide by two and keep going.":
			print "using ", nothing / 2, " as next nothing"
			return get_next_nothing(nothing / 2)
		else:
			print "couldn't get next nothing for: ", nothing, " got ", result
			return -1
	if len(next_nothing) > 1:
		print "using ", next_nothing[1], "as next nothing" 
		return next_nothing[1]
	return next_nothing[0]
	
#print get_next_nothing(12345) # test the first nothing

#start_nothing = 12345 # first nothing
#start_nothing = 8022 # asked to devide by 2
start_nothing = 63579 # asked to sort between multiple numbers...

current_nothing = start_nothing
print "starting with", current_nothing

count = 0
nothings = [start_nothing]

while (count < 400):
	count+= 1
	if (count % 10 == 0):
		print '.'
	#print count, ":", current_nothing
	current_nothing = get_next_nothing(current_nothing)
	if current_nothing < 0:
		break
	nothings.append(current_nothing)
	
#print nothings
	
