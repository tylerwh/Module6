import unittest
from more_functions import string_functions


class TestFunctions(unittest.TestCase):


  def test_multiple_string(self):
    result = "TylerTylerTylerTyler"
    self.assertEqual(string_functions.multiply_string("Tyler", 4), result)


if __name__ == "__main__":
    unittest.main()