#-----------------------------------------------------------------------------
# Name:        AirBnB Booking (Data structures) 
# Purpose:     To provide class structure and reusability in a environment of AirBnB booking sample.
#				
#
# Author:      Ammar Hakim
# Created:     30-Mar-2022
# Updated:     09-Apr-2022
#-----------------------------------------------------------------------------

import random
import json
from datetime import date

from VacationStay import VacationStay
from House import House
from Condo import Condo

today = date.today()
date = today.strftime("%m/%d/%y")
dashBreak=("-----------------\n")

# Welcome to Service (AirBnB)
print("Hi and welcome to our Airbnb service!\n\nTo get started please enter your legal name (signature) to sign to terms of service: ")
firstName= input("First Name: ")
lastName= input("Last Name: ")

# Write to clientForm.json
clientInfo={
  "First Name": firstName,
  "Last Name" : lastName,
  "Date of Issue" : date
}
for i in clientInfo:
  with open ("clientForm.json", "r") as f:
    clientForm=json.load(f)
    clientName=str((clientForm["First Name"])+" "+(clientForm["Last Name"]))
  clientForm[i] = clientInfo[i]
  with open ("clientForm.json", "w") as f:
    json.dump (clientForm, f, indent=4)

# Base Parameters (Parent Class)
rooms= int(input("\nHow many rooms do you require? "))
stories = random.randint(1,3)
print(dashBreak)
print("Sounds great! Your suite will be " + str(stories)+" stories tall and have " + str(rooms) + " rooms")

print("\nWe currently have the available options as either a House or a Condominium:")
houseOrCondo= input("Which would you like? ")

# Parameter Setup for Condominium
if houseOrCondo.lower() == "condo" or houseOrCondo.lower() == "condominium":
  addressNumber= int(str(random.randint(1, 9))+str(random.randint(1, 9))+str(random.randint(1, 9))+str(random.randint(1, 9)))
  floorNumber= random.randint(1,15)
  print(dashBreak)
  print("Perfect! You're Condo number is " + str(addressNumber)+ " and is located on the "+ str(floorNumber) +" floor")
  bathroomsNeeded= input("\nFinally, How many bathrooms would you require? (1-4)")
  bathrooms=int(bathroomsNeeded)
  
  # Parent Class
  stay= VacationStay(addressNumber, rooms, bathrooms)
  area=stay.getArea()
  
  # Inheritance to Child Class 
  stayChosen= Condo(addressNumber, floorNumber, stories, rooms, bathrooms, area)
  cost= stayChosen.getPricePerNight()
  print("It will cost $" +str(cost) +" per night for you're booking")
  print(dashBreak)
  
  print("It is recommended that the booking is for no greater than " +str(stayChosen.getPeopleRecommended()) +" people")
  
# Write to Condo Reciept file (vacationInformation.json)
  jsonWritesCondo={
  "Client Name": clientName,
  "Cost ($)/Night" : cost,
  "Unit Number": addressNumber,
  "Floor Number": floorNumber,
  "Rooms": rooms,
  "Bathrooms": bathrooms,
  "Stories": stories,
  "Area (square feet)": area
}
  with open ("vacationInformation.json", "w") as f:
    json.dump (jsonWritesCondo, f, indent=4)


  
elif houseOrCondo.lower() == "house":
  addressNumber= int(str(random.randint(1, 9))+str(random.randint(1, 9))+str(random.randint(1, 9))+str(random.randint(1, 9)))

  houseType= input("Would you like to rent a detatched or single detatched house? ")
  if houseType.lower()=="single detatched":
    type="Single Detatched"
  elif houseType.lower()=="detatched":
    type="Detatched"
  
  bathroomsNeeded= input("Finally, How many bathrooms would you require? (1-4)")
  bathrooms=int(bathroomsNeeded)

  print(dashBreak)
  # Parent Class
  stay= VacationStay(addressNumber, rooms, bathrooms)
  area=stay.getArea()
  
  # Inheritance to Child Class   
  stayChosen= House(addressNumber, type, stories, rooms, bathrooms, area)
  cost= stayChosen.getPricePerNight()
  print("It will cost $" +str(cost) +" per night for you're booking")

# Write to House Reciept file (vacationInformation.json)
  jsonWritesHouse={
  "Client Name": clientName,
  "Cost ($)/Night" : cost,
  "Unit Number": addressNumber,
  "Type": type,
  "Rooms": rooms,
  "Bathrooms": bathrooms,
  "Stories": stories,
  "Area (square feet)": area
  }
  with open ("vacationInformation.json", "w") as f:
    json.dump (jsonWritesHouse, f, indent=4)

# On Error (House or Condo not selected)
else:
  print("Invalid Input (Program Ended) ")

print("Thanks for booking with us!!! You may find you're booking information in the vacationInformation.json receipt")