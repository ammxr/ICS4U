#  Author: Ammar Hakim

#  Functions
def doubleCountdown(n):
  def helper(n):
    if n ==0:
      return 0
    else:
      print(n)
      return(helper(n-1))
  helper(n)
  return helper(n-1)

#  Main Program
n=int(input("Please enter a POSITIVE integer which you would like to begin your count: "))

print(doubleCountdown(n))