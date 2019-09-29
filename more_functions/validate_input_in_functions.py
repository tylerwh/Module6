"""
Author: Tyler Hochstetler
The purpose of this program is to practice passing arguments to functions.
"""


def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
  """ This function takes the above parameters, validates them, then returns a concatenated test_name and test_score
  :param test_name: required, name to be used
  :param test_score: default is 0, but can take a number as an argument 
  :param invalid_message: this displays if user inputs the incorrect number
  :returns: the test_name and test_score concatenated together
  """
  # return {test_name: test_score}
  return test_name + ": " + str(test_score)


if __name__ == "__main__":
  pass
