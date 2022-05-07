import time
import random
import copy
from insertionSort import insertionSort

# Process Time
startTime = time.time()
def getTime():
  endTime= (time.time()) - startTime
  print("The process took " + str(endTime) + " seconds to run")

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

#  Main Program

# Number of Trials
numTrials= 10
for i in range(numTrials):
  print("Loop #" +str(i+1)+" out of " + str(numTrials))
  randomList = getRandomList(dataSize)
  t = getTime()
  t2 = getTime(randomList, "defaultSort")
  timesDefault[i] = t2
