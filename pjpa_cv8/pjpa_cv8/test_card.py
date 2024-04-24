
#"""
#Testy pro modul card a t��du Card ze cvi�en� 8.

#Ke spu�t�n� je pot�eba modul pytest

#https://docs.pytest.org/en/latest/

#pip install pytest
#"""

import card
import pytest


@pytest.mark.parametrize('rank, suit', [
    (1, "s"),
    (18, "s"),
    (5, "x"),
    (17, "x"),
])
def test_bad_card_raises(rank, suit):
    #"""
    #Pokud karta vytvo�it nejde - nap��klad proto, �e je �patn� barva �i hodnota,
    #mus� t��da vyhodit v�jimku TypeError.
    #"""

    with pytest.raises(TypeError):
        card.Card(rank, suit)


def test_rank():
    #"""
    #Test metody vracejici hodnost karty
    #"""
    t_card = card.Card(3, "s")
    result = 3
    assert result == t_card.rank


def test_suit():
    #"""
    #Test metody vracejici barvu karty
    #"""
    t_card = card.Card(3, "t")
    result = "t"
    assert result == t_card.suit


@pytest.mark.parametrize('rank, suit, expected', [
    (3, "s", 3),
    (5, "t", 5),
    (10, "s", 10),
    (11, "s", 10),
    (12, "s", 10),
    (13, "s", 10),
    (14, "s", 11)
])
def test_black_jack_rank(rank, suit, expected):
    #"""
    #Test metody vracejici hodnotu karty dle pravidel pro Black Jack
    #"""
    t_card = card.Card(rank, suit)
    assert expected == t_card.black_jack_rank()


@pytest.mark.parametrize('rank, suit, expected', [
    (3, "s", "srdcov� trojka"),
    (10, "s", "srdcov� des�tka"),
    (11, "s", "srdcov� spodek"),
    (12, "s", "srdcov� kr�lovna"),
    (13, "s", "srdcov� kr�l"),
    (14, "s", "srdcov� eso")
])
def test_str(rank, suit, expected):
    #"""
    #Test metody pro vypis karty 
    #"""
    t_card = card.Card(rank, suit)

    assert expected == str(t_card)


def test_card_equals():
    #"""
    #Test porovnani, karty jsou si rovny
    #"""
    t_card1 = card.Card(2, "s")
    t_card2 = card.Card(2, "k")
    assert t_card1 == t_card2


def test_greater_then():
    #"""
    #Test porovnani, prvni karta je v�t�� ne� druh�
    #"""
    t_card1 = card.Card(3, "s")
    t_card2 = card.Card(2, "k")
    assert t_card1 > t_card2


def test_less_then():
    #"""
    #Test porovn�n�, prvn� karta je men�� ne� druh�
    #"""
    t_card1 = card.Card(2, "s")
    t_card2 = card.Card(5, "k")
    assert t_card1 < t_card2
