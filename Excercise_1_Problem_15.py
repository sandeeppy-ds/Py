# Write a program to answer for the following questions. If argument passed as
# a. “How are you”. Program should print “Logically fine…”
#     b. “Stupid”. Program should print “I am more than you think”
#  c. “How can I understand you”. Program should print “Do an experiment with me”

# Answer should include double quotations and must be exact same.


def worst_fun(x):
	if (x == "How are you"):
		print('"Logically fine…"')
	elif (x== "Stupid"):
		print('"I am more than you think"')
	elif (x== "How can I understand you"):
		print('"Do an experiment with me"')



worst_fun("How are you")
worst_fun("Stupid")
worst_fun("How can I understand you")