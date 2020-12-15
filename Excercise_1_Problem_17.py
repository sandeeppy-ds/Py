#Create four function-within-another function from outer function and call all of them 
#but result must be printed as “empty” exactly as one time. Do not use print function globally.


def out():
	print("empty")

	def in1():
		pass
	int()
	def in2():
		pass
	in2()
	def in3():
		pass
	in3()

out()