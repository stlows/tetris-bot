import unittest
import numpy as np
from Piece import *
from TetrisGrid import *
from PIL import Image

class TetrisTests(unittest.TestCase):

  def test_value_empty_board(self):
    board = TetrisGrid.empty()
    value = board.value()
    self.assertEqual(0, value)

  def test_best_move(self):
    board = TetrisGrid.empty()
    board.tiles[19][0] = 1
    board.tiles[19][1] = 1
    board.tiles[19][2] = 1
    board.tiles[19][3] = 1
    board.tiles[19][6] = 1
    board.tiles[19][7] = 1
    board.tiles[19][8] = 1
    board.tiles[19][9] = 1

    # S
    best_x, best_rotation, best_value = board.best_move(PieceS)
    self.assertEqual(best_x, 4)
    self.assertEqual(best_rotation, 0)
    self.assertEqual(best_value, 2)
    board = board.drop_rotation(PieceS.rotations[best_rotation], best_x)
    board.remove_full_line()
    # I
    best_x, best_rotation, best_value = board.best_move(PieceI)
    self.assertEqual(best_x, 0)
    self.assertEqual(best_rotation, 0)
    self.assertEqual(best_value, 6)
    board = board.drop_rotation(PieceI.rotations[best_rotation], best_x)
    board.remove_full_line()

    # L
    best_x, best_rotation, best_value = board.best_move(PieceL)
    self.assertEqual(best_x, 7)
    self.assertEqual(best_rotation, 0)
    self.assertEqual(best_value, 19)
    board = board.drop_rotation(PieceL.rotations[best_rotation], best_x)
    board.remove_full_line()

    # T
    best_x, best_rotation, best_value = board.best_move(PieceT)
    self.assertEqual(best_x, 3)
    self.assertEqual(best_rotation, 2)
    self.assertEqual(best_value, 4)
    board = board.drop_rotation(PieceT.rotations[best_rotation], best_x)
    board.remove_full_line()

    # S
    best_x, best_rotation, best_value = board.best_move(PieceS)
    self.assertEqual(best_x, 1)
    self.assertEqual(best_rotation, 0)
    self.assertEqual(best_value, 26)
    board = board.drop_rotation(PieceS.rotations[best_rotation], best_x)
    board.remove_full_line()

    # Z
    best_x, best_rotation, best_value = board.best_move(PieceZ)
    self.assertEqual(best_x, 5)
    self.assertEqual(best_rotation, 0)
    self.assertEqual(best_value, 48)
    board = board.drop_rotation(PieceZ.rotations[best_rotation], best_x)
    board.remove_full_line()

  def test_board_value(self):
    board = TetrisGrid.empty()
    board.tiles[19][0] = 1
    board.tiles[19][1] = 1
    board.tiles[19][2] = 1
    board.tiles[19][3] = 1
    board.tiles[18][5] = 1
    board.tiles[18][6] = 1
    board.tiles[18][7] = 1
    board.tiles[18][8] = 1
    board.tiles[18][9] = 1
    self.assertEqual(1054, board.value())



  def test_remove_multiple_lines(self):
    board = TetrisGrid.empty()
    
    board.tiles[19][4] = 1
    board.tiles[19][5] = 1
    board.tiles[19][7] = 1
    board.tiles[19][8] = 1
    for i in range(10):
      board.tiles[18][i] = 1
    for i in range(10):
      board.tiles[17][i] = 1
    for i in range(10):
      board.tiles[16][i] = 1
    board.tiles[15][0] = 1
    board.tiles[15][2] = 1
    board.tiles[15][7] = 1

    board.remove_full_line()
    self.assertEqual((20,10), board.tiles.shape)
    self.assertEqual(0, board.tiles[19][0])
    self.assertEqual(1, board.tiles[18][0])
    self.assertEqual(1, board.tiles[18][2])
    self.assertEqual(1, board.tiles[19][4])
    self.assertEqual(1, board.tiles[19][5])
    for i in range(10):
      self.assertEqual(0, board.tiles[17][i])

  def test_remove_a_line(self):
    board = TetrisGrid.empty()
    for i in range(10):
        board.tiles[19][i] = 1
    board.tiles[18][4] = 1
    board.tiles[18][5] = 1
    board.tiles[17][4] = 1

    board.remove_full_line()
    self.assertEqual((20,10), board.tiles.shape)
    self.assertEqual(0, board.tiles[19][0])
    self.assertEqual(1, board.tiles[18][4])
    self.assertEqual(0, board.tiles[18][5])
    self.assertEqual(1, board.tiles[19][4])
    self.assertEqual(1, board.tiles[19][5])

  def test_new_empty_board(self):
    board = TetrisGrid.empty()
    self.assertEqual((20,10), board.tiles.shape)

  def test_board_drop(self):
    board = TetrisGrid.empty()

    board = board.drop_rotation(PieceI.rotations[1], 0)
    self.assertEqual(1, board.tiles[19][0])
    self.assertEqual(1, board.tiles[18][0])
    self.assertEqual(1, board.tiles[17][0])
    self.assertEqual(1, board.tiles[16][0])

    board = board.drop_rotation(PieceO.rotations[0], 1)
    self.assertEqual(1, board.tiles[19][1])
    self.assertEqual(1, board.tiles[18][2])
    self.assertEqual(1, board.tiles[19][2])
    self.assertEqual(1, board.tiles[18][1])

    board = board.drop_rotation(PieceT.rotations[1], 0)
    self.assertEqual(1, board.tiles[15][0])
    self.assertEqual(1, board.tiles[14][0])
    self.assertEqual(1, board.tiles[13][0])
    self.assertEqual(1, board.tiles[14][1])

    board = board.drop_rotation(PieceS.rotations[0], 3)
    self.assertEqual(1, board.tiles[19][3])
    self.assertEqual(1, board.tiles[19][4])
    self.assertEqual(1, board.tiles[18][4])
    self.assertEqual(1, board.tiles[18][5])

    board = board.drop_rotation(PieceZ.rotations[0], 6)
    self.assertEqual(1, board.tiles[18][6])
    self.assertEqual(1, board.tiles[18][7])
    self.assertEqual(1, board.tiles[19][7])
    self.assertEqual(1, board.tiles[19][8])

    board = board.drop_rotation(PieceL.rotations[3], 8)
    self.assertEqual(1, board.tiles[17][8])
    self.assertEqual(1, board.tiles[17][9])
    self.assertEqual(1, board.tiles[18][9])
    self.assertEqual(1, board.tiles[19][9])

    board = board.drop_rotation(PieceJ.rotations[3], 5)
    self.assertEqual(1, board.tiles[17][5])
    self.assertEqual(1, board.tiles[17][6])
    self.assertEqual(1, board.tiles[16][6])
    self.assertEqual(1, board.tiles[15][6])

    board = board.drop_rotation(PieceT.rotations[2], 4)
    self.assertEqual(1, board.tiles[14][4])
    self.assertEqual(1, board.tiles[14][5])
    self.assertEqual(1, board.tiles[14][6])
    self.assertEqual(1, board.tiles[15][5])

    board = board.drop_rotation(PieceZ.rotations[1], 7)
    self.assertEqual(1, board.tiles[17][7])
    self.assertEqual(1, board.tiles[16][7])
    self.assertEqual(1, board.tiles[16][8])
    self.assertEqual(1, board.tiles[15][8])

    board = board.drop_rotation(PieceI.rotations[0], 1)
    self.assertEqual(1, board.tiles[13][1])
    self.assertEqual(1, board.tiles[13][2])
    self.assertEqual(1, board.tiles[13][3])
    self.assertEqual(1, board.tiles[13][4])

  def test_new_board_from_image(self):
    board_image = Image.open('board.png')
    board = TetrisGrid.fromImage(board_image)
    self.assertEqual(1, board.tiles[19][0])
    self.assertEqual(1, board.tiles[18][0])
    self.assertEqual(0, board.tiles[17][0])
    self.assertEqual(0, board.tiles[16][0])
    self.assertEqual(1, board.tiles[15][0])
    self.assertEqual(1, board.tiles[14][0])

    self.assertEqual(1, board.tiles[19][3])
    self.assertEqual(0, board.tiles[18][3])
    self.assertEqual(1, board.tiles[17][3])
    self.assertEqual(0, board.tiles[16][3])

  def test_piece_I(self):
    rotations = PieceI.rotations
    self.assertEqual(2, len(rotations))

    self.assertEqual(1, rotations[1].width)
    self.assertEqual(4, rotations[1].height)
    np.testing.assert_array_equal(np.array([[1],[1],[1],[1]]), rotations[1].pieces)

    self.assertEqual(4, rotations[0].width)
    self.assertEqual(1, rotations[0].height)
    np.testing.assert_array_equal(np.array([[1, 1, 1, 1]]), rotations[0].pieces)
  
  def test_piece_T(self):
    rotations = PieceT.rotations
    self.assertEqual(4, len(rotations))

    self.assertEqual(3, rotations[2].width)
    self.assertEqual(2, rotations[2].height)
    np.testing.assert_array_equal(np.array([[1,1,1],[0,1,0]]), rotations[2].pieces)

    self.assertEqual(2, rotations[3].width)
    self.assertEqual(3, rotations[3].height)
    np.testing.assert_array_equal(np.array([[0,1],[1,1],[0,1]]), rotations[3].pieces)

    self.assertEqual(3, rotations[0].width)
    self.assertEqual(2, rotations[0].height)
    np.testing.assert_array_equal(np.array([[0,1,0],[1,1,1]]), rotations[0].pieces)

    self.assertEqual(2, rotations[1].width)
    self.assertEqual(3, rotations[1].height)
    np.testing.assert_array_equal(np.array([[1,0],[1,1],[1,0]]), rotations[1].pieces)
  
  def test_piece_L(self):
    rotations = PieceL.rotations
    self.assertEqual(4, len(rotations))

    self.assertEqual(2, rotations[1].width)
    self.assertEqual(3, rotations[1].height)
    np.testing.assert_array_equal(np.array([[1,0],[1,0],[1,1]]), rotations[1].pieces)

    self.assertEqual(3, rotations[2].width)
    self.assertEqual(2, rotations[2].height)
    np.testing.assert_array_equal(np.array([[1,1,1],[1,0,0]]), rotations[2].pieces)

    self.assertEqual(2, rotations[3].width)
    self.assertEqual(3, rotations[3].height)
    np.testing.assert_array_equal(np.array([[1,1],[0,1],[0,1]]), rotations[3].pieces)

    self.assertEqual(3, rotations[0].width)
    self.assertEqual(2, rotations[0].height)
    np.testing.assert_array_equal(np.array([[0,0,1],[1,1,1]]), rotations[0].pieces)

  def test_piece_J(self):
    rotations = PieceJ.rotations
    self.assertEqual(4, len(rotations))

    self.assertEqual(2, rotations[3].width)
    self.assertEqual(3, rotations[3].height)
    np.testing.assert_array_equal(np.array([[0,1],[0,1],[1,1]]), rotations[3].pieces)

    self.assertEqual(3, rotations[0].width)
    self.assertEqual(2, rotations[0].height)
    np.testing.assert_array_equal(np.array([[1,0,0],[1,1,1]]), rotations[0].pieces)

    self.assertEqual(2, rotations[1].width)
    self.assertEqual(3, rotations[1].height)
    np.testing.assert_array_equal(np.array([[1,1],[1,0],[1,0]]), rotations[1].pieces)

    self.assertEqual(3, rotations[2].width)
    self.assertEqual(2, rotations[2].height)
    np.testing.assert_array_equal(np.array([[1,1,1],[0,0,1]]), rotations[2].pieces)
  
  def test_piece_S(self):
    rotations = PieceS.rotations
    self.assertEqual(2, len(rotations))

    self.assertEqual(3, rotations[0].width)
    self.assertEqual(2, rotations[0].height)
    np.testing.assert_array_equal(np.array([[0,1,1],[1,1,0]]), rotations[0].pieces)

    self.assertEqual(2, rotations[1].width)
    self.assertEqual(3, rotations[1].height)
    np.testing.assert_array_equal(np.array([[1,0],[1,1],[0,1]]), rotations[1].pieces)

  def test_piece_Z(self):
    rotations = PieceZ.rotations
    self.assertEqual(2, len(rotations))

    self.assertEqual(3, rotations[0].width)
    self.assertEqual(2, rotations[0].height)
    np.testing.assert_array_equal(np.array([[1,1,0],[0,1,1]]), rotations[0].pieces)

    self.assertEqual(2, rotations[1].width)
    self.assertEqual(3, rotations[1].height)
    np.testing.assert_array_equal(np.array([[0,1],[1,1],[1,0]]), rotations[1].pieces)
  
  def test_piece_O(self):
    rotations = PieceO.rotations
    self.assertEqual(1, len(rotations))

    self.assertEqual(2, rotations[0].width)
    self.assertEqual(2, rotations[0].height)
    np.testing.assert_array_equal(np.array([[1,1],[1,1]]), rotations[0].pieces)
    

if __name__ == '__main__':
    unittest.main()