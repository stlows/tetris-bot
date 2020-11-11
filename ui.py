import keyboard
import time
from constants import *
from Piece import *
import pyautogui

delay = 0.02

def rotate_right(n = 1):
  print("Rotating right", n)
  for i in range(n):
    keyboard.send("Up")
    time.sleep(delay)

def rotate_left(n = 1):
  print("Rotating left", n)
  for i in range(n):
    keyboard.send("z")
    time.sleep(delay)

def move_left(n = 1):
  print("Moving left", n)
  for i in range(n):
    keyboard.send("Left")
    time.sleep(delay)

def move_right(n = 1):
  print("Moving right", n)
  for i in range(n):
    keyboard.send("Right")
    time.sleep(delay)

def hold():
  print("Holding")
  keyboard.send("c")
  time.sleep(delay)

def drop():
  print("Dropping")
  keyboard.send("space")
  time.sleep(delay)

def make_move(piece, x, rotation, fast_drop = True):
  if rotation == 3:
    rotate_left()
  else:
    rotate_right(rotation)

  base_x = BASE_X[piece.name][rotation]
  if x > base_x:
    move_right(x - base_x)
  if x < base_x:
    move_left(base_x - x)
  if fast_drop:
    drop()

def get_falling(gamezone_screenshot):
  falling_color = gamezone_screenshot.getpixel((329, 50))
  falling_piece = None
  if falling_color == GREEN: falling_piece = PieceS
  if falling_color == RED: falling_piece = PieceZ
  if falling_color == BLUE: falling_piece = PieceJ
  if falling_color == PINK: falling_piece = PieceT
  if falling_color == ORANGE: falling_piece = PieceL
  if falling_color == YELLOW: falling_piece = PieceO
  if falling_color == CYAN: falling_piece = PieceI
  return falling_piece

def get_next_piece(gamezone_screenshot):
  next_pixel = (595,112)
  next_piece = None
  next_color = gamezone_screenshot.getpixel(next_pixel)
  if next_color == NEXT_GREEN: next_piece = PieceS
  if next_color == NEXT_RED: next_piece = PieceZ
  if next_color == NEXT_BLUE: next_piece = PieceJ
  if next_color == NEXT_PINK: next_piece = PieceT
  if next_color == NEXT_ORANGE: next_piece = PieceL
  if next_color == NEXT_YELLOW: next_piece = PieceO
  if next_color == NEXT_CYAN: next_piece = PieceI
  return next_piece

def get_second_next_piece(gamezone_screenshot):
  next_pixel = (595,180)
  next_piece = None
  next_color = gamezone_screenshot.getpixel(next_pixel)
  if next_color == NEXT_GREEN: next_piece = PieceS
  if next_color == NEXT_RED: next_piece = PieceZ
  if next_color == NEXT_BLUE: next_piece = PieceJ
  if next_color == NEXT_PINK: next_piece = PieceT
  if next_color == NEXT_ORANGE: next_piece = PieceL
  if next_color == NEXT_YELLOW: next_piece = PieceO
  if next_color == NEXT_CYAN: next_piece = PieceI
  return next_piece

