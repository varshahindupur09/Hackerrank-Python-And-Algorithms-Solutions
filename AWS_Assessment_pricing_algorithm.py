# AWS Assessment Question 1: 
# determining the number of adjustments needed to ensure that the Amazon pricing algorithm yields the same price for the sums of all subarrays of the length k within the array prod_price.
from collections import Counter

def getMinimumChanges(n: int, prod_price: list, k: int):
  # whenever there is a selection of subarray from array usually it ends up having %k where k would be the length of k as 0%2=0,1%2=1,2%2=0,3%2=1... similarly 0%3=0,1%3=1,2%3=2,3%3=0,4%3=1,5%3=2...
  groups = [[] for _ in range(k)]
  modifications = 0
  
  for i in range(n):
    groups[i%k].append(prod_price[i]) #0,1,0,1 group

  for grp in groups:
    counter = Counter(grp) # how many duplicates in a group
    max_freq = max(counter.values())
    changes += len(grp) - max_freq
    
  return changes
  

# # Sample Case 0
# n = 4
# prod_price = [1, 3, 1, 3]
# k = 2
# print(getMinimumChanges(n, prod_price, k))  # Output: 0
# print()

# # Sample Case 1
# n = 5
# prod_price = [1, 3, 2, 2, 3]
# k = 3
# print(getMinimumChanges(n, prod_price, k)) #Output:1
# print()

# # Sample Case 2
# n = 4
# prod_price = [5, 7, 7, 3] #Output:2
