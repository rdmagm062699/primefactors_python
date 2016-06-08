
class PrimeFactors(object):

	def get_prime_factors(self, num):
		factors = []
		
		while num > 1:
			for i in range(2, num+1):
				if num % i == 0:
					factors.append(i)
					num //= i

		return factors