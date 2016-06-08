import nose.tools as nt
from primefactors.my_prime_factors import *
import unittest

class MyPrimeFactorsTest(unittest.TestCase):

	def test_can_create_prime_factors_object(self):
		test = PrimeFactors()

		nt.assert_is_not_none(test)