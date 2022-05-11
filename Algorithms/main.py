# function in function
import time
import random
import copy
from insertionSort import insertionSort
from binarySearch import binarySearch
from linearSearch import linearSearch

def Average(arr):
    return sum(arr) / len(arr)
  
# Process Time
def getTime(start):
  endTime= (time.time()) - start
  print("    Took " + str(endTime) + " seconds to run")
  return endTime

# Random List Setup
def getRandomList(listSize):
  randomList = [0] * listSize
  for j in range(listSize):
    randomList[j] = round(random.random() * listSize)
  return randomList

# Sorting
def sortArr(arr, type):
  if type.lower()=="default":
    return arr.sort()
  elif type.lower()=="insertion":
    return insertionSort(arr)
  else:
    return("Invalid Selection")

def search(arr, type, value):
  if type.lower()=="linear":
    return linearSearch(arr, value)
  elif type.lower()=="binary":
    return binarySearch(arr, value)
  else:
    return("Invalid Selection")
    
# Main Program
    
#   Data Array Generation
dataSize=20
randomList = getRandomList(dataSize)
print(str(randomList))

#   Trials and Timings
type=input("What sort would you like to run? ")
numTrials= 10
timesList=[]

for i in range(numTrials):
  print("Loop #" +str(i+1)+" out of " + str(numTrials))
  randomList = getRandomList(dataSize)
  startTime = time.time()
  sortArr(randomList, type)
  timer = getTime(startTime)
  timesList.append(timer)
print('\n')
print("The average time was "+str(Average(timesList)))
print(randomList)

searchingType= input("What type of searching will you conduct? ")
searchValue = int(input("What value are you searching? "))
search(randomList, searchingType, searchValue)
