from pynput.mouse import Button, Controller as MouseController
import time

mouse = MouseController()
sleep = 0.2

def click(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)
    time.sleep(sleep)
#enddef

print ("Current position: " + str(mouse.position))

for i in range (50):
    click(-1137, 67)
    click(-1346, 447)
    click(-1056, 564)
    click(-1407, 507)
    click(-1137, 67)
    click(-1342, 490)
    click(-1832, 63)
    print(i)
