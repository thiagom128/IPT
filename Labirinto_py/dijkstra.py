from math import inf as infinity

class Graph:
    def __init__(self, graph, initial, destination):
        self.graph = graph
        self.initial_node = graph[initial[1]][initial[0]]
        self.destination_node = graph[destination[1]][destination[0]]

    def __str__(self):
        return "\n".join([" ".join([str(column).ljust(6) for column in row])
                         for row in self.graph])

    def get_nodes(self):
        return [node for row in self.graph for node in row]

    def get_neighbors(self, node):
        neighbors = []
        if (node.y != 0):
            neighbors.append(self.graph[node.y - 1][node.x])
        if (node.y != len(self.graph) - 1):
            neighbors.append(self.graph[node.y + 1][node.x])
        if (node.x != 0):
            neighbors.append(self.graph[node.y][node.x - 1])
        if (node.x != len(self.graph[node.y]) - 1):
            neighbors.append(self.graph[node.y][node.x + 1])
        return neighbors


class Node:
    tentative_distance = None
    visited = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.tentative_distance)

    def distance_to(self, other):
        return 1


def dijkstra(graph):
    initial_node = graph.initial_node
    destination_node = graph.destination_node

    # Marca todos os nos como nao visitado. Cria um conjunto de todos os nos nao visitados e coloca o nome como nao visitados.
    unvisited = set(graph.get_nodes())

    # Atribui a cada no um valor de distancia provisoria, definindo como zero a posicao inicial do no e infinito para os outros.
    initial_node.tentative_distance = 0
    for node in unvisited:
        if node and node is not initial_node:
            node.tentative_distance = infinity

    current_node = initial_node

    while not destination_node.visited:
        # Para o no atual, considere todos os vizinhos nao visitados e calcule suas distancias provisorias ate o atual.
        # Compare a distancia provisoria recem calculada com o valor atribuido atual e atribual o menor.
        for neighbor in graph.get_neighbors(current_node):
            if not neighbor or neighbor.visited:
                continue
            new_tentative_distance = current_node.tentative_distance + current_node.distance_to(neighbor)
            if neighbor.tentative_distance > new_tentative_distance:
                neighbor.tentative_distance = new_tentative_distance

        # Quando terminanmos de considerar todos os vizinhos do no atual, marque o no atual como visitado
        # e remova do conjunto nao visitado.
        # Um no visitado nunca podera ser visitado novamente.
        current_node.visited = True
        unvisited.remove(current_node)

        # Movendo para o proximo no nao visitado com a menor distancia provisoria
        smallest_tentative_distance = infinity
        for node in unvisited:
            if node and node.tentative_distance < smallest_tentative_distance:
                smallest_tentative_distance = node.tentative_distance
                current_node = node

    return destination_node.tentative_distance