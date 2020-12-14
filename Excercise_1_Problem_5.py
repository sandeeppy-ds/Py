'''                    Factorial         '''



numb = 3

fact = 1

for i in range(1, numb+1):
	fact = i * fact

print (" factorial is ", fact)



strr = "hi how are you"

count= 1

for i in range(len(strr)):
	if (strr[i]==' '):
		count= count + 1

print(count)