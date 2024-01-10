'''
Implement Depth First Search graph algorithm

Build an adjacency_list graph using the build_graph function

Run the dfs algorithm on the graph starting with the start node.

Time Complexity: O(V + E) - where V and E is the number of vertices and edges
                            of the graph respectively. In dfs, every vertex is
                            explored once contributing to O(V). For each vertex,
                            the algorithm explores all its adjacent edges either
                            twice(for undirected graph) or once(for directed graph)
                            contributing to O(E). Time complexity = O(V + E)
Space Complexity: O(V) - where V is the number of vertices in the graph
                         In the worst case, a linked list time of a graph,
                         we will end up with all the vertices in the call stack
                         leading to O(V) space due to recursion depth
'''


def build_graph(edges):
    """Build an adjacency list graph from a list of edges"""
    graph = {}
    for edge in edges:
        u, v = edge

        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)  # comment this out if directed graph

    return graph


def dfs(graph, start):
    """Run dfs on the graph starting from the start node"""
    result = []
    dfs_helper(graph, set(), start, result)
    return result


def dfs_helper(graph, visited, current_node, result):
    """Runs the actual dfs algorithm recursively"""
    visited.add(current_node)
    result.append(current_node)

    for neighbor in graph[current_node]:
        if neighbor not in visited:
            dfs_helper(graph, visited, neighbor, result)

if __name__ == '__main__':
    # Sample test cases
    sample_edges_1 = [[1, 2], [1, 5], [2, 5], [1, 4], [4, 3], [3, 5]]
    sample_graph_1 = build_graph(sample_edges_1)
    assert dfs(sample_graph_1, 1) == [1, 2, 5, 3, 4], "Failed"

    sample_edges_2 = [[0, 1], [0, 3], [1, 3], [0, 2], [1, 2]]
    sample_graph_2 = build_graph(sample_edges_2)
    assert dfs(sample_graph_2, 1) == [1, 0, 3, 2], "Failed"

    sample_edges_3 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]
    sample_graph_3 = build_graph(sample_edges_3)
    assert dfs(sample_graph_3, 1) == [1, 2, 3, 4, 5], "Failed"

    samples_edges_4 = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]]
    sample_graph_4 = build_graph(samples_edges_4)
    assert dfs(sample_graph_4, 1) == [1, 2, 4, 5, 3, 6, 7], "Failed"
    print("All test cases passed!")
