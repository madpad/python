#spam = ['a','b','c','d','e']
spam=[]
while True:
	element=input("enter an element in list or q to quit:")
	spam=spam+[element]
	if element=="q":
		break
		spam=spam+[element]
n=len(spam)
last = spam[-2]
newspam = spam
newspam.pop()
newspam.pop() #pops out the last value in the list newspam
for i in range(n-2):
	print(newspam[i] + ',',end='')
print('and ' + last)
