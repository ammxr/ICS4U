def linearSearch(arr,value):
  for i in range(len(arr)):
    if arr[i].x== value:
      print("Value found at index " + str(i))
      break
