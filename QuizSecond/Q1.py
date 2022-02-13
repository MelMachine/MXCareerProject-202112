class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, -1
        minNumber, maxNumber = nums[len(nums)-1], nums[0]



        for i in range(len(nums)):
            if nums[i] < maxNumber:
                end = i
            else:
                maxNumber = nums[i]
            print(end)

            if nums[len(nums)-i-1] > minNumber:
                start = len(nums)-i-1
            else:
                minNumber = nums[len(nums)-i-1]

        return end - start +1
