#If given, sample = "10,10,20,30,10,30,40", count 0’s, 1’s, 2’s, 3’s, 4’s, 9’s (number of occurrences) in the given string.


sample = "10,10,20,30,10,30,40"
i=0


def calling(h):
	count=0
	for i in range(len(sample)):
		if (sample[i] == h):
			
			x=sample[i]
			count = count+1
	a = print("no.of occurences of ", h, "in the string is", count)

calling('0')

calling('1')

calling('2')

calling("4")

calling("3")

calling("9")



	# elif (sample[i] == '1'):
		
	# 	x=sample[i]
	# 	print((x))

	# elif (sample[i] == '2'):
		
	# 	x=sample[i]
	# 	print((x))

	# elif (sample[i] == '3'):
		
	# 	x=sample[i]
	# 	print((x))

	# elif (sample[i] == '4'):
		
	# 	x=sample[i]
	# 	print((x))


	# elif (sample[i] == '9'):
		
	# 	x=sample[i]
	# 	print((x))