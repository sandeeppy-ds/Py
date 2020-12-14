strr = "counting words in a string"

count= 1

for i in range(len(strr)):
	if(strr[i]==' '):
		count = count + 1


print(count) #prints no.of words in a string


print(len(strr)) #prints length of the string


def  counting_string_words(strr):
	count= 1
	for i in range(len(strr)):
		if (strr[i] == ' ' or strr[i] == '\n' or strr[i]== '\t'):
			count= count + 1
	return count

stringg = "using function for counting the words in a string"

#counting_string_words(stringg)

print(counting_string_words(stringg))