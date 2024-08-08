import unittest
import city_functions

class TestingCase(unittest.TestCase):

	def testing_population(self):

		f = city_functions.city_country("santiago", "chile", "5000000")
		self.assertEqual(f, "Santiago, Chile - Population: 5000000")

if __name__ == "__main__":
	unittest.main()