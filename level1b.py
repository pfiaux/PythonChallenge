# Python Challenge level 1
# http://www.pythonchallenge.com/pc/def/map.html

# refactoring it to be called from cmd

import sys 
import string
from string import ascii_uppercase as uc, ascii_lowercase as lc

params = sys.argv[1:]

if len(params) != 2:
	print """Using level1b.py:
	python level1b.py <string> <rotation>"""
else:
	reference = lc+uc
	offset = eval(params[1])
	coded = lc[offset:] + lc[:offset] + uc[offset:] + uc[:offset]
	trans = string.maketrans(reference, coded)
	
	print reference
	print coded

	input = params[0]
	print input.translate(trans)
