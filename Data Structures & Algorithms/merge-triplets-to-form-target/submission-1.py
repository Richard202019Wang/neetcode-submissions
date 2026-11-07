class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t_a, t_b, t_c = target
        result = [False, False, False]
        for t in triplets:
            if all(result):
                return True
            t1, t2, t3 = t
            if t1 > t_a or t2 > t_b or t3 > t_c:
                continue
            if t1 == t_a:
                result[0] = True
            if t2 == t_b:
                result[1] = True
            if t3 == t_c:
                result[2] = True

        return all(result)




        