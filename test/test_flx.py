import sys

sys.path.append('../')

from flx import flx

def test_word():
    assert flx.word_p('C') == True
    assert flx.word_p('c') == True
    assert flx.word_p(' ') == False
    assert flx.word_p('\\') == False
    pass

def test_capital():
    assert flx.capital_p('C') == True
    assert flx.capital_p('c') == False
    assert flx.capital_p(' ') == False
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

def test_get_heatmap_str():
    assert flx.get_heatmap_str("switch-to-buffer", None) == [82, -4, -5, -6, -7, -8, -9, 79, -7, -8, 76, -10, -11, -12, -13, -13]
    pass

def test_bigger_sublist():
    assert flx.biggger_sublist([1, 2, 3, 4], None) == [1, 2, 3, 4]
    assert flx.biggger_sublist([1, 2, 3, 4], 2) == [3, 4]
    pass

def test_score_switch_to_buffer():
    result = flx.score("switch-to-buffer", "stb")
    assert result.indices == [0, 7, 10]
    assert result.score == 237
    assert result.tail == 0
    pass

def test_score_tsfe():
    result = flx.score("TestSomeFunctionExterme", "met")
    assert result.indices == [6, 16, 18]
    assert result.score == 57
    assert result.tail == 0
    pass

def test_score_mxv():
    result = flx.score("MetaX_Version", "met")
    assert result.indices == [0, 1, 2]
    assert result.score == 211
    assert result.tail == 2
    pass
