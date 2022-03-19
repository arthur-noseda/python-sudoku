import unittest
from sudoku.functions import check_rows, check_cols, check_regions, check_sudoku, naked_single

class TestSudoku(unittest.TestCase):

  def test_rows_should_be_valid(self):
    self.assertTrue(check_rows([[9, 6, 3, 1, 7, 4, 2, 5, 8],
                                [1, 7, 8, 3, 2, 5, 6, 4, 9],
                                [2, 5, 4, 6, 8, 9, 7, 3, 1],
                                [8, 2, 1, 4, 3, 7, 5, 9, 6],
                                [4, 9, 6, 8, 5, 2, 3, 1, 7],
                                [7, 3, 5, 9, 6, 1, 8, 2, 4],
                                [5, 8, 9, 7, 1, 3, 4, 6, 2],
                                [3, 1, 7, 2, 4, 6, 9, 8, 5],
                                [6, 4, 2, 5, 9, 8, 1, 7, 3]]))

  def test_rows_should_not_be_valid(self):
    self.assertFalse(check_rows([[9, 6, 3, 1, 7, 4, 2, 5, 8],
                                 [1, 7, 8, 3, 2, 5, 6, 4, 9],
                                 [2, 5, 4, 6, 8, 9, 7, 3, 1],
                                 [8, 2, 1, 4, 3, 7, 5, 9, 6],
                                 [4, 9, 6, 8, 4, 2, 3, 1, 7],
                                 [7, 3, 5, 9, 6, 1, 8, 2, 4],
                                 [5, 8, 9, 7, 1, 3, 4, 6, 2],
                                 [3, 1, 7, 2, 4, 6, 9, 8, 5],
                                 [6, 4, 2, 5, 9, 8, 1, 7, 3]]))

  def test_cols_should_be_valid(self):
    self.assertTrue(check_cols([[9, 6, 3, 1, 7, 4, 2, 5, 8],
                                [1, 7, 8, 3, 2, 5, 6, 4, 9],
                                [2, 5, 4, 6, 8, 9, 7, 3, 1],
                                [8, 2, 1, 4, 3, 7, 5, 9, 6],
                                [4, 9, 6, 8, 5, 2, 3, 1, 7],
                                [7, 3, 5, 9, 6, 1, 8, 2, 4],
                                [5, 8, 9, 7, 1, 3, 4, 6, 2],
                                [3, 1, 7, 2, 4, 6, 9, 8, 5],
                                [6, 4, 2, 5, 9, 8, 1, 7, 3]]))

  def test_cols_should_not_be_valid(self):
    self.assertFalse(check_cols([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                 [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                 [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                 [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                 [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                 [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                 [7, 8, 5, 1, 2, 3, 4, 9, 6],
                                 [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                 [9, 1, 2, 3, 4, 5, 6, 7, 8]]))

  def test_regions_should_be_valid(self):
    self.assertTrue(check_regions([[9, 6, 3, 1, 7, 4, 2, 5, 8],
                                   [1, 7, 8, 3, 2, 5, 6, 4, 9],
                                   [2, 5, 4, 6, 8, 9, 7, 3, 1],
                                   [8, 2, 1, 4, 3, 7, 5, 9, 6],
                                   [4, 9, 6, 8, 5, 2, 3, 1, 7],
                                   [7, 3, 5, 9, 6, 1, 8, 2, 4],
                                   [5, 8, 9, 7, 1, 3, 4, 6, 2],
                                   [3, 1, 7, 2, 4, 6, 9, 8, 5],
                                   [6, 4, 2, 5, 9, 8, 1, 7, 3]]))

  def test_regions_should_not_be_valid(self):
    self.assertFalse(check_regions([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                   [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                   [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                   [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                   [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                   [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                   [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                   [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                   [9, 1, 2, 3, 4, 5, 6, 7, 8]]))

  def test_sudoku_should_be_valid(self):
    self.assertTrue(check_sudoku([[9, 6, 3, 1, 7, 4, 2, 5, 8],
                                 [1, 7, 8, 3, 2, 5, 6, 4, 9],
                                 [2, 5, 4, 6, 8, 9, 7, 3, 1],
                                 [8, 2, 1, 4, 3, 7, 5, 9, 6],
                                 [4, 9, 6, 8, 5, 2, 3, 1, 7],
                                 [7, 3, 5, 9, 6, 1, 8, 2, 4],
                                 [5, 8, 9, 7, 1, 3, 4, 6, 2],
                                 [3, 1, 7, 2, 4, 6, 9, 8, 5],
                                 [6, 4, 2, 5, 9, 8, 1, 7, 3]]))

  def test_sudoku_should_not_be_valid(self):
    self.assertFalse(check_sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                   [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                   [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                   [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                   [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                   [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                   [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                   [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                   [9, 1, 2, 3, 4, 5, 6, 7, 8]]))

  def test_should_solve_sudoko(self):
    self.assertEqual(naked_single([[4, 0, 3, 0, 9, 6, 0, 1, 0],
                                   [0, 0, 2, 8, 0, 1, 0, 0, 3],
                                   [0, 1, 0, 0, 0, 0, 0, 0, 7],
                                   [0, 4, 0, 7, 0, 0, 0, 2, 6],
                                   [5, 0, 7, 0, 1, 0, 4, 0, 9],
                                   [1, 2, 0, 0, 0, 3, 0, 8, 0],
                                   [2, 0, 0, 0, 0, 0, 0, 7, 0],
                                   [7, 0, 0, 2, 0, 9, 8, 0, 0],
                                   [0, 6, 0, 1, 5, 0, 3, 0, 2]]),
                                 (True, [[4, 7, 3, 5, 9, 6, 2, 1, 8],
                                         [6, 5, 2, 8, 7, 1, 9, 4, 3],
                                         [9, 1, 8, 3, 2, 4, 5, 6, 7],
                                         [3, 4, 9, 7, 8, 5, 1, 2, 6],
                                         [5, 8, 7, 6, 1, 2, 4, 3, 9],
                                         [1, 2, 6, 9, 4, 3, 7, 8, 5],
                                         [2, 9, 5, 4, 3, 8, 6, 7, 1],
                                         [7, 3, 1, 2, 6, 9, 8, 5, 4],
                                         [8, 6, 4, 1, 5, 7, 3, 9, 2]]))

  def test_fail_to_solve_sudoku(self):
    self.assertEqual(naked_single([[0, 0, 6, 0, 4, 0, 1, 0, 0],
                                   [0, 5, 0, 0, 9, 0, 0, 6, 0],
                                   [8, 0, 0, 0, 0, 0, 0, 0, 5],
                                   [0, 0, 0, 3, 0, 4, 0, 0, 0],
                                   [3, 1, 0, 0, 0, 0, 0, 4, 8],
                                   [0, 0, 0, 8, 0, 7, 0, 0, 0],
                                   [6, 0, 0, 0, 0, 0, 0, 0, 9],
                                   [0, 2, 0, 0, 3, 0, 0, 5, 0],
                                   [0, 0, 1, 0, 5, 0, 7, 0, 0]]),
                                  (False, None))

if __name__ == '__main__':
  unittest.main()