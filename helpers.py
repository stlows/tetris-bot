from constants import *

def centralize(points):
  min_y = points[:,0].min()
  min_x = points[:,1].min()
  
  translate = [0,0]
  if min_y != 0:
    translate[0] = -min_y
  if min_x != 0:
    translate[1] = -min_x

  return np.add(points, translate)

def get_pieces(points):
  max_y = points[:,0].max()
  max_x = points[:,1].max()
  pieces = np.zeros((max_y + 1, max_x + 1))
  for point in points:
    pieces[point[0]][point[1]] = 1
  return pieces