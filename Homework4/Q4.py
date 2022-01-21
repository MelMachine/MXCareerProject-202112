class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # visited = set()
        # # 数据拆分
        # def get_nums(num):
        #     result = 0
        #     mid = num 
        #     while mid > 0:
        #         result += (mid % 10)
        #         mid = mid // 10
        #     return result

        # def dfs(i,j):
        #     if i >= m or j >= n or (i,j) in visited or k < get_nums(i)+get_nums(j):
        #         return 0
        #     visited.add((i,j))
        #     dfs(i+1,j)
        #     dfs(i,j+1)
        
        # dfs(0, 0)
        # return len(visited)

        visited = set()

        def getSum(x):
            res = 0
            while x != 0 :
                res += x % 10
                x = x//10
            return res


        def DFS(i,j):
            if i >= m or j >= n or k < getSum(i) + getSum(j) or (i,j) in visited:
                return 0


            visited.add((i,j))
            DFS(i+1,j)
            #DFS(i-1,j)
            DFS(i,j+1)
            #DFS(i,j-1)

        DFS(0,0)
        print(visited)
        return len(visited)
