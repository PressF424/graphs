class Graph:
    def __init__(self, vertices):
        self.V = vertices  # вершины
        self.graph = []    # ребра

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        result = []  #  минимальное  дерево

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        for u, v, w in self.graph:
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Вывод минимального  дерева
        total_weight = sum([w for u, v, w in result])
        print("Минимальное остовное дерево включает следующие рёбра:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")
        print(f"Общая стоимость остовного дерева: {total_weight}")
