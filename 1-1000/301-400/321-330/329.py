class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        lengths = [[0] * m for _ in range(n)]

        def get4dir(i, j):
            dirs = []
            if i > 0:
                dirs.append((i-1, j))
            if j > 0:
                dirs.append((i, j-1))
            if i < n-1:
                dirs.append((i+1, j))
            if j < m-1:
                dirs.append((i, j+1))

            return dirs

        def get_length(i, j):
            if lengths[i][j] > 0:
                return lengths[i][j]
            length = 1
            for _i, _j in get4dir(i, j):
                if matrix[i][j] < matrix[_i][_j]:
                    length = max(length, 1 + get_length(_i, _j))
            lengths[i][j] = length
            return length

        max_length = 0
        for i in range(n):
            for j in range(m):
                max_length = max(max_length, get_length(i, j))

        return max_length
