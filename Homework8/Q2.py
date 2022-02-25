class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowChecker, colChecker, regionChecker = {}, {}, {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                regionNumber = i // 3 * 3 + j // 3

                if rowChecker.has_key(i) and board[i][j] in rowChecker[i]:
                    return False 
                if colChecker.has_key(j) and board[i][j] in colChecker[j]:
                    return False
                if regionChecker.has_key(regionNumber) and board[i][j] in regionChecker[regionNumber]:
                    return False

                if not rowChecker.has_key(i):
                    rowChecker[i] = set()
                rowChecker[i].add(board[i][j])

                if not colChecker.has_key(j):
                    colChecker[j] = set()
                colChecker[j].add(board[i][j])

                if not regionChecker.has_key(regionNumber):
                    regionChecker[regionNumber] = set()
                regionChecker[regionNumber].add(board[i][j])

        return True
