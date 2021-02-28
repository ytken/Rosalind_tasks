# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:59:15 2021

@author: Анастасия
"""

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
f = open(filename, 'r')

key = ""
seqs = {}
for line in f.read().splitlines():
    if line[0] == '>':
        key = line
    else:
        seqs[key] = line
        
list_d = list(seqs.items())

for i in list_d:
    sta = i[1][:3:]
    end = i[1][-3::]
    for j in list_d[list_d.index(i):]:
        staj = j[1][:3:]
        endj = j[1][-3::]
        if endj == sta and i[0]!=j[0]:
            print(j[0][1:], i[0][1:])
        if staj == end and i[0]!=j[0]:
            print(i[0][1:], j[0][1:])


        

