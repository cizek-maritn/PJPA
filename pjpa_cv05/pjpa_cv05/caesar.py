

def encrypt(word, offset):
    
    #:param word - slovo k zasifrovani
    #:param offset - znakovy posun
    #:return: zasifrovane slovo
    r_off=offset%26
    out=""
    for i in  word:
        num=ord(i)
        if (num>=65) and (num<=90):
            num=num+r_off
            if (num>90):
                num=num-26
        elif (num>=97) and (num<=122):
            num=num+r_off
            if (num>122):
                num=num-26
        out+=chr(num)
    return out


def decrypt(word, offset):
    
    #:param word - zasifrovane slovo
    #:param offset - znakovy posun
    #:return: desifrovane slovo
    r_off=offset%26
    out=""
    for i in  word:
        num=ord(i)
        if (num>=65) and (num<=90):
            num=num-r_off
            if (num<65):
                num=num+26
        elif (num>=97) and (num<=122):
            num=num-r_off
            if (num<97):
                num=num+26
        out+=chr(num)
    return out
	
if __name__ == "__main__":
    print(encrypt('to bolt or not to be',7))
    print(encrypt("flaxa", 27))
    print(encrypt('VeLkA MaLa', 19))
    print(decrypt('av ivsa vy uva av il', 7))
    print(decrypt('gmbyb', 27))
    print(decrypt('OxEdT FtEt', 19))