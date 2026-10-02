class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_dict = defaultdict(list)
        distance_list = []
        heapq.heapify(distance_list)
        result = []
        for i in range(len(points)):
            distance_dict[math.sqrt(points[i][0]**2 + points[i][1]**2)].append(i)
            heapq.heappush(distance_list, math.sqrt(points[i][0]**2 + points[i][1]**2))

        while k > 0:
            current_dis = heapq.heappop(distance_list)
            current_point = points[distance_dict[current_dis][0]]
            distance_dict[current_dis].pop(0)
            result.append(current_point)
            k -= 1
        return result
