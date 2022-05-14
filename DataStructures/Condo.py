from VacationStay import VacationStay

class Condo(VacationStay):
  '''
    Condo object with parameters number, floorNumber, stories, rooms, bathrooms, and area
    
    Attributes
    ----------
    number : int
	    Unit number for booking housing
    floorNumber : int
      Floor number of Condo
    stories : int 
      Amount of stories of booked condo
    rooms : int
	    Amount of rooms in housing 
    bathrooms : int
	    Amount of bathrooms in housing
    area : int
      Area (square feet) of condo
    
    Methods
    -------
    getPricePerNight() -> float
	    Returns price per night for rent Airbnb
  '''
  def __init__(self, number, floorNumber, stories, rooms, bathrooms, area):
    '''
    Constructor to build Condo object
    
    Parameters
	  ----------
    number : int
	    Unit number for Condo (inherited)
    floorNumber : int
      Floor number of Condo
    stories : int 
      Amount of stories
    rooms : int
	    Amount of rooms in Condo 
    bathrooms : int
	    Amount of bathrooms in Condo
    '''
    super().__init__(number, rooms, bathrooms)
    self.stories = stories
    self.floorNumber = floorNumber
  def getPricePerNight(self):
    '''
  	Returns the price per night (rent)
  	Returns
  	-------
  	Price per night (float)
  	'''
    self.pricePerNight = 369.99 * (self.rooms)
    return(self.pricePerNight)
