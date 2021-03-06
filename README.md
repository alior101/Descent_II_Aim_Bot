# Descent_II_Aim_Bot

![image](https://user-images.githubusercontent.com/3033580/139537451-f6f2562d-baac-4ef6-9102-4ce7a089a0d4.png)

This repo holds the files used to create a small AI assisted aiming bot for Descent II game.
Descent II is an old (1996) FPS game for DOS. Since it has many fans (including myself) it has a linux port with full multiplayer functionality.
The 6 DOF of the ship is a perfect opportunity to test a small AI object detection as a human enemies detection/location/aim/shoot assistance.
It's not a perfect aim/shoot bot by not means.. The target was to show how to quickly build a simple AI bot... 
The pytorch ipynb is based on https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb 

Instructions:
1. Install d2x-rebirth and xdotool (the game and the utility to locate the windowed game at a spcific screen location for python screen grabing function) 
2. install pytorch mss pyautogui pandas torch torchvision torchaudio opencv-python tqdm matplotlib seaborn under *root* permission (since screen capture needs su)
3. run ./run.sh
4. The python script captures images with enemies in a local folder some time after a detection is done (I used it to augement the training samples of ennemies at differnt scales and rotations and improve the detection quality) 



The training images are at https://app.roboflow.com/descent-aimhelperbot/descentii-small/3 - images were captured with a screen capture utility and uploaded for quick manual anotation on Roboflow.
![image](https://user-images.githubusercontent.com/3033580/139537647-fa658be8-9d09-4a81-b7fa-6d0fe349db05.png)

Training script Custom_Yolo5_With_Descent_Images.ipynb was done on colab 

The training dashboard is public at https://wandb.ai/alior101/YOLOv5/runs/3cyh8daj?workspace=user-alior101 
![image](https://user-images.githubusercontent.com/3033580/139537603-c1ccde11-18d9-41e9-932b-061911b08225.png)

![image](https://user-images.githubusercontent.com/3033580/139537619-7e7e7a7f-80f3-4dc5-94e3-87441aa30332.png)
Model achieved ~0.9 mAP with almost 1 R and P!  

Running it on actual game screen show a very good detection..  
![image](https://user-images.githubusercontent.com/3033580/139537569-e3609d52-d66b-4077-af34-d9ce59b58ef5.png)

