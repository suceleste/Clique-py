from pynput.mouse import Controller, Button
from time import sleep

mouse = Controller()

def Click(x, y, DG=True):
    """x et y sont les coordonné et DG correspond au clique droit(True) et gauche(False)"""
    mouse.position = (x, y)
    if DG == True :
        mouse.press(Button.right)
        sleep(0.2)
        mouse.release(Button.right)
    else :
        mouse.press(Button.left)
        sleep(0.2)
        mouse.release(Button.left)

