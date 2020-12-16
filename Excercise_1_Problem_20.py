# #Define a function that takes four string parameters and 
# print only 2nd and 3rd strings together in one line & 1st and 4th strings together in another line.
# Condition: Achieve this only through “for loop” within the function.



def together(a,b,c,d):
	for i in (b,c):
		print(i, end=",")
	print(end="\n")
	for j in (a,d):
		print(j, end=',')
		


together("sand","mud","clay","water")