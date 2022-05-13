def insertionSort(arr):
  i = 0
  for i in range(len(arr)):
    temp = arr[i]
    j = i
    while(j>0  and temp.x < arr[j-1].x):
          arr[j] = arr[j-1]
          j-= 1
    arr[j] = temp