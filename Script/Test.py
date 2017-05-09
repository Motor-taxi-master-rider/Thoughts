class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bit = x ^ y
        count = 0
        while bit:
            if bit & 1 == 1:
                count += 1
            bit = bit >> 1
        return count


a = Solution()
print(a.hammingDistance(1, 4))
