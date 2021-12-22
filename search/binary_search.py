"""
Binary search algorithm for a sorted array

Author: Shun Nagasaki
"""

def binary_search(array, target):
  low = 0
  high = len(array)-1

  while(low <= high):
    mid = (low+high)//2
    if array[mid] == target:
      return True
    else:
      if target > array[mid]:
        low = mid+1
      else:
        high = mid-1
  
  return False

def main():
  # sample runs of the function
  print(binary_search([1,2,3,5,8], 6))
  print(binary_search([1,2,3,5,6,8], 5))
