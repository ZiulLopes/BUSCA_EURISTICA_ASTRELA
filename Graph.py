from collections import defaultdict # dictionary of lists
from PriorityQueue import *
# Grafo
class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.path = []

        self.successors = defaultdict(list)


    # adicionar as bordas
    def addEdge(self, source, destination, weight):
        edge = (source, destination, weight)
        if not self.existsEdge(edge):
            self.nodes[source], self.nodes[destination] = source, destination
            self.edges.append(edge)
            self.successors[source.getKey()].append((destination, weight))
        else:
            print('Error: borda (%s -> %s com largura %s) já exites!!' \
                % (edge[0].getKey(), edge[1].getKey(), edge[2]))

    def existsEdge(self, edge):
        for e in self.edges:
            if e[0].getKey() == edge[0].getKey() and \
                e[1].getKey() == edge[1].getKey() and e[2] == edge[2]:
                return True
        return False

    def getPath(self):
        return self.path


    # "A*"
    def executeAStar(self, initial_node, goal_node):
        if not self.edges:
            print('Error: grafo não contem bordas!!')
        else:
            # verificar se nós existem
            if initial_node in self.nodes and goal_node in self.nodes:
                if initial_node == goal_node: # verifica se é mesmo nó
                    return 0

                queue = PriorityQueue() # criar pilha de prioridaades

                # distancias
                distance_vector, antecessors = {}, {}
                for node in self.nodes:
                    distance_vector[node.getKey()] = None
                    antecessors[node.getKey()] = None
                distance_vector[initial_node.getKey()] = 0

                # calculo do custo
				# F(n) = G(n) + H(n)
                g_cost, h_cost = 0, initial_node.getForwardCost()
                f_cost = g_cost + h_cost
                queue.insert((initial_node, g_cost, h_cost), f_cost)
                total_cost = None

                while True:

                    current_node, g_cost, h_cost = queue.remove()

                    successors = self.successors[current_node.getKey()]

                    for successor in successors:
                        destination, weight = successor

                        # calcular custos
                        new_g_cost = g_cost + weight
                        h_cost = destination.getForwardCost()
                        f_cost = new_g_cost + h_cost
                        queue.insert((destination, new_g_cost, h_cost), f_cost)

                        # atualizar distancia
                        if distance_vector[destination.getKey()]:
                            if distance_vector[destination.getKey()] > new_g_cost:
                                distance_vector[destination.getKey()] = new_g_cost
                                antecessors[destination.getKey()] = current_node.getKey()
                        else:
                            distance_vector[destination.getKey()] = new_g_cost
                            antecessors[destination.getKey()] = current_node.getKey()

                        # verificar objetivo
                        if destination.getKey() == goal_node.getKey():
                            # atualizar custo total
                            if not total_cost:
                                total_cost = f_cost
                            elif f_cost < total_cost:
                                total_cost = f_cost

                    if queue.isEmpty(): # verificar pilha vazia
                        # montar caminho
                        curr_node = goal_node.getKey()
                        while curr_node:
                            self.path.append(curr_node)
                            curr_node = antecessors[curr_node]
                        self.path = self.path[::-1]
                        return total_cost
            else:
                print('Error: Nó não existe!!')
