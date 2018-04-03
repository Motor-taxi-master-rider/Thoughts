s = 'abppplee'
d = ['able', 'ale', 'apple', 'bale', 'kangaroo']


def compare(s, w):
    i = 0
    for character in w:
        while i < len(s):
            if character == s[i]:
                i += 1
                break
            i += 1
        else:
            break
    else:
        return True
    return False


def solution(s, d):
    for w in sorted(d, key=len, reverse=True):
        if compare(s, w):
            return w


print(solution(s, d))
