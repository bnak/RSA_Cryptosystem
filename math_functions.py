def generate_primes(num): 
	primes = [2,3]
	for i in range (3, num+1):
		num_is_prime = True
		for item in primes: 
			if i % item == 0:
				num_is_prime = False

		if num_is_prime == True:
			primes.append(i)

	return primes


def euclidean_GCD (a,b): 
	r = max(a,b) - min(a,b)
	if a == 0 and b == 0: 
		return 0
	elif a==0 or b == 0: 
		print "No GCD for", a, b
		return None
	elif min(a,b)%r ==0: 
		return r
	else: 
		return euclidean_GCD(min(a,b), r)

def least_common_multiple(a,b): 
	#Proposition: The least common multiple of a and b is the product of a,b divided by the GCD.
	lcm = (a*b)/euclidean_GCD(a,b)
	return lcm