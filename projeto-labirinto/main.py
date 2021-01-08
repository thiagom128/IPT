import dijkstra as d

caminho_arquivo = input("Informe o caminho do Labirinto(1 - Paredes, 0 - Livre, 2 - Inicial, 3 - Final):\n")
with open(caminho_arquivo) as f: # C:\python\labirinto.txt
    conteudo = f.readlines()

#Pega o tamanho em linha e colunas do arquivo, para ser percorrido
tam_with = len(conteudo[0])
height = len(conteudo)

nodes = [[None for _ in range(tam_with)] for __ in range(height)]

for x in range(tam_with):
    for y in range(height):
        pixel = conteudo[y][x:x+1]
        if pixel == '1': # Paredes
            nodes[y][x] = None
        else:
            nodes[y][x] = d.Node(x, y) # Livre

        if pixel == '2':
            initial_coords = (x, y) # Inicio
        if pixel == '3':
            destination_coords = (x, y) # Chegada


graph = d.Graph(nodes, initial_coords, destination_coords)

destination_distance = d.dijkstra(graph)

initial_node = graph.graph[initial_coords[1]][initial_coords[0]]
destination_node = graph.graph[destination_coords[1]][destination_coords[0]]

nodes = graph.get_nodes()

for node in nodes:
    if node:
        node.visited = False

axu = []
current_node = destination_node
smallest_tentative_distance = destination_distance
# Encontrando o caminho
while current_node is not initial_node:
    neighbors = graph.get_neighbors(current_node)
    for neighbor in neighbors:
        if not neighbor or neighbor.visited:
            continue
        if neighbor.tentative_distance < smallest_tentative_distance:
            smallest_tentative_distance = neighbor.tentative_distance
            neighbor.visited = True
            current_node = neighbor
    axu.append(f"[{current_node.x},{current_node.y}]")

#Faz o print do caminho
caminho = ''
for i in range(len(axu)):
    x = i + 1
    if x <= len(axu):
        caminho += axu[len(axu)-x]
print("O menor caminho encontrado partindo do 2:")
print(caminho)
