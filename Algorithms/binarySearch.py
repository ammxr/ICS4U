# Binary search O(log n)
def binarySearch(arr, value):
  low = 0
  high = len(arr)-1
  while low != high:
    mid = int((high + low) // 2)
    if (value == arr[mid]):
      return mid
    elif (value<mid):
      high = mid
      mid = (high+low)/2
    else:
      low = mid
      mid = (high+low)/2
  return -1
