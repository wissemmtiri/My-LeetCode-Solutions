class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        zigzag = ['' for _ in range(numRows)]
        row, step = 0, 1
        for c in s:
            zigzag[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(zigzag)