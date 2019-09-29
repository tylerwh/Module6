import unittest
from source_files import inner_functions_assignment as inner_func 


class MyTestCase(unittest.TestCase):
  
  def test_measurements_rectangle(self):
    test_list = [2.1, 3.4]
    self.assertEqual(inner_func.measurements(test_list), "Perimeter = 11.0 Area = 7.14")
  

  def test_measurements_square(self):
    test_list = [3.5]
    self.assertEqual(inner_func.measurements(test_list), "Perimeter = 14.0 Area = 12.25")


if __name__ == "__main__":
    unittest.main()