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


def dfs(graph, start_node):
    # visit = list()
    visit = {}
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visit:
            # visit.append(node)
            visit[node] = True
            stack.extend(graph[node])

    return visit


if __name__ == '__main__':
    result = dfs(graph, 'A')
    print(list(result.keys()))