import keyboard  # using module keyboard
import mss
import mss.tools

import multiprocessing
import sys
import time
import pyautogui
import torch
from PIL import Image

# some inital values 
timeout = 0
enemy_detected = False

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt')  # default
pyautogui.moveTo(320,240,0)

with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 0, "left": 0, "width": 640, "height": 480}

    # Grab the data
    while True: 
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        results = model(img)
        #pyautogui.moveTo(320,240,0)

        # this timer will be usefull to implement a delay 
        # after an enemy detection to cause another screen grabbing 
        # and increasing the trainign set 
        if timeout>0:
            timeout = timeout - 1

        # Results
        #results.print()
        if results.xywh[0].shape[0]>0:
            # certaintly
            cert = results.xywh[0][0][4]
            print("**** Enemy detected with certainty of {}****".format(cert))
            if cert > 0.7:
                print(results.xywh[0])  # img1 predictions (tensor)
                enemy_pos = results.xywh[0]
                pos = pyautogui.position() 
                enemy_x_pos = enemy_pos[0][0] + int(enemy_pos[0][2]/2)
                enemy_y_pos = enemy_pos[0][1] + int(enemy_pos[0][3]/2)
                print("Enemy is at {},{}".format(enemy_x_pos, enemy_y_pos))
                delta_x = (enemy_x_pos - 320)/4
                delta_y = (enemy_y_pos - 240)/4
                pyautogui.moveTo(pos[0] + delta_x, pos[1] - delta_y ,0.2)
                time.sleep(0.1)
                print("Shooting at it...")
                keyboard.press("ctrl")
                time.sleep(0.1)
                keyboard.release("ctrl")
                pyautogui.moveTo(320,240,0.2)

                # if detected an enemy, wait few moments 
                # then cpature another image
                # this will add other occurences of enemies and will
                # increase the training set quality
                enemy_detected = True
                timeout = 0 

            if enemy_detected == True and timeout == 0:
                output = "d2x_enemy_{}.png".format(str(int(time.time())))
                mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
                enemy_detected = False

            # this will gibve me an option to capture additional ennemies 
            # and increase the quality of the training set
            if keyboard.is_pressed('c'): 
                print("Saving undetected enemy")
                output = "d2x_enemy_other_{}.png".format(str(int(time.time())))
                mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
