import unittest
from temperature import Temperature

class Test_Temperature(unittest.TestCase):

    def setUp(self):
        self.temp1 = Temperature()
        self.temp2 = Temperature(100)

    def tearDown(self):
        del self.temp1
        del self.temp2

    def test_celsius(self):
        self.assertEqual(self.temp1.celsius, 0)
        self.assertEqual(self.temp2.celsius, 100)

    def test_fahrenheit(self):
        self.assertEqual(self.temp1.fahrenheit, 32)
        self.assertEqual(self.temp2.fahrenheit, 212)

    def test_change_celsius(self):
        self.temp1.celsius = 50
        self.temp2.fahrenheit = 100
        self.assertEqual(self.temp1.celsius, 50)
        self.assertAlmostEqual(self.temp2.celsius, 37 + 7/9)
        self.assertEqual(self.temp1.fahrenheit, 122)
        self.assertEqual(self.temp2.fahrenheit, 100)

if __name__ == '__main__':
    unittest.main()
