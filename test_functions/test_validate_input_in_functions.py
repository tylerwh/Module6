import unittest

from more_functions import validate_input_in_functions as validate_input


class TestFunction(unittest.TestCase):
  def test_score_input_test_name(self):
    test_name = "Tyler"
    self.assertEqual(validate_input.score_input(test_name), "Tyler: 0")
  

  def test_score_input_test_score_valid(self):
    test_name = "Tyler"
    score = 90
    self.assertEqual(validate_input.score_input(test_name, score), "Tyler: 90")
  

  def test_score_input_test_score_below_range(self):
    test_name = "Tyler"
    under_score = -50
    self.assertEqual(validate_input.score_input(test_name, under_score), "Invalid test score, try again!")
  

  def test_score_input_test_score_above_range(self):
    test_name = "Tyler"
    over_score = 115
    self.assertEqual(validate_input.score_input(test_name, over_score), "Invalid test score, try again!")
  

  def test_test_score_non_numeric(self):
    test_name = "Tyler"
    non_numeric_score = "$$"
    self.assertEqual(validate_input.score_input(test_name, non_numeric_score), ValueError)
  

  def test_score_input_invalid_message(self):
    test_name = "Tyler"
    score = -1
    message = "Test Message"
    self.assertEqual(validate_input.score_input(test_name, score, message), message)


if __name__ == "__main__":
    unittest.main()
