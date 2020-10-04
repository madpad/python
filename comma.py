#spam = ['a','b','c','d','e']
spam=[]
while True:
	element=input("enter an element in list or q to quit:")
	spam=spam+[element]
	if element=="q":
		break
n=len(spam)
last = spam[-1]
newspam = spam
newspam.pop() #pops out the last value in the list newspam
for i in range(n-1):
	print(newspam[i] + ',',end='')
print('and ' + last)
