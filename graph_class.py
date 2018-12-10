import sys
from collections import defaultdict

# Parameters
directory_name  = 'email-data/'
edges_file      = directory_name + 'email-core.txt'
labels_file     = directory_name + 'email-labels.txt'

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


def construct_graph():
    """
    Return: email_graph | graph from emails-data
    """
    # Initialize graph
    email_graph = Graph()

    # Construct nodes
    node_dict = {}
    with open(labels_file) as infile:
        print('Loading information from: ', labels_file)
        for line in labels_file:
            v, label = line.split()

            # Create node
            node = Node(int(v), int(label))

            # Add node to dictionary
            node_dict[int(v)] = node

    # Construct edges
    with open(edges_file) as infile:
        print('Loading information from: ', edges_file)
        for line in edges_file:
            v1, v2 = line.split()
            v1 = int(v1); v2 = int(v2)

            node1 = node_dict[v1]
            node2 = node_dict[v2]
            email_graph.add_node(node1)
            email_graph.add_node(node2)
            email_graph.add_edge(node1, node2)

    return email_graph

def k_nearest_neighbor(graph, k=10):
    pass

if __name__ == '__main__':
    # Call constructor
    email_graph = construct_graph()

    # Results
    print("Dataset has {} nodes".format(len(email_graph.nodes)))

    # TODO Implement k-NN here
