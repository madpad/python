
#Guess a number program
#import random module
import random
secretnumber = random.randint(1,20)
#print(secretnumber)
print('Think of a number between 1 and 20')

#Ask guest to guess the number within 4 tries

for guess in range(1,5):
	print('Take a guess')
	my_guess = int(input())
	#
	if my_guess < secretnumber:
		print('Your guess is too low, Guess again')
	elif my_guess > secretnumber:
		print('Your guess it too high. Guess again')
	else:
		break
#
if my_guess == secretnumber:
	print('You guessed the correct number in ' + str(guess) +' guesses')
else:
	print('Tough luck. The correct guess is' + str(secretnumber))