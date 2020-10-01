spam = ['a','b','c','d','e']
n=len(spam)
last = spam[-1]
newspam = spam
newspam=spam.remove(last)
for i in range(n-1):
	print(str(newspam[i]),end='')
print(last)