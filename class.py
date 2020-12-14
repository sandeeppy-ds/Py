
#retrn statement is the final satisfatory reult.

def pubg(x,y):
	return x**3,y**2
	print ("pubg is a game")

pubg(2,3) #here print statement inside a function doesnt work since we have writtened after the return

#inorder to know what a funtion is returned when its called.

print(pubg(2,3))


a=30

class home:
	
	a=40 #class variable
	def floor(self):  #instance object
		print("floor")
		a=30 #instance variable
		print(a)

	def walls(): #class object
		print("walls")
		a=25 #local variable
		print(a)

	def pillars():
		print("pillars")

	def roof():
		print("roof")

	def sand(self):
		self.a=10
		print(a)
	print (a)
print(a)

home()


b = home()

print(b.sand())
print(b.floor())

print(home.roof())