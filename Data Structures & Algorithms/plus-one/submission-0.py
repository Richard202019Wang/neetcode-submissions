class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        cur = 0
        res = []
        for i in range(len(digits) - 1, -1, -1):
            result += digits[i] * (10 ** cur)
            cur += 1
        
        result += 1
        cur -= 1
        while cur >= 0:
            if result // (10 ** cur) != 10:
                res.append(result // (10 ** cur))
            else:
                res.append(1)
                res.append(0)
            result = result % (10 ** cur)
            cur -= 1
        return res

        