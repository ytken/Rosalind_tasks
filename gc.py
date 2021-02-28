# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:05:47 2021

@author: Анастасия
"""

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

def gccontent(seq, d):
    cgkol = 0
    for i in seq:
        if (i=='C') or (i=='G'):
            cgkol += 1
    return round(((cgkol)*100)/(len(seq)-d), 6)

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
f = open(filename, 'r')
num=0
cur=0
cgmax=0
name=""
namemax=""
curseq=""
delta=0

for x in f:
    if (x[0]==">"):
        if curseq != "":
            cur = gccontent(curseq, delta)
            if (cur > cgmax):
                cgmax = cur
                namemax=name
            print(curseq[:10]," ",cgmax)
            curseq=""
            delta = 0
        name=x
        print(x)
        continue
    curseq += x
    delta += 1
    
cur = gccontent(curseq, delta)
if (cur > cgmax):
    cgmax = cur
    namemax=name
print(curseq[:10]," ",cgmax)


print(namemax[1:])
print(cgmax)