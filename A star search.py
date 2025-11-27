from collections import defaultdict

# Hàm DFS đệ quy
def dfs_recursive(adj_list, visited, node, result):
    # Đánh dấu node đã được thăm
    visited[node] = True
    result.append(node)

    # Duyệt tất cả đỉnh kề của node
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs_recursive(adj_list, visited, neighbor, result)


# Hàm DFS tổng quát, xử lý cả đồ thị rời rạc
def dfs(adj_list):
    num_vertices = len(adj_list)
    visited = [False] * num_vertices
    result = []

    # Duyệt qua từng đỉnh đề phòng đồ thị bị chia thành nhiều thành phần
    for node in range(num_vertices):
        if not visited[node]:
            dfs_recursive(adj_list, visited, node, result)

    return result


# Thêm cạnh vào danh sách kề (đồ thị vô hướng)
def add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)


if __name__ == "__main__":
    V = 6  # Số lượng đỉnh
    adj_list = [[] for _ in range(V)]  # Khởi tạo danh sách kề rỗng

    # Thêm các cạnh vào đồ thị
    add_edge(adj_list, 1, 2)
    add_edge(adj_list, 2, 0)
    add_edge(adj_list, 0, 3)
    add_edge(adj_list, 5, 4)

    # Thực hiện DFS
    result = dfs(adj_list)

    # In kết quả
    print("DFS Traversal:", *result)
