import unittest
from gcd import gcd
print("hello")




class tests(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("Тестирование старт")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("Финиш тестирования")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + self.shortDescription() + "]")
        print("")


    def test_one(self):
        """тест двух равных чисел"""
        print("id: " + self.id())
        self.assertEqual(gcd(1, 1.0), 1)
    def test_one1(self):
        """тест двух простых чисел"""
        print("id: " + self.id())
        self.assertEqual(gcd(17, -1.0), 1)
    def test_one2(self):
        """тест двух простых чисел одинаковых чисел"""
        print("id: " + self.id())
        self.assertEqual(gcd(-11, 11.0), 11)

        
    def test_nul(self):
        """тест с нулями"""
        self.assertEqual(gcd(0, 0), 0)
    def test_nul1(self):
        """ноль с одной стороны"""
        self.assertEqual(gcd(5, 0), 5)
    def test_nul2(self):
        """ноль с другой"""
        print("id: " + self.id())
        self.assertEqual(gcd(0, 15), 15)
        
    def test_five(self):
        """тест с пятерками"""
        print("id: " + self.id())
        self.assertEqual(gcd(5, 10), 5)
    def test_five1(self):
        """тест с пятерками 2"""
        self.assertEqual(gcd(-5, 10.0), 5)
    def test_five2(self):
        """тест с пятерками 3"""
        self.assertEqual(gcd(-51, 51), 51)
    def test_five3(self):
        """тест с пятерками 4"""
        self.assertEqual(gcd(-51, 51.0), 51)
    def test_five4(self):
        """тест с пятерками 5"""
        self.assertEqual(gcd(-11, 17.0), 1)
    def test_five5(self):
        """тест с с отрицательным числом"""    
        self.assertEqual(gcd(-99, 9.0), 9)
        
    def test_for(self):
        """тест с четверками"""
        self.assertEqual(gcd(8, 4), 4)
 
    def test_for1(self):
        """тест для большого числа"""
        self.assertEqual(gcd(8, -44), 4)
    def test_for2(self):
        """тест  чисел"""
        self.assertEqual(gcd(888888, 4), 4)
    def test_for4(self):
        """тест для большого числа"""
        self.assertEqual(gcd(99999999999999999999, 11111111111111111111), 11111111111111111111)
    def test_noequal(self):
        """тест для строки"""
        self.assertNotEqual(gcd(1, 10.0), "1.0")

        
if __name__ == '__main__':
    unittest.main()
