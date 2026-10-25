
import heapq


def a_star(graph, heuristic, start, goal):
    open_list = []
    counter = 0

    g_score = {start: 0}
    parent = {start: None}

    heapq.heappush(
        open_list,
        (heuristic[start], counter, start)
    )

    while open_list:
        f, _, current = heapq.heappop(open_list)

        # Skip an outdated queue entry
        if f != g_score[current] + heuristic[current]:
            continue

        # Check whether the goal is reached
        if current == goal:
            path = []
            node = current

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("Path:", " -> ".join(path))
            print("Total cost:", g_score[goal])
            return path

        # Explore neighbouring nodes
        for neighbor, cost in graph.get(current, []):
            tentative_g = g_score[current] + cost

            if tentative_g < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = tentative_g
                parent[neighbor] = current

                counter += 1
                h = heuristic[neighbor]
                f = tentative_g + h

                heapq.heappush(
                    open_list, (f, counter, neighbor)
                )

    print("No solution found")
    return None


# Graph: neighbor and edge cost
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2)],
    'B': [('C', 1)],
    'C': [('G', 5)],
    'G': []
}

# Heuristic values
heuristic = {
    'S': 5,
    'A': 4,
    'B': 2,
    'C': 3,
    'G': 0
}

start = 'S'
goal = 'G'

a_star(graph, heuristic, start, goal)
