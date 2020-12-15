
strr = "need to,separate commas,with the world and,great"

# def comma_sep(strr):
# 	for i in range(len(strr)):
# 		if (strr[i]==','):
# 			print()
# 		else:
# 			print(strr[i], end='')

# comma_sep(strr)



def comma_sep(strr):
	for i in strr:
		if (i ==','):
			print()
		else:
			print(i, end='')

comma_sep(strr)