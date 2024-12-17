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

def test_inc_vec():
    assert flx.inc_vec([1, 2, 3], 1, 0, None) == [2, 3, 4]
    assert flx.inc_vec([1, 2, 3], 1, 1, None) == [1, 3, 4]
    pass

def test_get_hash_for_string():
    assert flx.get_hash_for_string("switch-to-buffer") == {
        'r': [15],
        'e': [14],
        'f': [12, 13],
        'u': [11],
        'b': [10],
        '-': [6, 9],
        'o': [8],
        't': [3, 7],
        'h': [5],
        'c': [4],
        'i': [2],
        'w': [1],
        's': [0]
        }
    pass
