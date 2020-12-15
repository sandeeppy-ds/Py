#Convert a string into an integer. If unable to convert, print “Unable to convert”


import re
strr ="10"
x= re.match("[a-zA-z]", strr)
if x:
	print("unable to convert")
else:
	print(type(int(strr)))