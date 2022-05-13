def linearSearch(arr,value):
  for i in range(len(arr)):
    if arr[i].x== value:
      print("VALUE FOUND AT INDEX " + str(i) + " \n  COORDINATE: " + str(arr[i]))
      break