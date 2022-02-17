class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        subList = [(-nums[i], i) for i in range(k)]
        print(subList)
        heapq.heapify(subList)

        ans = [-subList[0][0]]
        for i in range(k,len(nums)):
            heapq.heappush(subList, (-nums[i],i))
            while subList[0][1] <= i - k:
                heapq.heappop(subList)
            ans.append(-subList[0][0])

        return ans 
