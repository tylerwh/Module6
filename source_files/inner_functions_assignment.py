"""
Author: Tyler Hochstetler
The purpose of this program is to practice creating and calling inner functions. 
"""


def measurements(meas_list):
  """Receive a list of measurements for a rectangle and return a string with the perimeter and area.
  :param area: stores the area of the calculated meas_list as a string
  :param perimeter: stores the perimeter of the calculated meas_list as a string
  :returns: string providing the calculated perimeter and area
  """
  
  
  def area(meas_list):
    """Calculates the area
    :param calculated_area: calculates the area using the provided list
    :returns: calculated_area as a number type
    """
    if len(meas_list) < 2:
      calculated_area = meas_list[0] * meas_list[0]
    else:
      calculated_area = meas_list[0] * meas_list[1]
    return calculated_area


  def perimeter(meas_list):
    """Calculates the perimeter
    :param calculated_perimeter: calculates the perimeter of the provided list
    :returns: calculated_perimeter as a number type
    """
    if len(meas_list) < 2:
      calculated_perimeter = meas_list[0] * 4
    else:
      calculated_perimeter = meas_list[0] * 2 + meas_list[1] * 2
    return calculated_perimeter
  

  # Call the two inner methods and cast the results as strings
  area = str(area(meas_list))
  perimeter = str(perimeter(meas_list))

  # return {"Perimeter = " + perimeter + " Area = " + area}
  return "Perimeter = " + perimeter + " Area = " + area


if __name__ == "__main__":
    pass