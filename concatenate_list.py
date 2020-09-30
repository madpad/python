#program to capture a list of bank names
#
banknames =[]
while True:
	print('Enter name of Bank ' + str(len(banknames)+1) + 'or enter a blank to end:')
	name = input()
	if name =='':
		break
	banknames = banknames +[name] #list concatenation
print('The bank names are')
for name in banknames:
	print('  ' + name)
