# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D2oEkX5KLxGCCxHEhHZa7bUKimvhdz6i
"""

from collections import deque

def breadthFirstSearch(graph, startNode):
    visited = []

    queue = deque([startNode])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}
startNode = 1
result = breadthFirstSearch(graph, startNode)
print(result)