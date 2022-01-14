class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """


        ans = float("inf")
        tmp = 0

        total = sum(cardPoints)
        windowSize = len(cardPoints) - k 

        for i in range(len(cardPoints)):
            
            tmp += cardPoints[i]

            if i >= windowSize:
                tmp -= cardPoints[i-windowSize] 

            if i >= windowSize - 1:
            

                ans = min(ans,tmp)
                print(tmp)



        return total- ans
        
