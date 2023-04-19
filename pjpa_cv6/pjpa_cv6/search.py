# -*- coding: utf-8 -*-

import re

#""" 
#Úkol 6.
#Vaším dnešním úkolem je vytvořit program, který o zadaném textu zjistí některé
#údaje a vypíše je na standardní výstup. Hlavním smyslem cvičení je procvičit
#si práci s regulárními výrazy, takže pro plný bodový zisk je nutné použít k
#řešení právě tento nástroj.

#Program musí pracovat s obecným textem, který bude zadaný v souboru. Jméno
#souboru bude zadáno jako vstupní parametr funkce main, která by měla být
#vstupním bodem programu. Samozřejmě, že funkce main by neměla řešit problém
#kompletně a měli byste si vytvořit další pomocné funkce. Můžete předpokládat,
#že soubor bude mít vždy kódování utf-8 a že bude psaný anglicky, tedy jen
#pomocí ASCII písmen, bez české (či jiné) diakritiky. 

#Konkrétně musí program zjistit a vypsat:

#1. Počet slov, která obsahují nejméně dvě samohlásky (aeiou) za sebou. Například
#slovo bear.

#2. Počet slov, která obsahují alespoň tři samohlásky - například slovo atomic.

#3. Počet slov, která mají šest a více znaků - například slovo terrible.

#4. Počet řádků, které obsahují nějaké slovo dvakrát. 

#Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
#"""


def main(file_name):
    #"""
    #zpracujte soubor 
    #"""
    f=open(file_name)
    text=f.read()
    f.close()
    text=text.lower()
    text=text.replace(".", '')
    text=text.replace(",", '')
    text=text.replace("\"", '')
    lines=text.split('\n')
    word_dict = {}
    for line in lines:
        words=line.split(" ")
        for word in words:
            word_dict.update({word: 1})
    first=double_vowel(word_dict)
    second=three_vowels(word_dict)
    third=gte_six(word_dict)
    fourth=two_occurences(lines)
    print(first)
    print(second)
    print(third)
    print(fourth)
    pass

def double_vowel(words):
    n=0
    for word in words:
        reg=re.search("[aeiyou][aeiyou]", word)
        if (reg != None):
            n+=1
    return n

def three_vowels(words):
    n=0
    for word in words:
        reg=re.search("[aeiyou].*[aeiyou].*[aeiyou]", word)
        if (reg != None):
            n+=1
    return n

def gte_six(words):
    n=0
    for word in words:
        reg=re.search("[a-z]{6,}", word)
        if (reg != None):
            n+=1
    return n

def two_occurences(lines):
    n=0
    for line in lines:
        reg=re.findall("\\b([a-z]{1,})\\b.*\\b\\1\\b", line)
        for match in reg:
            n+=1
    return n

if __name__ == '__main__':
    main('cv06_test.txt')