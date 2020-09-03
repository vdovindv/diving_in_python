import sys

def equasion(a, b, c):
	d = (b**2 - 4*a*c)**0.5
	x_1 = (-b + d)/(2*a)
	x_2 = (-b - d)/(2*a)
	return(x_1, x_2)

if __name__=='__main__':
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	c = int(sys.argv[3])
	x_1, x_2 = equasion(a, b, c)
	print(int(x_1), '\n', int(x_2))
