s = 'abppplee'
d = ['able', 'ale', 'apple', 'bale', 'kangaroo']

from collections import defaultdict, namedtuple

Alphabets = defaultdict(list)
for word in d:
    Alphabets[word[0]].append([word, 0])


def solution(s, d):
    result = ''
    for character in s:
        alphabet_list = Alphabets[character]
        for i in reversed(range(len(alphabet_list))):
            temp = alphabet_list.pop(i)
            temp[1] += 1
            if len(temp[0]) == temp[1]:
                if temp[1] >= len(result):
                    result = temp[0]
            else:
                Alphabets[temp[0][temp[1]]].append(temp)
    return result


print(solution(s, d))
