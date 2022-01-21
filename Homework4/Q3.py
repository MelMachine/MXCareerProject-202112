class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        dic = {}

        for item in s:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1

        for ch in s:
            if ch not in stack:
                while stack and ch < stack[-1] and ch in dic and dic[stack[-1]]>0:
                    stack.pop()

                stack.append(ch)
            dic[ch] -= 1

        return "".join(stack)
