#568,398
#y difference 270
import pyautogui
#x difference
from PIL import ImageOps,ImageGrab
import time

game_cords = (76,143,1063,675)
def grab_game():
    image = ImageGrab.grab(game_cords)
    return (image)

def grayscale(image):
    GS = ImageOps.grayscale(image)
    print(GS)
    return GS

def maain():
    all = grayscale(grab_game())
    return all
