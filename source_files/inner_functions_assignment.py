"""
Author: Tyler Hochstetler
The purpose of this program is to practice creating and calling inner functions. 
"""


def measurements(meas_list):
  """Receive a list of measurements for a rectangle and return a string with the perimeter and area."""
  
  
  def area(meas_list):
    """Calculates the area"""
    calculated_area = meas_list[0] * meas_list[1]
    return calculated_area


  def perimeter(meas_list):
    """Calculates the perimeter"""
    calculated_perimeter = meas_list[0] * 2 + meas_list[1] * 2
    return calculated_perimeter
  

  area = str(area(meas_list))
  perimeter = str(perimeter(meas_list))

  return "Perimeter = " + perimeter + " Area = " + area


if __name__ == "__main__":
    pass