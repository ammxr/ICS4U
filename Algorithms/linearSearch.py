def linearSearch(arr, l, n):
  for i in range(0,l):
    if arr[i] == n:
      return ("Index is at " + str(i))
test = [1,3,6,74,8,23,4]
l= len(test)
n=6
run= linearSearch(test,l,n)
print(run)