class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(list)
        for edge in edges:
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])
        def crawl(current, connections, checked: List[int]):
            checked[current] = 1 #mark off used
            for k in connections[current]:
                if(checked[k] == 0):
                    crawl(k, connections, checked)
        components = 0
        checked = [0] * n
        for i in range(n):
            if(checked[i] == 0):
                components = components + 1
                crawl(i, connections, checked)
        return components
        

        
            
