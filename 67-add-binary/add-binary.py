class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # n = max(len(a),  len(b))
        # a, b = a.zfill(n) , b.zfill(n)

        return bin(int(a, 2) + int(b, 2))[2:]