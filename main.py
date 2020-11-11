import pyautogui
import time
from PIL import Image
import math
import numpy as np
from constants import *
from TetrisGrid import *
from Piece import *
import ui
import keyboard
#pyautogui.displayMousePosition()

save_images = False


resume_btn = pyautogui.locateOnScreen('resume_btn.png')
if resume_btn != None:
  center = pyautogui.center(resume_btn)
  pyautogui.click(center)
  region = (608,287,680,570)
  if save_images:
    gamezone_screenshot = pyautogui.screenshot("gamezone_init.png",region=region)
  else:
    gamezone_screenshot = pyautogui.screenshot(region=region)
  hold_piece = ui.get_next_piece(gamezone_screenshot)
  falling_piece = ui.get_second_next_piece(gamezone_screenshot)
  print("Init state:")
  print("Hold: ", hold_piece)
  print("Falling: ", falling_piece)
  time.sleep(2.5)
  ui.hold()
  can_switch = False
  board = TetrisGrid.empty()
  counter = 0

  while True:
    time.sleep(0.2)
    if save_images:
      gamezone_screenshot = pyautogui.screenshot("gamezone" + str(counter) + ".png",region=region)
    else:
      gamezone_screenshot = pyautogui.screenshot(region=region)
    next_piece = ui.get_next_piece(gamezone_screenshot)

    print("--- " + str(counter) + " ---")
    print("Hold: ", hold_piece)
    print("Falling: ", falling_piece)
    print("Next: ", next_piece)
 
    best = board.best_move(falling_piece)
    hold_best = board.best_move(hold_piece)

    if hold_best[2] < best[2] and can_switch:
      print("Hold is better then falling")
      ui.hold()
      time.sleep(0.2)
      best = hold_best
      temp = falling_piece
      falling_piece = hold_piece
      hold_piece = temp
    
    best_x, best_rotation, best_value = best
    print("Best: ", falling_piece.name, "x = ", best_x, " | rot = ", best_rotation)

    ui.make_move(falling_piece,best_x,best_rotation, fast_drop = True)
    can_switch = True
    board = board.drop_rotation(falling_piece.rotations[best_rotation], best_x)
    removed = board.remove_full_line()
    
    time.sleep(0.3 + 0.1 * (removed - 1))
    falling_piece = next_piece
    counter += 1


  


