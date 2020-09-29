import sys
#
def collatz(number):
	if number%2 ==0:
		print(number//2)
	elif number%2==1:
		print(3*number + 1)

while True:
	print('enter any number')
	number=int(input())
	collatz(number)
	print(collatz(number))
	if collatz(number)==1:
		sys.ext()
	elif collatz(number)!=1:
		continue
