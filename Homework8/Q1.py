class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        checker = {}
        for c in s:
            if c not in checker:
                checker[c] = True
            else:
                checker[c] = False

        for i in range(len(s)):
            if checker[s[i]] == True:
                return i
        return -1
