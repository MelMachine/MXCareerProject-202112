class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        low, high = 0, len(numbers) -1 

        while low < high:
            mid = low + (high - low) // 2
            if numbers[mid] < numbers[high]:
                high = mid
            elif numbers[mid] > numbers[high]:
                low = mid + 1  

            else: high -=1
        return numbers[low]
