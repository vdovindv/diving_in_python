import sys

def sum(digit_string):
	res = 0
	for digit in digit_string:
		res+=int(digit)
	return res

if __name__=='__main__':
	digit_string = sys.argv[1]
	print(sum(digit_string))
