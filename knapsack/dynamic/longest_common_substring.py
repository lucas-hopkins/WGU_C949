

def find_longest_common_substring(string_1, string_2):
  
  # build initial matrix with all 0s
  matrix = []
  for row in range(len(string_1)):
    a = []
    for col in range(len(string_2)):
      a.append(0)
    matrix.append(a)

  # compare the letter in the row / col indexes
  # if they are the same, set upLeft to 0
  # otherwise  as long as the row and col are greater than 0
  # set upLeft to matrix value at index one left and one up from the curre
  # position
  # increment the current matrix position by one
  for row in range(len(string_1)):
    for col in range(len(string_2)):
      if string_1[row] == string_2[col]:
        upLeft = 0
        if row > 0 and col > 0:
          upLeft = matrix[row - 1][col - 1]
        
        matrix[row][col] = 1 + upLeft
      
      else:
        matrix[row][col] = 0
  
  
  for row in matrix:
    print(row)



find_longest_common_substring("Look", "zyBooks")

