def triangle(a, b, c):
    
    #Funkce vrací True nebo False, podle toho zda strany a, b, c mohou tvoøit
    #pravoúhlý trojúhelník

    #Pro jednoduchost mùžete pøedpokládat, že strany a, b jsou odvìsny, c je pøepona. 
    #Tak jako je to ve známé matematické pouèce. 

    if (c^2)==(a^2+b^2): 
        return True
    else: 
        return False

#print(triangle(3,4,5))
#print(triangle(3,4,20))
#print(triangle(3,4,1))