# Linear search O(n)
def linearSearch(arr,target):
  target = 6
  for i in range(len(arr)):
    if arr[i]== target:
      return i
  return -1

# Binary search O(log n)
def binarySearch(arr, target):
  low = 0
  high = len(arr)-1
  mid = (high+low)/2
  while low != high:
    if (target == arr[mid]):
      return mid
    elif (target<mid):
      high = mid
      mid = (high+low)/2
    else:
      low = mid
      mid = (high+low)/2
  return -1