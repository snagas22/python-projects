"""
Sudoku solver in Python that takes an input of a csv file
and solves the sudoku puzzle
Author: Shun Nagasaki
"""

import sys
import pprint
import csv

class Sudoku_Solver:
  def __init__(self, file):
    # TODO
    self.file = file
    self.grids = []
    pass


  def __read_grid(self, file):
    with open(file, 'r') as f:
      csv_reader = csv.reader(f)
      for r in csv_reader:
        row = [int(x) for x in r]
        self.grids.append(row)
    

  def __is_valid(self, guess, row, col):
    # checking row
    row_vals = self.grids[row]
    if guess in row_vals:
      return False

    # checking column
    col_vals = [self.grids[i][col] for i in range(9)]
    if guess in col_vals:
      return False

    # checking for 3x3 square to make sure there is no overlap
    row_box_idx = (row // 3) * 3
    col_box_idx = (col // 3) * 3

    for i in range(row_box_idx, row_box_idx+3):
      for j in range(col_box_idx, col_box_idx+3):
        if self.grids[i][j] == guess:
          return False

    return True


  def find_empty_cell(self):
    # find an index of the next empty cell
    # return a tuple (None, None) if there isn't one
    for r in range(9):
      for c in range(9):
        if self.grids[r][c] == 0:
          return r, c
    
    return None, None


  def solve(self):
    row, col = self.find_empty_cell()

    if row is None:
      return True
    
    for i in range(1, 10):
      if self.__is_valid(i, row, col):
        self.grids[row][col] = i

        if self.solve():
          return True
      
      self.grids[row][col] = 0
    
    return False
  

  def solve_puzzle(self):
    self.__read_grid(self.file)
    return self.solve()
  

  def print_puzzle(self):
    pprint.pprint(self.grids)
  

def main():
  file = sys.argv[1]
  solver = Sudoku_Solver(file)
  solver.solve_puzzle()
  solver.print_puzzle()


if __name__ == '__main__':
  main()
  

