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