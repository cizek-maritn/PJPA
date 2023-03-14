#!/bin/env python
# -*- coding: utf-8 -*-

def is_convex(a, b, c, d):
    #flase pokud se nejedna o ctyruhlnik
    if (a==b) or (a==c) or (a==d) or (b==c) or (b==d) or (c==d):
        return False

    #tvorba vektoru, vektor jde z smerem z prvniho pismena do druheho
    AB=(b[0]-a[0], b[1]-a[1])
    BC=(c[0]-b[0], c[1]-b[1])
    CD=(d[0]-c[0], d[1]-c[1])
    DA=(a[0]-d[0], a[1]-d[1])
    #print(AB)
    #print(BC)
    #print(CD)
    #print(DA)

    #vektorovy soucin
    cA=(AB[1]*(-DA[0]))-(AB[0]*(-DA[1]))
    cB=(BC[1]*(-AB[0]))-(BC[0]*(-AB[1]))
    cC=(CD[1]*(-BC[0]))-(CD[0]*(-BC[1]))
    cD=(DA[1]*(-CD[0]))-(DA[0]*(-CD[1]))
    #print(c1)
    #print(c2)
    #print(c3)
    #print(c4)
    #print("next")

    #pokud jsou smery vsech vektorovych soucinu stejne, ctyruhelnik je konvexni
    if (cA>0) and (cB>0) and (cC>0) and (cD>0):
        return True
    elif (cA<=0) and (cB<=0) and (cC<=0) and (cD<=0):
        return True
    else:
        return False


if __name__ == '__main__':
    is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))

#nepovedlo se mi rozchodit pytest
#print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)))
#print(is_convex((-1.0, -1.0), (1.0, -1.0), (1.0, 1.0), (-1.0, 1.0)))
#print(is_convex((0.0, 0.0), (1.1, 0.1), (0.9, 0.8), (0.1, 0.9)))
#print(is_convex((0.0, 0.0), (1.0, 0.0), (0.3, 0.3), (0.0, 1.0)))
#print(is_convex((0.0, 0.0), (0.2, 0.7), (1.0, 1.0), (0.0, 1.0)))
#print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.7, 0.3)))
#print(is_convex((0.7, 0.8), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)))
#print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 0.0)))
#print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 0.0), (0.0, 0.0)))
#print(is_convex((1.0, 0.0), (1.0, 0.0), (1.0, 0.0), (1.0, 0.0)))

