# Binary search O(log n)
def binarySearch(arr, value):
  low = 0
  high = len(arr)-1
  while low != high:
    mid = int((high + low) // 2)
    if (value == arr[mid]):
      print("Value found at index " + str(mid))
      break
    elif (value<mid):
      high = mid
      mid = (high+low)/2
    elif value not in arr:
      print("Value does not exist within array")
      break
    else:
      low = mid
      mid = (high+low)/2
