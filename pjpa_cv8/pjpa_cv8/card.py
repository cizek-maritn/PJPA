# -*- coding: ISO-8859-1 -*-

#"""
#@TODO implementujte dle zadání cvièení 8
#"""

class Card:
    #"""
    #Tøída pro reprezentaci hracích karet
    #"""

    def __init__(self, given_rank, given_suit):
        if (given_rank<2) or (given_rank>14):
            raise TypeError("Karta musí mít hodnotu od 2 do 14. Byla zadána hodnota: " + str(given_rank))
        elif (given_suit=='s') or (given_suit=='k') or (given_suit=='p') or (given_suit=='t'):
            self.rank=given_rank
            self.suit=given_suit
        else:
            raise TypeError("Karta musí mít barvu zadanou znakem s, k, p nebo t. Bylo zadáno: " + given_suit)
       

    def black_jack_rank(self):
        #"""
        #Metoda vrací hodnotu karty dle pravidel pro Black Jack
        #:return:
        #"""
        if (self.rank<2) or (self.rank>14):
            raise TypeError("Karta musí mít hodnotu od 2 do 14. Byla zadána hodnota: " + str(self.rank))
        elif not ((self.suit=='s') or (self.suit=='k') or (self.suit=='p') or (self.suit=='t')):
            raise TypeError("Karta musí mít barvu zadanou znakem s, k, p nebo t. Bylo zadáno: " + self.suit)

        if (self.rank==14):
            return 11
        elif (self.rank>10):
            return 10
        else:
            return self.rank

    def __str__(self):
        if (self.rank<2) or (self.rank>14):
            raise TypeError("Karta musí mít hodnotu od 2 do 14. Byla zadána hodnota: " + str(self.rank))
        elif not ((self.suit=='s') or (self.suit=='k') or (self.suit=='p') or (self.suit=='t')):
            raise TypeError("Karta musí mít barvu zadanou znakem s, k, p nebo t. Bylo zadáno: " + self.suit)

        s=""
        if (self.suit=='s'):
            s+="srdcov"
        elif (self.suit=='k'):
            s+="károv"
        elif (self.suit=='p'):
            s+="pikov"
        else:
            s+="trefov"

        if (self.rank==2):
            s+="á dvojka"
        elif (self.rank==3):
            s+="á trojka"
        elif (self.rank==4):
            s+="á ètyøka"
        elif (self.rank==5):
            s+="á pìtka"
        elif (self.rank==6):
            s+="á šestka"
        elif (self.rank==7):
            s+="á sedmièka"
        elif (self.rank==8):
            s+="á osmièka"
        elif (self.rank==9):
            s+="á devítka"
        elif (self.rank==10):
            s+="á desítka"
        elif (self.rank==11):
            s+="ý spodek"
        elif (self.rank==12):
            s+="á královna"
        elif (self.rank==13):
            s+="ý král"
        else:
            s+="é eso"

        return s

    def __eq__(self, other):
        return self.black_jack_rank()==other.black_jack_rank()

    def __lt__(self, other):
        return self.black_jack_rank()<other.black_jack_rank()

    def __le__(self, other):
        return self.black_jack_rank()<=other.black_jack_rank()

    def __gt__(self, other):
        return self.black_jack_rank()>other.black_jack_rank()

    def __ge__(self, other):
        return self.black_jack_rank()>=other.black_jack_rank()

if __name__ == '__main__':
    #a=Card(2, 's')
    #b=Card(5, 't')
    #if (a<b):
    #    print("ano")
    pass

