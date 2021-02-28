# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:00:14 2021

@author: Анастасия
"""

dicti_str = "UUU F      CUU L      AUU I       GUU V UUC F      CUC L      AUC I      GUC V UUA L      CUA L      AUA I      GUA V  UUG L      CUG L      AUG M      GUG V UCU S      CCU P      ACU T      GCU A UCC S      CCC P      ACC T      GCC A UCA S      CCA P      ACA T      GCA A UCG S      CCG P      ACG T      GCG A UAU Y      CAU H      AAU N      GAU D UAC Y      CAC H      AAC N      GAC D UAA Stop   CAA Q      AAA K      GAA E UAG Stop   CAG Q      AAG K      GAG E UGU C      CGU R      AGU S      GGU G UGC C      CGC R      AGC S      GGC G UGA Stop   CGA R      AGA R      GGA G UGG W      CGG R      AGG R      GGG G "
b = 1
combi = ""
ami = ""
nuc = 0
d = {}

for i in dicti_str:
    if (i==' '):
        if (b == 0):
            d[combi] = ami
            b = 1
            combi = ""
            ami = ""
        continue
    if (b == 1):
        if (nuc < 3):
            combi += i
            nuc += 1 
        elif (nuc == 3):
            b = 0
            nuc = 0
    if (b == 0):
        ami += i

print(d)
        
nucposl = input()
k = 0
n = ""
amiposl = ""
for i in nucposl:
    if (k<3):
        n += i
        k += 1
        continue
    k = 1
    amiposl += d[n]
    print(n)
    n = i
    
print(amiposl)



