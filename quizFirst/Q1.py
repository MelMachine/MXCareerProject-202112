class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        checkList = ["a","e","i","o","u","A","E","I","O","U"]

        

        list1 =  list(s)
       
        left, right = 0, len(list1) - 1
        while left < right:
           
            if list1[left] in checkList and list1[right] in checkList:
                list1[left], list1[right] = list1[right], list1[left]
                left += 1
                right -=1


            elif list1[left] not in checkList:
                left += 1 

            elif list1[right] not in checkList:
                right -= 1 

            
                
        return "".join(list1)

