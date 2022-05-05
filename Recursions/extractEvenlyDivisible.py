#  Author: Ammar Hakim
import random

def extractEvenlyDivisible(numList,n):
  # Helper function works off new array while keeping count off original
  def helper(newArray=[]):
   
    # If the array is not provided return nothing
    if (len(numList))==0:
      numList.sort()
      return newArray
    
    # Else if the array first item is divisible by number (n) 
    elif numList[0] % n==0:
      newArray.append(numList[0])
      numList.pop(0)
      return helper(newArray)
  
    #  If not divisible then remove item from reference list (numList)
    else:
      numList.pop(0)
      return helper(newArray)
  return helper()


#  Array Input generated using random - For efficiency opposed to using manual inputs per number. 
inputArray=input("Would you like test using a randomly generated array count? (Yes/No) ")
if inputArray.lower()=="yes":
  randomlist = []
  for i in range(0,10):
    randNum = random.randint(1,100)
    randomlist.append(randNum)
  usedArray=randomlist  
elif inputArray.lower()=="no":
  usedArray=[1,2,3,4,5,6,7,8,9]
  print("Ok proceeding with test case array: " + str(usedArray))
else:
  print("Response was invalid exiting program...")

#  Divisor Input
inputDivisor=input("What would you like to divide by? (Integer number only) ")
try:
  int(inputDivisor)%1 == 0
  usedDivisor=int(inputDivisor)
except:
  print("Divisor value is invalid... Exiting program")


#  Final Results
print("\n Your input array was: \n" + "    " +str(usedArray) + "\n Divided by: \n" + "    "+ str(usedDivisor) + "\n Here were the applicable numbers:" + "    " + str(extractEvenlyDivisible(usedArray,usedDivisor)))