# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:47:03 2024

@author: Pratiksha
"""

from tkinter import *
from time import strftime

root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title('Python Digital Clock Application')


def time():
    string = strftime('%I:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)

mark = Label(root,
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'black')

mark.pack(anchor = 'center')
time()

mainloop()