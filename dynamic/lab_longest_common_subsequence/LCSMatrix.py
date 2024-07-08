
class LCSMatrix:
  def __init__(self, str1, str2):
    self.row_count = len(str1)
    self.col_count = len(str2)
    self.str1 = str1
    self.str2 = str2
    self.matrix = None

    # add one to the end of the matrix to provide a base case for dynamic programming
    matrix = [[0 for _ in range(self.row_count+ 1)] for _ in range(self.col_count + 1)]
    self.matrix = matrix

    self.matrix = self.get_longest_common_subsequences

    self.print_matrix

  def get_column_count(self):
      return self.col_count

  def get_row_count(self):
      return self.row_count

  def get_entry(self, row, col):
    if row < 0 or col < 0: return 0 
    else: return self.matrix[row][col]
  
  def get_longest_common_subsequences(self):

    # iterate
    for row in range(self.row_count):
      for col in range(self.col_count):
          up_left = 0
          if self.str1[row] == self.str2[col]:
            up_left = self.get_entry(row, col)
            self.matrix[col][row] = 1 + up_left

          else:
            self.matrix[row][col] = max(self.get_entry(row - 1,col), self.get_entry(row, col - 1))

    return self.matrix
  
  def print_matrix(self):
    print()
    for row in self.matrix:
      print(row)