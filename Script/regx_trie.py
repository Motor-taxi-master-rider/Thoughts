import re


class Trie():
    """Regex::Trie in Python. Creates a Trie out of a list of words. The trie can be exported to a Regex pattern.
    The corresponding Regex should match much faster than a simple Regex union."""

    def __init__(self):
        self.data = {}

    def add(self, word):
        ref = self.data
        for char in word:
            ref[char] = char in ref and ref[char] or {}
            ref = ref[char]
        ref[''] = 1

    def dump(self):
        return self.data

    def quote(self, char):
        return re.escape(char)

    def _pattern(self, pData):
        data = pData
        if "" in data and len(data.keys()) == 1:
            return None

        alt = []
        cc = []
        q = 0
        for char in sorted(data.keys()):
            if isinstance(data[char], dict):
                recurse = self._pattern(data[char])
                if recurse:
                    alt.append(self.quote(char) + recurse)
                else:
                    cc.append(self.quote(char))
            else:
                q = 1
        cconly = not len(alt) > 0

        if len(cc) > 0:
            if len(cc) == 1:
                alt.append(cc[0])
            else:
                alt.append('[' + ''.join(cc) + ']')

        if len(alt) == 1:
            result = alt[0]
        else:
            result = "(?:" + "|".join(alt) + ")"

        if q:
            if cconly:
                result += "?"
            else:
                result = "(?:%s)?" % result
        return result

    def pattern(self):
        return self._pattern(self.dump())


if __name__ == '__main__':
    import re
    import timeit
    import random

    with open(r'C:\Users\ezhuxzh\Downloads\words') as wordbook:
        banned_words = [word.strip().lower() for word in wordbook]
        random.shuffle(banned_words)

    test_words = [
        ("Surely not a word", "#surely_NöTäWORD_so_regex_engine_can_return_fast"),
        ("First word", banned_words[0]),
        ("Last word", banned_words[-1]),
        ("Almost a word", "couldbeaword")
    ]


    def trie_regex_from_words(words):
        trie = Trie()
        for word in words:
            trie.add(word)
        return re.compile(r"\b" + trie.pattern() + r"\b", re.IGNORECASE)


    def find(word):
        def fun():
            return union.match(word)

        return fun


    for exp in range(1, 6):
        print("\nTrieRegex of %d words" % 10 ** exp)
        union = trie_regex_from_words(banned_words[:10 ** exp])
        for description, test_word in test_words:
            time = timeit.timeit(find(test_word), number=1000) * 1000
            print("  %s : %.1fms" % (description, time))
