class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap, ans = [], []
        for i in range(len(points)):
            dis = points[i][0]**2 + points[i][1]**2
            loc = points[i]
            if len(heap) < k:
                heapq.heappush(heap,(-dis, loc))
            else:
                if -heap[0][0] > dis:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-dis, loc))

        for dis,loc in heap:
            ans.append(loc)
        return ans
