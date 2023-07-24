def f(n):
	if n % 2 ==1:
		n= 3*n +1
	else:
		n = n//2
	return n
def c(n):
	if n==int(n):
		if n>0:
			sequence = []
			k =n
			if n ==1:
				sequence.append(int(1))
				return sequence
			while k!=1:
				k = f(k)
				sequence.append(int(k))
			return sequence
		else:
			return 'not defined for numbers less than 1'
	else:
		return 'define for positive integers'


# chess.verbose = True
if __name__=='__main__':
    n = int(input())
    print(c(n))



