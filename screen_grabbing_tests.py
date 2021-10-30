import keyboard  # using module keyboard
import mss
import mss.tools

import multiprocessing
import sys
import time
import pyautogui


with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    #mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    #print(output)
    cnt = 30
    while cnt>0:  # making a loop
        print("going left")
        pos = pyautogui.position() 
        pyautogui.moveTo(pos[0] + 20, pos[1],0.2)
        time.sleep(1)
        print("going right")
        pos = pyautogui.position() 
        pyautogui.moveTo(pos[0] - 20 , pos[1],0.2)
        time.sleep(1)
        cnt = cnt - 1
        
        # keyboard.send('s')
        # time.sleep(1)
                    #pass

    # cnt = 0
    # while True:  # making a loop
    #     if keyboard.is_pressed('q'):  # if key 'q' is pressed 
    #         print('You Pressed A Key! {}'.format(cnt))
    #         cnt = cnt +1
    #         time.sleep(0.1)
    #         keyboard.send('w')
    #         #break  # finishing the loop
    #     else:
    #         print('You Pressed Another Key! {}'.format(cnt))
    #         if cnt > 0 :
    #             cnt = cnt  - 1
    #         time.sleep(0.1)
    #                 #pass

    #     # Grab the data
    #         sct_img = sct.grab(monitor)

    #         # Save to the picture file
    #         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    #         print(output)
