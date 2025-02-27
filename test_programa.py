# test_primos.py
import pytest
from proyecto import es_primo

def test_numeros_primos():
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(5) == True
    assert es_primo(7) == True
    assert es_primo(11) == True

def test_numeros_no_primos():
    assert es_primo(0) == False
    assert es_primo(1) == False
    assert es_primo(4) == False
    assert es_primo(6) == False
    assert es_primo(9) == False
    assert es_primo(15) == False

def test_numeros_grandes():
    assert es_primo(97) == True  # 97 es primo
    assert es_primo(100) == False  # 100 no es primo
    assert es_primo(101) == True  # 101 es primo

def test_numeros_negativos():
    assert es_primo(-5) == False
    assert es_primo(-11) == False
