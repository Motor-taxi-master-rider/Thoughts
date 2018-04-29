from functools import lru_cache


def longest_common_subsequence(first, second):
    """longest sub sequence of a sting. It needn't to be consequent."""

    @lru_cache()
    def helper(p, q, pn, qn, subsequence):
        if pn < 0 or qn < 0:
            return subsequence
        if p[pn] == q[qn]:
            return helper(p, q, pn - 1, qn - 1, f'{p[pn]}{subsequence}')
        else:
            add_p = helper(p, q, pn, qn - 1, subsequence)
            add_q = helper(p, q, pn - 1, qn, subsequence)
            return max(add_p, add_q, key=len)

    return helper(first, second, len(first) - 1, len(second) - 1, '')


if __name__ == '__main__':
    P = 'BATD'
    Q = 'ABACD'
    assert longest_common_subsequence(P, Q) == 'BAD'

    P = 'WHATTIMEISIT'
    Q = 'WHATSTHEWEATHERLIKE'
    # 'WHATTEI' is a valid result. We didn't catch it because two intermediate sub string
    # may have same length but different characters when we compare them with the `max`
    # function. I've tried to make subsequence a tuple to store all the result, however I
    # just failed because in the first test case: intermediate sub strings 'AD' and 'BD'
    # will have the same length too, which is not what we want.
    # TODO: improve the algorithm to result multi reuslts
    assert longest_common_subsequence(P, Q) == 'WHATTET'
