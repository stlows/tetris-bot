import numpy as np

# Grid size
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Colors
BLACK = (0,0,0)
GREEN = (0, 195, 70)
RED = (195, 0, 0)
BLUE = (0, 122, 195)
PINK = (163, 0, 195)
ORANGE = (195, 140, 0)
YELLOW = (195, 178, 0)
CYAN = (0, 175, 195)

NEXT_BLUE = (0, 67, 127)
NEXT_CYAN = (0, 161, 178)
NEXT_ORANGE = (127, 85, 0)
NEXT_YELLOW = (127, 117, 0)
NEXT_GREEN = (0, 127, 35)
NEXT_PINK =  (106, 0, 127)
NEXT_RED =  (127, 0, 0)

# Pieces points
PIECE_L_POINTS = np.array([[0,2],[1,0],[1,1],[1,2]])
PIECE_S_POINTS = np.array([[0,1],[0,2],[1,0],[1,1]])
PIECE_Z_POINTS = np.array([[0,0],[0,1],[1,1],[1,2]])
PIECE_T_POINTS = np.array([[0,1],[1,0],[1,1],[1,2]])
PIECE_I_POINTS = np.array([[0,0],[0,1],[0,2],[0,3]])
PIECE_J_POINTS = np.array([[0,0],[1,0],[1,1],[1,2]])
PIECE_O_POINTS = np.array([[0,0],[0,1],[1,0],[1,1]])

# Base x
BASE_X = {
  "L":[3,4,3,3],
  "J":[3,4,3,3],
  "S":[3,4], 
  "Z":[3,4],
  "T":[3,4,3,3],
  "I":[3,5],
  "O":[4]
}

# BASE_ROT = {
#   "L":3,
#   "S":0,
#   "Z":0,
#   "T":2,
#   "I":1,
#   "J":1,
#   "O":0
# }


# Rotation
ROT_90 = np.array([[0,-1],[1,0]])
