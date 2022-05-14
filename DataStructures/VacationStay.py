class VacationStay:
  '''
    VacationStay object with parameters number, rooms, and bathrooms
    Attributes
    ----------
    number : int
	    Unit number for booking housing 
    rooms : int
	    Amount of rooms in housing 
    bathrooms : int
	    Amount of bathrooms in housing
    Methods
    -------
    getArea() -> int
	    Returns area value determined by ratio in relation to rooms 
    getPeopleRecommended() -> int
	    Returns recommended maximum for comfortable experience based off area (square feet).
  '''
  def __init__(self, number, rooms, bathrooms):
    '''
    Constructor to build a vacationStay object
    Parameters
	  ----------
	  number : int
		  Unit number of booking
	  rooms : int
		  Number of rooms of booking
	  bathrooms : int
		  Number of bathrooms in booking
    '''
    self.number = number
    self.rooms = rooms
    self.bathrooms = bathrooms
    self.area = 100*rooms
  def getArea(self):
    '''
    Returns the area of the booked unit
    Returns
    -------
    Area of the booked unit
    '''
    return self.area
  def getPeopleRecommended(self):
    '''
  	Returns the recomended maximum per booked unit
  	Returns
  	-------
  	Recomended maximum per booked unit (int)
  	'''
    return (int(self.area)//50)