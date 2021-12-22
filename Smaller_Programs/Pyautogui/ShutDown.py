import pyautogui as pg
import time

pg.hotkey("winleft", "x")
for x in range(2):
    pg.keyDown("u")
    pg.keyUp("u")

time.sleep(8)

pg.keyDown("Shift")
for x in range(2):
    pg.keyDown("tab")
    pg.keyUp("tab")

pg.press("enter")

# tab is 'tab' 
# shift is 'shift'