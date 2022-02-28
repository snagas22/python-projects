"""
Solution to Contiguous Subarrays practice problem on Meta Recruiting Website
url: https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=226517205173943&ppid=454615229006519&practice_plan=1

Author: Shun Nagasaki
"""


import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

# probably not efficient enough
def count_subarrays(arr):
  # Write your code here
  ret = []
  for i in range(len(arr)):
    curr = 1
    # starts with arr[i]
    
    for j in range(i+1, len(arr)):
      if arr[i] >= arr[j]:
        curr += 1
      else:
        break
    # ends with arr[i]
    for j in range(i-1, -1, -1):
      if arr[i] >= arr[j]:
        curr += 1
      else:
        break
    
    ret.append(curr)
  
  return ret


# more efficient
def count_subarrays_2(arr):
  n = len(arr)
  res = [1] * n
  stack = [-1]
  #left
  for i in range(n):
    while len(stack) > 1 and arr[stack[-1]] < arr[i]:
      stack.pop()
    res[i] += i - stack[-1] - 1
    stack.append(i)

  # from right
  stack = [n]
  for i in range(n - 1, -1, -1):
    while len(stack) > 1 and arr[stack[-1]] < arr[i]:
      stack.pop()
    res[i] += stack[-1] - i - 1
    stack.append(i)
  return res


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  