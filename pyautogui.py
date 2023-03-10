#！/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui
import time
import os
import sys
import subprocess


# move mouse
def move_mouse(x, y):
    pyautogui.moveTo(x, y, duration=0.5)

# click mouse
def click_mouse(x, y):
    pyautogui.click(x, y)

# double click mouse
def double_click_mouse(x, y):
    pyautogui.doubleClick(x, y)

# right click mouse
def right_click_mouse(x, y):
    pyautogui.rightClick(x, y)

def main():
    # move mouse
    move_mouse(100, 100)
    # click mouse
    click_mouse(100, 100)
    # double click mouse
    double_click_mouse(100, 100)
    # right click mouse
    right_click_mouse(100, 100)

if __name__ == '__main__':
    main()

