# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:12:39 2021

@author: Анастасия
"""

line = input()
pair=line.split()

mon=int(pair[0])
liv=int(pair[1])
gen=[0 for i in range(liv-1)]


un = 1

for i in range(mon-1):
    f=un
    tot=0
    for i in gen:
        tot+=i
    un=tot
    for i in range(liv-2,0,-1):
        gen[i] = gen[i-1]
    gen[0]=f 
    print(un, gen)
    
tota=0
for i in gen:
    tota+=i
print(tota+un)