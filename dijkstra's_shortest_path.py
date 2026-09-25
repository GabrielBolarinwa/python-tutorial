import heapq


class Graph:
    @staticmethod
    def shortest_path(n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        adj = [[] for _ in range(n)]
        for s, d, weight in edges:
            adj[s].append([d, weight])
        shortest = {}

        minHeap = [[0, src]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
