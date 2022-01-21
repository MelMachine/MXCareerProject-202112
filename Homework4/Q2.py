class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stackLeft, stackStar = [], []

        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stackLeft.append(i)
            elif c == "*":
                stackStar.append(i)
            else:
                if stackLeft:
                    stackLeft.pop()
                elif stackStar:
                    stackStar.pop()
                else:
                    return False

        while stackLeft and stackStar:
            if stackLeft[-1] < stackStar[-1]:
                stackLeft.pop()
                stackStar.pop()
            else:
                return False

        return len(stackLeft) == 0
