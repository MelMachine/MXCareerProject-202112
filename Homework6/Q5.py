class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def check(s):
            if not s:
                return True
            for i in range(1,len(s)+1):
                if s[:i] in wordDict:
                    if check(s[i:]):
                        return True
            return False

        return check(s)
