#Write a program that computes the net amount in bank account based on transaction mode. 
#Function must take two parameters, amount and transaction_mode. 
#Acceptable transaction_modes are “W” for Withdrawal and “D” for Deposit.
# Based on transaction_mode, program should print net amount.

W= "Withdrawal"
D= "Deposit"
net_amount= 100
def banking(x,y):
	if y == D:
		print("net amount is", net_amount + x)
	elif y== W:
		print("net amount is", net_amount - x)

banking(10,W)
banking(25,W)
banking(22,D)

