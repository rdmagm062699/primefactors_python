
class PrimeFactors(object):

	def get_prime_factors(self, num):
		factors = []

		if num > 1:
			if num % 2 == 0:
				factors.append(2)
				num /= 2
				if num > 1:
					factors.append(num)
				return factors
			
			factors.append(num)
			return factors

		return factors