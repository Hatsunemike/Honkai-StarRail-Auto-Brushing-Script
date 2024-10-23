# Honkai: Star Rail auto brushing script

## Description

Only support auto-brushing in 侵蚀隧洞(Artifact gaining).

## Features

1. Start a new battle automatically when previous battle finishes.
2. Automatically use Reserved Trailblaze Power 40 per each when the Trailblaze Power isn't enough.

## Environments

1. Python environments

   packages needed: `Numpy`,`opencv-python`,`pyautogui`,`pillow`

## How to use

1. Set the environment.

   You can use `Anaconda` to create a independent environment.

2. Update the `.png` file by screenshots that have your own device's resolution ratio.

   Due to the accuracy needing, the script use template-matching algorithm to find the button and symbols on the screen, so the matching result won't consider the scale change.It's necessary for you to give the pictures which have precise scales.

3. Open a shell/cmd **in Administrator Mode** to run the script `main.py`

4. Run the game, and start the battle.

   It's recommended to keep full-screen in order to avoid the button sheltering from another window. Of course, if you are familiar with the valuable region, you can do it selectively.