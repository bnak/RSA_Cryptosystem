from math_functions import *

def key_generation(): 
	print "ran"

def encrypt(string1):
	string1 = string1.lower()
	array_of_char = []
	for char in string1:
		array_of_char.append(ord(char)-96) 

	return array_of_char


def decrypt():
	print "ran"


def main():
	p = 13331
	q = 17257
	print encrypt("Ran")
	print euclidean_GCD(80, 90)




if __name__ == '__main__':
	main()