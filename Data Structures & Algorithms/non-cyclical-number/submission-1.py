class Solution:
    def isHappy(self, n: int) -> bool:
        face_one = False
        num_set = set()
        while not face_one:
            cur = 0
            for dig in str(n):
                cur += int(dig) ** 2
            if cur == 1:
                return True
            elif cur in num_set:
                print(num_set)
                return False
            num_set.add(cur)
            n = cur
        return True