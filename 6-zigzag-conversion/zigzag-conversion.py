class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # first i will go from top down and move column and move index up by one, untill i reach the top then, go top
        # but in this case I will have to turn from zigzag to a row like format

        if numRows == 1 or numRows >= len(s):
            return s
        
        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        
        for i in range(numRows):
            rows[i] = "".join(rows[i])
        
        return ''.join(rows)


        