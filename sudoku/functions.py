def check_rows(grid):
  numbers = range(1, 10)
  for row in grid:
    for number in numbers:
      if number not in row:
        return False
  return True

def check_cols(grid):
  transposed = [
    [
      row[i] for row in grid
    ]
    for i in range(9)
  ]
  return check_rows(transposed)

def check_regions(grid):
  regions = [
    [
      grid[k + 3 * i][l + 3 * j]
      for k in range(3) for l in range(3)
    ]
    for i in range(3) for j in range(3)
  ]
  return check_rows(regions)

def check_sudoku(grid):
  return check_rows(grid) and check_cols(grid) and check_regions(grid)

def naked_single(grid):
  prev_count = _count_zeros(grid)
  while True:
    for i in range(9):
      for j in range(9):
        if grid[i][j] == 0:
          values = {
            grid[i][k] for k in range(9) if k != j and grid[i][k] != 0
          } | {
            grid[k][j] for k in range(9) if k != i and grid[k][j] != 0
          } | {
            grid[i // 3 * 3 + k][j // 3 * 3 + l]
            for k in range(3)
            for l in range(3)
            if i // 3 * 3 + k != i
                and j // 3 * 3 + l != j
                and grid[i // 3 * 3 + k][j // 3 * 3 + l] != 0
          }
          if len(values) == 8:
            grid[i][j] = sum(range(1, 10)) - sum(values)
    count = _count_zeros(grid)
    if count == 0:
      return (True, grid)
    elif count == prev_count:
      return (False, None)
    else:
      prev_count = count


def _count_zeros(grid):
  return len([grid[i][j] for i in range(9) for j in range(9) if grid[i][j] == 0])
