from helpers import *
from constants import *
from Rotation import *

class Piece:
  def __init__(self, points, number_of_rotations, name):
    self.points = points
    self.number_of_rotations = number_of_rotations
    self.name = name
    self.rotations = self.get_all_rotations()
  def get_all_rotations(self):
    rotations = []
    temp = self.points
    for i in range(self.number_of_rotations):
      rotations.append(Rotation(temp,self.name + str(i*90)))
      temp = centralize(temp.dot(ROT_90))
    return rotations
  def __str__(self):
    return self.name
# Pieces
PieceL = Piece(PIECE_L_POINTS, 4, "L")
PieceS = Piece(PIECE_S_POINTS, 2, "S")
PieceZ = Piece(PIECE_Z_POINTS, 2, "Z")
PieceT = Piece(PIECE_T_POINTS, 4, "T")
PieceI = Piece(PIECE_I_POINTS, 2, "I")
PieceJ = Piece(PIECE_J_POINTS, 4, "J")
PieceO = Piece(PIECE_O_POINTS, 1, "O")
PIECES = [PieceL, PieceS, PieceZ, PieceT, PieceI, PieceJ, PieceO]