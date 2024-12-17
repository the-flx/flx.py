import sys

sys.path.append('../')

from flx import flx

def test_word():
    assert flx.word('C') == True
    assert flx.word('c') == True
    assert flx.word(' ') == False
    assert flx.word('\\') == False
    pass

def test_capital():
    assert flx.capital('C') == True
    assert flx.capital('c') == False
    assert flx.capital(' ') == False
    pass
