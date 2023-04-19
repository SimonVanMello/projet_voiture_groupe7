import unittest

class Testultrasons(unittest.TestCase):

    def test_mesure(self):
        distance = 50
        # Assertion de la distance mesurée
        self.assertEqual(distance, 50, "Distance exacte")

if __name__ == '__main__':
    unittest.main()