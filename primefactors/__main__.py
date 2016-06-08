import sys
from my_prime_factors import PrimeFactors

if __name__ == "__main__":
	pf = PrimeFactors()
	
	print(pf.get_prime_factors(int(sys.argv[1])))