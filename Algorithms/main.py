import timeit 
import random
import copy
from insertionSort import insertionSort
from binarySearch import binarySearch
from linearSearch import linearSearch
import dataGen as dataGen 

def Average(arr):
  return sum(arr) / len(arr)
  
# Process Time
def getTime(start):
  endTime= (timeit.default_timer()) - start
  return endTime

# Sorting
def sortArr(arr, type):
  copyArr = copy.deepcopy(arr)
  if type.lower()=="default":
    copyArr.sort(key=lambda var: var.x)
    return copyArr
  
  elif type.lower()=="insertion":
    insertionSort(copyArr)
    return copyArr
  else:
    return("Invalid Selection")

def search(arr, type, value):
  copyArr = copy.deepcopy(arr)
  if type.lower()=="linear":
    return linearSearch(copyArr, value)
  elif type.lower()=="binary":
    return binarySearch(copyArr, value)
  else:
    return("Invalid Selection")
    
# Main Program

#   Data Array Generation
dataSize=20
randomList = dataGen.generateData(dataSize)
print("CURRENT ARRAY:\n\n" + str(randomList))

#   Trials and Timings
type=input("\nPLEASE CHOOSE A SORTING METHOD (Insertion/Default):  ")
numTrials= 10
timesList=[]

print("\nINITIATING TRIALS:")
for i in range(numTrials):
  print("Loop " +str(i+1)+"/" + str(numTrials))
  startTime = timeit.default_timer()
  sortedArray= sortArr(randomList, type)
  timer = getTime(startTime)
  timesList.append(timer)
  print("    Took " + str(timer) + " seconds to run")
print("AVERAGE TRIAL TIME: "+str(Average(timesList))+" SECONDS \n\nSORTED LIST:")
print(sortedArray)

searchingType= input("\nPLEASE ENTER YOUR PREFFERED SEARCHING METHOD: (Linear/Binary)  ")

searchValue = random.choice(randomList)
for i in range(numTrials):
  print("Loop " +str(i+1)+"/" + str(numTrials))
  startTime = timeit.default_timer()
  search(sortedArray, searchingType, searchValue.x)
  timer = getTime(startTime)
  timesList.append(timer)
  print("    Took " + str(timer) + " seconds to run")
print("AVERAGE TRIAL TIME: "+str(Average(timesList))+" SECONDS")
