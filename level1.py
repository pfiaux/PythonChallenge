# Python Challenge level 1
# http://www.pythonchallenge.com/pc/def/map.html


# ref http://www.evanfosmark.com/2009/01/rot13-in-python-30/
from string import ascii_uppercase as uc, ascii_lowercase as lc
import string

reference = lc+uc
offset = 2
coded = lc[offset:] + lc[:offset] + uc[offset:] + uc[:offset]

print "mapping from: ", coded
print "to: ", reference

trans = string.maketrans(reference, coded)

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "http://www.pythonchallenge.com/pc/def/map.html"

print input.translate(trans)

print url.translate(trans)

debug = "ynnjw rm rfc dgjclykc md rfgq nyec, zsr lmr rfc cvrclqgml"
print debug.translate(trans)

# Solution http://wiki.pythonchallenge.com/index.php?title=Level1:Main_Page