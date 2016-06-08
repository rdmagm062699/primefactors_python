import nose.tools as nt
from primefactors.my_prime_factors import *
import unittest

class MyPrimeFactorsTest(unittest.TestCase):

	def test_can_create_prime_factors_object(self):
		pf = PrimeFactors()

		nt.assert_is_not_none(pf)

	def test_one_has_no_prime_factors(self):
		pf = PrimeFactors()

		factors = pf.get_prime_factors(1)

		nt.assert_equal(factors, [])

	def test_prime_factors_of_two(self):
		pf = PrimeFactors()

		factors = pf.get_prime_factors(2)

		nt.assert_equal(factors, [2])

	def test_prime_factors_of_three(self):
		pf = PrimeFactors()

		factors = pf.get_prime_factors(3)

		nt.assert_equal(factors, [3])

	def test_prime_factors_of_four(self):
		pf = PrimeFactors()

		factors = pf.get_prime_factors(4)

		nt.assert_equal(factors, [2,2])

	def test_prime_factors_of_nine(self):
		pf = PrimeFactors()

		factors = pf.get_prime_factors(9)

		nt.assert_equal(factors, [3,3])

	def test_prime_factors_of_ninety(self):
		pf = PrimeFactors()

		factors = pf.get_prime_factors(90)

		nt.assert_equal(sorted(factors), [2,3,3,5])

	def test_prime_factors_of_onehundredtwenty(self):
		pf = PrimeFactors()

		factors = pf.get_prime_factors(120)

		nt.assert_equal(sorted(factors), [2,2,2,3,5])