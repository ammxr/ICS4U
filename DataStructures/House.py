from VacationStay import VacationStay

class House(VacationStay):
  '''
    House object with parameters number, type, stories, rooms, bathrooms, area
    
    Attributes
    ----------
    number : int
	    Unit number for house
    type : int
      Floor number of Condo
    stories : int 
      Amount of stories of booked house
    rooms : int
	    Amount of rooms in house 
    bathrooms : int
	    Amount of bathrooms in house
    area : int
      Area  (square feet) of House
    
    Methods
    -------
    getPricePerNight() -> float
	    Returns price per night for rent Airbnb
  '''
  def __init__(self, number, type, stories, rooms, bathrooms, area):
    '''
    Constructor to build Condo object
    
    Parameters
	  ----------
    number : int
	    Unit number for house
    type : int
      Floor number of Condo
    stories : int 
      Amount of stories of booked house
    rooms : int
	    Amount of rooms in house 
    bathrooms : int
	    Amount of bathrooms in house
    area : int
      Area  (square feet) of House
    '''
    super().__init__(number, rooms, bathrooms)
    self.stories = stories
    self.type = type
  def getPricePerNight(self):
    '''
  	Returns the price per night (rent)
  	Returns
  	-------
  	Price per night (float)
  	'''
    self.pricePerNight = 199.99 * int(self.rooms)
    return(self.pricePerNight)