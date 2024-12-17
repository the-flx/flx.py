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
    pass
