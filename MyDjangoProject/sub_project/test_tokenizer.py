import unittest 
from tokenizer import tokenize 
 
class TestTokenize(unittest.TestCase): 
 
    def test_simple_day(self): 
        input_string = "MON 1300-1500"
        expected = ["MON","1300-1500"]
        tokens = tokenize(input_string)
        self.assertEqual(len(tokens),len(expected))
        self.assertEqual(tokens,expected)

    def test_day_and_date(self):
        input_string = "MON, 10 JAN: 1300-1500"
        expected = ["MON, 10 JAN","1300-1500"]
        tokens = tokenize(input_string)
        self.assertEqual(len(tokens),len(expected))
        self.assertEqual(tokens,expected)

    def test_day_and_date_with_year(self):
        input_string = "MON, 10 JAN 2024: 1300-1500"
        expected = ["MON, 10 JAN 2024","1300-1500"]
        tokens = tokenize(input_string)
        self.assertEqual(len(tokens),len(expected))
        self.assertEqual(tokens,expected)

    def test_day_and_date_timerange_is_not_year(self):
        input_string = "MON, 10 JAN 1300-1500"
        expected = ["MON, 10 JAN","1300-1500"]
        tokens = tokenize(input_string)
        self.assertEqual(len(tokens),len(expected))
        self.assertEqual(tokens,expected)
    
    def test_date_range(self):
        input_string = "10 JAN 2024-20 JAN 2024: 1300-1500"
        expected = ["10 JAN 2024","-","20 JAN 2024","1300-1500"]
        tokens = tokenize(input_string)
        self.assertEqual(len(tokens),len(expected))
        self.assertEqual(tokens,expected)

    def test_multiple_time_ranges(self):
        input_string = "MON, 10 JAN: 1300-1500 1600-1700"
        expected = ["MON, 10 JAN","1300-1500","1600-1700"]
        tokens = tokenize(input_string)
        self.assertEqual(len(tokens),len(expected))
        self.assertEqual(tokens,expected)
    
    def test_multiple_days(self):
        input_string = "MON WED FRI 1600-1700"
        expected = ["MON","WED","FRI","1600-1700"]
        tokens = tokenize(input_string)
        self.assertEqual(len(tokens),len(expected))
        self.assertEqual(tokens,expected)

    def test_day_range(self):
        input_string = "MON-FRI 1600-1700"
        expected = ["MON","-","FRI","1600-1700"]
        tokens = tokenize(input_string)
        self.assertEqual(len(tokens),len(expected))
        self.assertEqual(tokens,expected)

    def test_complex(self):
        input_string ="MON-SAT 0800-1500 12 JAN 2024-14 JAN 2024 0800-1300 10 JAN 1300-1500 10 JAN 2024 1300-1500 MON, 10 JAN 2024 1400-1400 MON, 10 JAN 1400-2300"
        expected = ["MON","-","SAT","0800-1500","12 JAN 2024","-","14 JAN 2024", "0800-1300","10 JAN","1300-1500","10 JAN 2024","1300-1500","MON, 10 JAN 2024","1400-1400","MON, 10 JAN","1400-2300"]
        tokens = tokenize(input_string)
        self.assertEqual(len(tokens),len(expected))
        self.assertEqual(tokens,expected)

         
 
if __name__ == "__main__": 
    unittest.main() 
