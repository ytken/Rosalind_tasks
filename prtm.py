# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:55:00 2021

@author: Анастасия
"""

dicti="A   71.03711 C   103.00919 D   115.02694 E   129.04259 F   147.06841 G   57.02146 H   137.05891 I   113.08406 K   128.09496 L   113.08406 M   131.04049 N   114.04293 P   97.05276 Q   128.05858 R   156.10111 S   87.03203 T   101.04768 V   99.06841 W   186.07931 Y   163.06333 "

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
f = open(filename, 'r')

key = ""
wei = {}
for line in f.read().splitlines():
    paa = line.split()
    wei[paa[0]] = float(paa[1])

seq = input()
sum = 0
for i in seq:
    sum += wei[i]
print(round(sum,3))