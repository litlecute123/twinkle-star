# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:06:54 2018

@author: L1592
"""

from math import*
def s(x,N):
    n=1
    a=1
    s=0
    while n<=N:
        s=s+a
        a=-x**2/(2*n*(2*n-1))*a
        n+=1
    return s
print(s(radians(60),100))  