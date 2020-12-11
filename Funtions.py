'''   ******Functions****     '''

#Funtions are mainly used to write the logic
# Functions can be called/acessed
# Functions can be defined with any names ( remember naming convention while defining a function is simillar to the variable)
#Functions will always have paranthesis followed by function name and is used to define the parameters
#Indentation is very important while creating a function. we can write n no.of lines of code/logic inside a function.
# Fnctions needs to be called in order to expect the output of a function.



#using global variables as arguments to a function ( Note that if none of the parameters are defined for a function by default it will look for the global variables)

x = 2
y = 4

def calc():
	print (x + 2)
	print (y + 4)

calc()


#Defining a function with arguments
#Here x,y are positional arguments. when ever we pass the parameters by default it will be taken by using the position.

def calc(x,y):
	print (x + 2)
	print (y + 4)

calc(3,5)


#Defining a function with arguments and changing the positions
#positional argument always follows keyword argument
def calc(x,y):
	print (x + 3)
	print (y + 2)

calc(y = 2, x = 4)

calc( 4 , y = 3)

#defing a variable inside a function with * as pre deccissor makes it as a tuple
	#Note that we an only use * for one variable and we cant use for multiple  variables
def calc(x,*y):
	print (x)
	print (y)

calc(1,4,8,9)

calc(2,2,4,3 )


#defining a variable inside a function with ** as pre-decissor makes it a Dictionary

def calc(x,**y):
	print(x)
	print(y)

calc(4)


#We can define a function within a function and is valid only on certain below conditons
   #we need to call the location function inside a global function in order to access it globally.

def project_y(x):
	print(x)
	def project_v(a):
		print ( a + 2)
	project_v(4)



project_y(7)
