# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:42:57 2018

@author: E. Handford
"""

print ("hello world!")

x = []
t = 1
a = 1
b = 1
c = 1
fin = 1

while c<4000000:

    c = (a + b)
    a = b
    b = c
   
    if c%2 == 0 :
        x.extend([c])
    print (x)
 




fin = sum(x)

print (fin)

    
    
    

