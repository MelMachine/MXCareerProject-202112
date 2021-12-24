class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        strList = s.strip().split()

        print(strList)
        left, right = 0, len(strList) - 1

        while left < right:
            tmp = strList[left]
            strList[left] = strList[right]
            strList[right] = tmp
            left+=1
            right-=1
        #return strList
        return " ".join(strList)
        
