from itertools import combinations

class Node:

    def __init__(self, infected, id):
        self.neighbors = []
        self.infected = infected
        self.id = id
        uninfected_nodes.append(self)
    def addNeighbor(self, neighborNode):
        self.neighbors.append(neighborNode)

uninfected_nodes = []
polynomial = []
xpower = 0

def generatecombinations():
    from itertools import combinations
    combs = []
    possibilities = []
    r = 1
    for i in range(len(uninfected_nodes)):
        possibilities.append(i)
    while r < len(uninfected_nodes) + 1:
        for combination in combinations(possibilities, r):
            combs.append(list(combination))
        r += 1
    print(combs)
    print(len(combs))
    print(uninfected_nodes[(combs[0][0])])
    return True

    #create a dictionary or really long list of possible combinations
    #pass into infect the values from combinations

def infect():
    # xpower = combination.length
    #retreive index of uninfected_node to infect 
    #pass on list of Node objects with certain nodes infected to function forcing
    return True

def forcing():
    #run logic of forcing  
    #force until no change then goes to function forced
    return True

def forced():
    #check whether each node is forced or not
    #check xpower to see which index of polynomial to add to
    return True

if __name__ == '__main__':
    Node1 = Node(False, "1")
    Node2 = Node(False, "2")
    Node3 = Node(False, "3")

    generatecombinations()

