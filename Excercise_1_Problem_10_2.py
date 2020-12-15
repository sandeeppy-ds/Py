#Write a program that computes the value in the form of x+xx+xxx+xxxx. For Example, if x = 2, result should be 2+22+222+2222 = 2468


x = 2

#y = x + ((10*x)+2) + ((100*x)+22) + ((1000*x)+222)
a= ((10*x)+x)
b= ((100*x)+a)
c= ((1000*x)+b)
# print(x)
# print(a)
# print(b)
# print(c)

y = x + a + b + c

#print(y)

print(x,"+",a,"+",b,"+",c,"=",y)
