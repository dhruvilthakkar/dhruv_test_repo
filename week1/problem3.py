# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:14:34 2017

@author: dhru4670
"""

s='azcbobobegghakl'
subs=''
curr=''
l=[]

for char in s:
    if not curr or char >= curr[-1]:
        curr += char
    else:
        curr, subs = '', max(curr, subs, key=len)

print(curr)
#print("Longest substring in alphabetical order is:",subs)