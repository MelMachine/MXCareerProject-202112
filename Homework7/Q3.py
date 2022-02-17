class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        counter = collections.Counter(s)

        if max(counter.values()) > (len(s)+1) // 2:
            return ans

        heap = []
        for key,val in counter.items():
            heapq.heappush(heap,(-val, key))

        prev = (0, None)

        while heap:
            val, key = heapq.heappop(heap)
            ans += key
            if prev[0] < 0:
                heapq.heappush(heap, prev)

            prev =(val + 1, key)
        return ans
