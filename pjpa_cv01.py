def triangle(a, b, c):
    
    #Funkce vrac� True nebo False, podle toho zda strany a, b, c mohou tvo�it
    #pravo�hl� troj�heln�k

    #Pro jednoduchost m��ete p�edpokl�dat, �e strany a, b jsou odv�sny, c je p�epona. 
    #Tak jako je to ve zn�m� matematick� pou�ce. 

    if (c^2)==(a^2+b^2): 
        return True
    else: 
        return False

#print(triangle(3,4,5))
#print(triangle(3,4,20))
#print(triangle(3,4,1))