#!/usr/bin/env python

'''
Created on Aug 27, 2011

@author: House of T
'''

from Tkinter import Tk
import Paddle, Ball

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

class Game:
    def __init__(self):
        self.player_paddle = Paddle()
        self.comp_paddle = Paddle()
        self.ball = Ball()
        

if __name__ == "__main__":
    pass