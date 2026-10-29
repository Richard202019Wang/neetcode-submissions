class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_num = defaultdict(int)
        edge_m = defaultdict(list)
        for edge in edges:
            u, v = edge
            edge_m[u].append(v)
            edge_m[v].append(u)
            adj_num[u] += 1
            adj_num[v] += 1
        
        q = deque([i for i in range(1, len(edges) + 1) if adj_num[i] == 1])
        while q:
            node = q.popleft()
            adj_num[node] -= 1
            for adj in edge_m[node]:
                adj_num[adj] -= 1
                if adj_num[adj] == 1:
                    q.append(adj)
        
        for edge in reversed(edges):
            u, v = edge
            if adj_num[u] == 2 and adj_num[v]:
                return [u, v]
        
            