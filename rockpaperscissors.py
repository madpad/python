#Rock Paper Scissors
import random, sys
print ('ROCK Paper and Scissors')
wins =0
losses =0
ties=0
#
while True:
	print('%s wins, %slosses, %sties' % (wins, losses, ties))
	while True:
		print('Play your move (r)ock, (p)aper, (s)cissors, (q)uit')
		playermove = input()
		if playermove == 'q':
			sys.exit() #quit the game
		elif playermove == 'r' or playermove == 'p' or playermove == 's':
			break #break out of the player loop
	print('You played str(playermove)')
	#
	if playermove == 'r':
		print('ROCK against...')
	elif playermove == 'p':
		print('Paper against...')
	elif playermove == 's':
		print('Scissors against...')
#
	#display what the computer moves
	randomnumber = random.randint(1,3)
	computermove = 0
	if randomnumber == 1:
		computermove = 'r'
		print('ROCK')
	elif randomnumber ==2:
		computermove = 'p'
		print('SCISSORS')
	elif randomnumber ==3:
		computermove == 's'
		print('SCISSORS')
#
	if playermove == 'r' and computermove == 'r':
		print('It is a tie')
		ties = ties+1
	elif playermove == 'r' and computermove == 'p':
		print('Paper contains rock. You lose')
		losses = losses+1
	elif playermove == 'r' and computermove == 's':
		print('Rock crushes scissors. You win')
		wins = wins+1
	elif playermove == 'p' and computermove == 'r':
		print('paper contains rock. You win')
		wins = wins+1
	elif playermove == 'p' and computermove == 's':
		print('Scissors cuts paper. You lose')
		losses = losses+1
	elif playermove == 's' and computermove == 'r':
		print('Rock crushes scissors. You lose')
		losses = losses+1
	elif playermove == 's' and computermove == 'p':
		print('scissors cuts paper. You win')
		wins = wins+1

