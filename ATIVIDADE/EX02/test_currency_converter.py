import pytest
from currency_converter import usd_to_eur, eur_to_usd, usd_to_brl, brl_to_usd

def test_usd_to_eur():
    assert usd_to_eur(100) == 85
    assert usd_to_eur(200) == 170
    assert usd_to_eur(0) == 0

def test_eur_to_usd():
    assert eur_to_usd(85) == 100
    assert eur_to_usd(170) == 200
    assert eur_to_usd(0) == 0

def test_usd_to_brl():
    assert usd_to_brl(100) == 550
    assert usd_to_brl(200) == 1100
    assert usd_to_brl(0) == 0

def test_brl_to_usd():
    assert brl_to_usd(550) == 100
    assert brl_to_usd(1100) == 200
    assert brl_to_usd(0) == 0
