import unittest
from city_functions import city_country

class TestCityFunctions(unittest.TestCase):

	def test_city_country(self):
		w = city_country("santiago", "chile")
		self.assertEqual(w, "Santiago, Chile")

if __name__ == "__main__":
	unittest.main()
