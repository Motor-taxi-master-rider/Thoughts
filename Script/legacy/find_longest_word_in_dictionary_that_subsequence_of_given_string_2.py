import unittest
from collections import defaultdict
from typing import List

"""
给定字符串string和一组单词words，找到words中最长的单词，它是string的子序列。

满足以下条件时，单词w是字符串s子序列：在不改变字符顺序的前提下，删除s的任意数量字符(可能为0个)，能够组成单词w。

testApple为示例。
"""


def solve(string: str, words: List[str]):
    result = None
    Alphabets = defaultdict(list)
    for word in words:
        if word == '':
            result = ''
            continue
        Alphabets[word[0]].append([word, 0])

    for character in string:
        alphabet_list = Alphabets[character]
        for i in reversed(range(len(alphabet_list))):
            temp = alphabet_list.pop(i)
            temp[1] += 1
            if len(temp[0]) == temp[1]:
                if result is None or temp[1] > len(result):
                    result = temp[0]
            else:
                Alphabets[temp[0][temp[1]]].append(temp)
    return result


class TestSolution(unittest.TestCase):
    def testApple(self):
        """
        able, ape, apple都为`string`的子序列， apple为最长子序列
        bale不是`string`的子序列
        banana比apple长, 但不是`string`的子序列
        """
        string = 'abppplee'
        words = ['able', 'ape', 'apple', 'bale', 'banana']
        self.assertEqual(solve(string, words), 'apple')


    def testAbple(self):
        """ pick first candidate """
        string = 'abppplee'
        words = ['able', 'ape', 'abple','apple', 'bale', 'banana']
        self.assertEqual(solve(string, words), 'abple')

    def testAbppple(self):
        """ string itself is a candidate """
        string = 'abppplee'
        words = ['able', 'ape', 'apple', 'bale', 'banana', 'abppplee']
        self.assertEqual(solve(string, words), 'abppplee')

    def testNotExist(self):
        """ return None if no candidate """
        string = 'helloworld'
        words = ['able', 'ape', 'apple', 'bale', 'banana']
        self.assertEqual(solve(string, words), None)

    def testEmptyString(self):
        """ empty string should be a candidate """
        string = 'helloworld'
        words = ['able', 'ape', 'apple', 'bale', 'banana', '']
        self.assertEqual(solve(string, words), '')

    def testLongString(self):
        string = 'thequickbrownfoxjumpsoverthelazydog'
        words = ['fqizl', 'vkwsq', 'xypsz', 'wdjbu', 'btjiu', 'thqkg', 'gmtkq', 'dcbsx', 'iykfq', 'aouvr']
        self.assertEqual(solve(string, words), 'thqkg')


if __name__ == '__main__':
    unittest.main()
