from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        lastRow = self.getRow(rowIndex - 1)

        newRow = [1]
        for j in range(1, rowIndex):
            newRow.append(lastRow[j-1] + lastRow[j])
        newRow.append(1)
        return newRow
