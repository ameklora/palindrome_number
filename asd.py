x = int(input())
def check(x=x, counter=0):
	for num in x:
		ind = x.index(num)
		ind = -ind
		if num == x[ind - 1]:
			counter += 1
	if counter == len(x):
		return True
	else:
		return False
def smth(x):
	x = ' '.join(str(x)).split()
	print(check(x))
smth(x)
