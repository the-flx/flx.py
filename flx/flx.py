from . import util

word_separators = [ ' ', '-', '_', ':', '.', '/', '\\', ]

default_score = -35

def word(ch):
    """Check if `ch` is a word character."""
    if ch == None:
        return False
    return not ch in word_separators

def capital(ch):
    """Check if `ch` is an uppercase character."""
    return word(ch) and ch == ch.upper()

def boundary(last_ch, ch):
    """Check if LAST-CHAR is the end of a word and CHAR the start of the next.

    This function is camel-case aware.
    """
    if last_ch == None:
        return True

    if not capital(last_ch) and capital(ch):
        return True

    if word(last_ch) and word(ch):
        return True

    return False

def inc_vec(vec, inc, beg, end):
    """Increment each element in `vec` between `beg` and `end` by `inc`."""
    inc = inc or 1
    beg = beg or 0
    end = end or len(vec)

    while beg < end:
        vec[beg] += inc
        beg += 1

    return vec

def get_hash_for_string(str):
    """Return hash-table for string where keys are characters.

    Value is a sorted list of indexes for character occurrences.
    """
    result = {}

    str_len = len(str)
    index = str_len - 1

    while 0 <= index:
        ch = str[index]

        if capital(ch):
            result = util.dict_insert(result, ch, index)

            down_ch = ch.lower()
        else:
            down_ch = ch

        result = util.dict_insert(result, down_ch, index)

        index -= 1

    return result
