import numpy as np
from constants import *
import math
from Piece import *

class TetrisGrid:

  @classmethod
  def fromImage(cls, im):
    tiles = np.zeros((GRID_HEIGHT, GRID_WIDTH))
    width, height = im.size
    gap = math.floor(width / GRID_WIDTH)
    half_gap = math.floor(gap / 2)
    for y in range(0, GRID_HEIGHT):
      for x in range(0, GRID_WIDTH):
        tile_pos = x * gap + half_gap, y * gap + half_gap
        pix = im.getpixel(tile_pos)
        if pix == BLACK:
          tiles[y][x] = 0
        else:
          tiles[y][x] = 1
    return cls(tiles)

  @classmethod
  def fromArray(cls, tiles):
    return cls(tiles)
  
  @classmethod
  def empty(cls):
    return cls(np.zeros((GRID_HEIGHT, GRID_WIDTH)))

  def __init__(self, tiles):
    self.tiles = np.copy(tiles)

  def drop_rotation(self, rotation, x):
    delta_y = 0
    pieces_coord_on_board = np.add([delta_y, x], rotation.points)
    while not self.is_intercepting_or_out_of_bound(pieces_coord_on_board):
      delta_y += 1
      pieces_coord_on_board = np.add([delta_y, x], rotation.points)
    delta_y -= 1
    pieces_coord_on_board = np.add([delta_y, x], rotation.points)
    new_grid = TetrisGrid.fromArray(np.copy(self.tiles))
    for point in pieces_coord_on_board:
      new_grid.tiles[point[0]][point[1]] = 1
    return new_grid
  
  def best_move(self, piece):
    best = 0, 0, 10 ** 20
    for i, rotation in enumerate(piece.rotations):
      for x in range(GRID_WIDTH - rotation.width + 1):
        try_board = self.drop_rotation(rotation, x)
        try_board.remove_full_line()
        value = try_board.value()
        if value < best[2]:
          best = x, i, value
        #print("Trying (x = " + str(x) + ", rot = " + str(i) + ")" + ", Value = " + str(value))
    return best

  def value(self):

    lines_sums = np.sum(self.tiles, axis = 1)
    power_of_tens = [10**(19-i) for i in range(20)]
    lines_values = np.multiply(lines_sums, power_of_tens)
    lines_value = np.sum(lines_values)
    
    heighest = math.floor(math.log10(lines_value)) if lines_value > 0 else 0
    columns = [self.tiles[:,i] for i in range(10)]
    hole_value = 0
    for column in columns:
      for i in range(20):
        if column[i] == 1:
          if np.sum(column[i:]) != 20 - i:
            hole_value += 10 ** (heighest + 2)
            break
      else:
        continue
      break
    value = lines_value + hole_value
    return value

  def remove_full_line(self):
    removed = 0
    for i in range(self.tiles.shape[0]):
      if self.tiles[i].all():
        removed += 1
        self.tiles = np.delete(self.tiles, i, 0)
        new_row = np.zeros((1, GRID_WIDTH))
        self.tiles = np.append(new_row, self.tiles, axis=0)
    return removed

  def is_intercepting_or_out_of_bound(self, board_points):
    for point in board_points:
      if point[0] > GRID_HEIGHT - 1:
        return True
      if self.tiles[point[0]][point[1]] != 0:
        return True
    return False
    