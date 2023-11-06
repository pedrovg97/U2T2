import os
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Função para calcular a média do grau dos vizinhos
def calculate_average_neighbor_degree(graph):
    return nx.average_neighbor_degree(graph)

# Lista de arquivos .edges na pasta do projeto
edge_files = [file for file in os.listdir() if file.endswith('.edges')]

# Inicialize listas para armazenar todos os dados
all_degrees = []
all_avg_neighbor_degrees = []

# Loop através dos arquivos .edges
for edge_file in edge_files:
    # Leia o arquivo .edges e crie um grafo bipartido
    graph = nx.read_edgelist(edge_file, create_using=nx.Graph)

    # Calcule a média do grau dos vizinhos
    avg_neighbor_degree = calculate_average_neighbor_degree(graph)

    # Grau dos nós
    degrees = [d for n, d in graph.degree()]

    all_degrees.extend(degrees)
    all_avg_neighbor_degrees.extend(list(avg_neighbor_degree.values()))

# Crie um gráfico de dispersão relacionando a média do grau dos vizinhos com o grau dos nós
plt.figure(figsize=(8, 6))
plt.scatter(all_degrees, all_avg_neighbor_degrees, s=10)
plt.title('Average Neighbor Degree vs. Node Degree')
plt.xlabel('Node Degree')
plt.ylabel('Average Neighbor Degree')

# Adicione a linha de tendência
z = np.polyfit(all_degrees, all_avg_neighbor_degrees, 1)
p = np.poly1d(z)
plt.plot(all_degrees, p(all_degrees), 'r--', label='Trendline')

# Adicione uma legenda
plt.legend()

# Exiba o gráfico
plt.show()
