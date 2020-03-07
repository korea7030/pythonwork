from queue import Queue

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}


def bfs(graph, start_node):
    # visit = list() 시간복잡도 : O(n)
    visit = {}  # 시간복잡도 : O(1)
    queue = Queue()

    queue.put(start_node)

    while queue.qsize() > 0:
        node = queue.get()

        if node not in visit:
            visit[node] = True

            for next_node in graph[node]:
                queue.put(next_node)

    return visit


if __name__ == '__main__':
    result2 = bfs(graph, 'A')
    print(list(result2.keys()))