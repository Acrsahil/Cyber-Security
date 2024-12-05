import os
import pyautogui
import time


def on_move(x, y):
    os.system("ls")
    print(f"current position of x is {x} and y is {y} ")


prev_x, prev_y = pyautogui.position()
while True:
    current_x, current_y = pyautogui.position()

    if current_x != prev_x or current_y != prev_y:
        on_move(current_x,current_y)  # Call the function to print "Hello"
        prev_x, prev_y = current_x, current_y  # Update the previous position
    time.sleep(0.1)
