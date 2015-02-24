from math_functions import *
import random

def key_generation(p,q): 
	n = p*q
	phi_n = (p-1)*(q-1)
	e = choose_e(phi_n)
	return n, phi_n, e

def choose_e(phi_n): 
	primes = generate_primes(phi_n)
	print primes
	e = random.choice(primes)
	return e

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
	print key_generation(11,13)




if __name__ == '__main__':
	main()