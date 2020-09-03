import sys

def ladder(num):
	res = ''
	for i in range(num):
		res += ' '*(num-i-1) + '#'*(i+1) + '\n'
	print(res)

if __name__=='__main__':
	num = int(sys.argv[1])
	ladder(num)
