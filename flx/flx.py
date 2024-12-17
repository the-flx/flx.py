import sys

from . import util

class Result:
    indices = None
    score = None
    tail = None

    def __init__(self, indices, score, tail):
        self.indices = indices
        self.score = score
        self.tail = tail

word_separators = [ ' ', '-', '_', ':', '.', '/', '\\', ]

default_score = -35

def word_p(ch):
    """Check if `ch` is a word character."""
    if ch == None:
        return False
    return not ch in word_separators

def capital_p(ch):
    """Check if `ch` is an uppercase character."""
    return word_p(ch) and ch == ch.upper()

def boundary_p(last_ch, ch):
    """Check if LAST-CHAR is the end of a word and CHAR the start of the next.

    This function is camel-case aware.
    """
    if last_ch == None:
        return True

    if not capital_p(last_ch) and capital_p(ch):
        return True

    if not word_p(last_ch) and word_p(ch):
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

        if capital_p(ch):
            result = util.dict_insert(result, ch, index)

            down_ch = ch.lower()
        else:
            down_ch = ch

        result = util.dict_insert(result, down_ch, index)

        index -= 1

    return result

def get_heatmap_str(str, group_separator):
    """Generate the heatmap vector of string.

    See documentation for logic.
    """
    scores = []

    str_len = len(str)
    str_last_index = str_len - 1

    for _ in range(str_len):
        scores.append(default_score)

    penality_lead = '.'

    group_alist = [[-1, 0]]

    scores[str_last_index] += 1

    last_ch = None
    group_word_count = 0

    index1 = 0

    for ch in str:
        # before we find any words, all separaters are
        # considered words of length 1.  This is so "foo/__ab"
        # gets penalized compared to "foo/ab".
        effective_last_char = last_ch

        if group_word_count == 0:
            effective_last_char = None

        if boundary_p(effective_last_char, ch):
            group_alist[0].insert(2, index1)

        if not word_p(last_ch) and word_p(ch):
            group_word_count += 1

        # ++++ -45 penalize extension
        if not last_ch is None and last_ch == penality_lead:
            scores[index1] += -45

        if not group_separator is None and group_separator == ch:
            group_alist[0][1] = group_word_count
            group_word_count = 0
            group_alist.insert(0, [index1, group_word_count])

        if index1 == str_last_index:
            group_alist[0][1] = group_word_count
        else:
            last_ch = ch

        index1 += 1

    group_count = len(group_alist)
    separator_count = group_count - 1

    # ++++ slash group-count penalty

    if separator_count != 0:
        scores = inc_vec(scores, group_count * -2, None, None)

    index2 = separator_count
    last_group_limit = None
    basepath_found = False

    for group in group_alist:
        group_start = group[0]
        word_count = group[1]
        # this is the number of effective word groups
        words_len = len(group) - 2
        basepath_p = False

        if words_len != 0 and not basepath_found:
            basepath_found = True
            basepath_p = True

        num = None

        if basepath_p:
            # ++++ basepath separator-count boosts
            boosts = 0
            if separator_count > 1:
                boosts = separator_count - 1
            # ++++ basepath word count penalty
            penalty = -word_count
            num = 35 + boosts + penalty
        # ++++ non-basepath penalties
        else:
            if index2 == 0:
                num = -3
            else:
                num = -5 + (index2 - 1)

        scores = inc_vec(scores, num, group_start + 1, last_group_limit)

        cddr_group = group.copy()  # clone it
        cddr_group.pop(0)
        cddr_group.pop(0)

        word_index = words_len - 1
        last_word = last_group_limit or str_len

        for word in cddr_group:
            # ++++  beg word bonus AND
            scores[word] += 85

            index3 = word
            char_i = 0

            while index3 < last_word:
                scores[index3] += (-3 * word_index) - char_i
                char_i += 1
                index3 += 1

            last_word = word
            word_index -= 1

        last_group_limit = group_start + 1
        index2 -= 1

    return scores

def biggger_sublist(sorted_list, val):
    """Return sublist bigger than `val` from sorted `sorted-list`.

    If `val` is nil, return entire list.
    """
    result = []
    if val is None:
        return sorted_list
    else:
        for sub in sorted_list:
            if sub > val:
                result.append(sub)
    return result

def find_best_match(imatch, str_info, heatmap, greater_than, query, query_len, q_index, match_cache):
    """Recursively compute the best match for a string, passed as `str_info` and
    `heatmap`, according to `query`.
    """
    greater_num = greater_than or 0
    hash_key = q_index + (greater_num * query_len)
    hash_val = util.dict_get(match_cache, hash_key)

    if not hash_val is None:
        imatch.clear()
        for val in hash_val:
            imatch.append(val)
    else:
        uchar = query[q_index]
        sorted_list = util.dict_get(str_info, uchar)
        indexes = biggger_sublist(sorted_list, greater_than)
        temp_score = None
        best_score = -sys.maxsize - 1

        if q_index >= query_len - 1:
            # At the tail end of the recursion, simply generate all possible
            # matches with their scores and return the list to parent.
            for val in indexes:
                indices = [val]
                imatch.append(Result(indices, heatmap[val], 0))
        else:
            for val in indexes:
                elem_group = []
                find_best_match(elem_group, str_info.copy(), heatmap.copy(), val, query, query_len, q_index + 1, match_cache);

                for elem in elem_group:
                    caar = elem.indices[0]
                    cadr = elem.score
                    cddr = elem.tail

                    if (caar - 1) == val:
                        temp_score = cadr + heatmap[val] + (min(cddr, 3) * 15) + 60;
                    else:
                        temp_score = cadr + heatmap[val]

                    # We only care about the optimal match, so only forward the match
                    # with the best score to parent
                    if temp_score > best_score:
                        best_score = temp_score

                        imatch.clear()
                        indices = elem.indices.copy()
                        indices.insert(0, val)
                        tail = 0
                        if (caar - 1) == val:
                            tail = cddr + 1
                        imatch.append(Result(indices, temp_score, tail))

        util.dict_set(match_cache, hash_key, imatch.copy())

def score(str, query):
    """Return best score matching `query` against `str`."""
    if not str or not query:
        return None

    str_info = get_hash_for_string(str)
    heatmap = get_heatmap_str(str, None)

    query_len = len(query)
    full_match_boost = (1 < query_len) and (query_len < 5)
    match_cache = {}
    optimal_match = []
    find_best_match(optimal_match, str_info, heatmap, None, query, query_len, 0, match_cache)

    if len(optimal_match) == 0:
        return None

    result1 = optimal_match[0]
    caar = len(result1.indices)

    if full_match_boost and caar == len(str):
        result1.score += 10000

    return result1
