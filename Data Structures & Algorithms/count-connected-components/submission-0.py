class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        edge_map = defaultdict(list)
        for edge in edges:
            u, v = edge
            edge_map[u].append(v)
            edge_map[v].append(u)

        visited = set()
        
        stack = []
        for i in range(n):
            if i not in visited:
                stack.append(i)
                visited.add(i)
                while stack:
                    node = stack.pop()
                    for adj in edge_map[node]:
                        if adj not in visited:
                            stack.append(adj)
                            visited.add(adj)
                result += 1
        
        return result