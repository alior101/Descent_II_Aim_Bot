#!/bin/bash
d2x-rebirth -window -nomovies -pilot lior -nosound -nomusic -maxfps 60 &
sleep 3
D2R=`xdotool search --onlyvisible --name d2x`
echo $D2R
xdotool getwindowgeometry $D2R
xdotool windowmove $D2R 0 0 
sudo  /home/lior/anaconda3/bin/python3 main.py
