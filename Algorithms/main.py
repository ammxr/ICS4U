# function in function
import time
import random
import copy
from insertionSort import insertionSort

# Process Time
startTime = time.time()
def getTime(start):
  endTime= (time.time()) - startTime
  print("    Took " + str(endTime) + " seconds to run")

# Random List Setup
def getRandomList(listSize):
  randomList = [0] * listSize
  for j in range(listSize):
    randomList[j] = round(random.random() * listSize)
  return randomList

# Data Array Generation
dataSize=20
randomList = getRandomList(dataSize)
print(str(randomList))
# Sorting
def sortArr(arr, type):
  if type.lower()=="default":
    return arr.sort()
  elif type.lower()=="insertion":
    return insertionSort(arr)
  else:
    return("Invalid Selection")

#  Main Program
type=input("What sort would you like to run? ")
sortArr(randomList, type)

# Number of Trials
numTrials= 10
for i in range(numTrials):
  print("Loop #" +str(i+1)+" out of " + str(numTrials))
  randomList = getRandomList(dataSize)
  timer = getTime()
