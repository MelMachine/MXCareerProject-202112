class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """

        ans = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                ans += customers[i]
                customers[i] =0


        maxNumber = 0
        tmp = 0 
        for i in range(len(customers)):
            
            if i < minutes:
                tmp += customers[i]
            else:
                tmp += customers[i] - customers[i-minutes]

            maxNumber = max(maxNumber,tmp)

        return maxNumber + ans
