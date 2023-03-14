# -*- coding: utf8 -*-

def triangle(a, b, c):
    #print(c**2)
    #print(a**2)
    #print(b**2)
    if (c**2)==(a**2+b**2): 
        return True
    else: 
        return False

#print(triangle(3,4,5))
#print(triangle(3,4,20))
#print(triangle(3,4,1))