from helpers import *
class Rotation:
  def __init__(self, points, name):
    self.points = points
    self.pieces = get_pieces(self.points)
    self.height, self.width = self.pieces.shape
    self.name = name
  def __str__(self):
    return self.name + " (" + str(self.height) + "x" + str(self.width) + ")"
    