# encoding:utf-8

"""
    LUIZ FERNANDO LOPES
    Implementação de busca heuristica A *.
    Problema baseado na imagem grafo_robo.jpg onde o objetivo é partindo de A chegar na porta (G)

    Reference: https://www.youtube.com/watch?v=b9fH-j_yNHU
    Código adaptado do Author Marcos Castro

"""

# importar bibliotecas
from Node import *
from Graph import *


# Criar grafo
graph = Graph()

# Nos com valor heuristico
nodeA = Node("A", 30)
nodeB = Node("B", 26)
nodeC = Node("C", 21)
nodeD = Node("D", 7)
nodeE = Node("E", 22)
nodeF = Node("F", 36)
nodeG = Node("G", 0)

# Arestas como na imagem grafo_robo
graph.addEdge(nodeA, nodeB, 12)
graph.addEdge(nodeA, nodeC, 14)
graph.addEdge(nodeC, nodeD, 24)
graph.addEdge(nodeC, nodeE, 7)
graph.addEdge(nodeB, nodeC, 9)
graph.addEdge(nodeB, nodeD, 38)
graph.addEdge(nodeD, nodeG, 9)
graph.addEdge(nodeE, nodeD, 13)
graph.addEdge(nodeE, nodeF, 9)
graph.addEdge(nodeE, nodeG, 29)


total_cost = graph.executeAStar(nodeA, nodeG)
path = graph.getPath()

if total_cost:
    print('Custo total do grafo: {}\nCaminho: {}'.format(total_cost, ' -> '.join(path)))
else:
    print('Objetivo não encontrado!')


