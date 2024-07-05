from collections import deque

# def add_vertex(data):
#     global graph
#     if data in graph:
#         print("Already present")
#     else:
#         graph[data] = []


def add_edge(adj_list, start, end):
    adj_list[start].append(end)


def print_graph(graph):
    index = 0
    for arr in graph:
        print(index, "==>", end=" ")
        for num in arr:
            print(num, end=" ")
        print()
        index += 1


def bfs(adj_list, start_node):
    visited = [False for _ in range(len(adj_list))]
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        # print(adj_list[node])
        for number in adj_list[node]:
            if not visited[number]:
                visited[number] = True
                queue.append(number)


def add_edge_metrics(adj_metrics, i, j):
    metrics_size = len(adj_metrics)
    if 0 > i >= metrics_size and 0 > j >= metrics_size:
        return
    adj_metrics[i][j] = 1


if __name__ == "__main__":
    # graph = {}
    # add_vertex("A")
    # add_vertex("B")
    # add_vertex("C")
    # add_vertex("D")
    # add_vertex("E")
    # add_edge("A", "B")
    # add_edge("B", "D")
    # add_edge("C", "A")
    # add_edge("C", "E")
    # add_edge("C", "D")
    # add_edge("D", "E")
    # add_edge("D", "F")
    # print_graph()
    vertex_size = 5
    adj_list = [[] for _ in range(vertex_size)]
    add_edge(adj_list, 0, 1)
    add_edge(adj_list, 0, 2)
    add_edge(adj_list, 1, 3)
    add_edge(adj_list, 1, 4)
    add_edge(adj_list, 2, 4)
    print_graph(adj_list)
    x = 0

    bfs(adj_list, 0)

    adj_metrics = [[0 for _ in range(vertex_size)] for _ in range(vertex_size)]
    add_edge_metrics(adj_metrics, 0, 1)
    add_edge_metrics(adj_metrics, 0, 2)
    add_edge_metrics(adj_metrics, 1, 3)
    add_edge_metrics(adj_metrics, 1, 4)
    add_edge_metrics(adj_metrics, 2, 4)

