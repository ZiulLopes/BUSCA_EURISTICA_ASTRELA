# No
class Node:
    # "key" identificador do no
    # "forward_cost" custo heuristico usado no calculo
    def __init__(self, key, forward_cost):
        self.key = key
        self.forward_cost = forward_cost

    def getKey(self):
        return self.key

    def getForwardCost(self):
        return self.forward_cost
