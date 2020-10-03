spam = ['a','b','c','d','e']
n=len(spam)
last = spam[-1]
newspam = spam
newspam.remove(last)
for i in range(n-1):
	print(newspam[i] + ',',end='')
print('and ' + last)
