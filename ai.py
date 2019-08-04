
#difference  = 566
import pyautogui
from grab import game_cords



def ai(image):
    con = 0
    while con == 0:
        for y in range(177):
            for x in range(84):
                loc1 = (5*x,y*3)
                loc2 = (5*x+566,y*3)
                first_one = image.getpixel(loc1)
                second_one = image.getpixel(loc2)
                if first_one - second_one>10 or first_one-second_one<-10 :
                    pyautogui.click(loc1[0]+game_cords[0],loc1[1]+game_cords[1])
                    con+=1




