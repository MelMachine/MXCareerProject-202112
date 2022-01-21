class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ans = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()
                if not stack:
                    break

                h = min(height[i],height[stack[-1]]) - height[cur]
                w = i - stack[-1] - 1
                ans  += h * w

            stack.append(i) 
        return ans
