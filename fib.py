# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:24:14 2021

@author: Анастасия
"""

pair = input().split()
mon = int(pair[0])
fam = int(pair[1])

un = 1
pr = 0

for i in range(mon-1):
    f = un
    un = pr*fam
    pr += f
    
print(un+pr)