'''
Created on Aug 27, 2011

@author: House of T
'''

from __future__ import division
from Tkinter import Tk

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

class Paddle:
    def __init__(self,color="#ffffff"):
        self.WIDTH =  screen_width / 100
        self.HEIGHT = screen_height / 20
        self.COLOR = color
        
    