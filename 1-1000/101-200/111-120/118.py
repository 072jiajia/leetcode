from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            lastRow = ans[i-1]
            newRow = [1]
            for j in range(1, i):
                newRow.append(lastRow[j-1] + lastRow[j])
            newRow.append(1)
            ans.append(newRow)
        return ans
