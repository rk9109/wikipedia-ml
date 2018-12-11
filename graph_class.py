import sys
from collections import defaultdict

# Graph class
class Node:
    def __init__(self, value, label):
        self.value = value
        self.label = label

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, node1, node2):
        self.edges[node1].append(node2)


def construct_graph(university):
    """
    Return: web_graph | graph from web_data
    """
    # Initialize graph
    web_graph = Graph()

    # Parameters
    directory_name  = 'web_data/'
    edges_file      = directory_name + university + '.cites'
    labels_file     = directory_name + university + '.content'

    # Construct nodes
    node_dict = {}
    with open(labels_file) as infile:
        print('Loading information from: ', labels_file)
        for line in infile:
            values = line.split()
            name  = values[0]
            label = values[-1]

            # Create node
            node = Node(name, label)

            # Add node to dictionary
            node_dict[name] = node

    # Construct edges
    with open(edges_file) as infile:
        print('Loading information from: ', edges_file)
        for line in infile:
            v1, v2 = line.split()

            node1 = node_dict[v1]
            node2 = node_dict[v2]
            web_graph.add_node(node1)
            web_graph.add_node(node2)
            web_graph.add_edge(node1, node2)
            web_graph.add_edge(node2, node1)

    return web_graph


def nearest_neighbor(graph):
    loss = 0
    for node in graph.nodes:
        neighbors = [neighbor.label for neighbor in graph.edges[node]]
        pred      = max(set(neighbors), key=neighbors.count)
        real      = node.label

        if (real != pred):
            loss = loss + 1

    print('0-1 NN Error = ' + str(loss) + ', Mean 0-1 Error = ' + str(loss/len(web_graph.nodes)))


if __name__ == '__main__':
    # Call constructor
    web_graph = construct_graph('washington')

    # Results
    print("Dataset has {} nodes".format(len(web_graph.nodes)))

    # Nearest neighbor
    nearest_neighbor(web_graph)
