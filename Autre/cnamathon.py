from pynput.mouse import Button, Controller as MouseController
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#1-Star (734, 524) 5-Star(823,524)
for i in range (50):
    click(1495,54)
    time.sleep(0.5)
    click(1275,423)
    time.sleep(0.5)
    click(823, 524)
    time.sleep(0.5)
    click(1495,54)
    time.sleep(0.5)
    click(1307,482)
    time.sleep(0.5)
    click(89, 47)
    time.sleep(3)