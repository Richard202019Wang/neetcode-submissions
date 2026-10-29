class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        node_m = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            node_m[u].append(v)
            node_m[v].append(u)
        
        visited = {0}

        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            visited.add(node)
            for adj in node_m[node]:
                if adj == parent:
                    continue
                if adj in visited:
                    return False
                stack.append((adj, node))
            # print(last_node)
        return len(visited) == n
