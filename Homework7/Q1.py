class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [-stone for stone in stones]
        heapq.heapify(heap) 
        print(heap) 

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap,x-y)

        if heap:
            return -heap[0]
        return 0
