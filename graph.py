import sys
from tqdm import *
from collections import defaultdict
from utilities import number_lines

# Parameters
directory_name  = 'wikipedia-data/'
edges_file      = directory_name + 'wiki-topcats.txt'
names_file      = directory_name + 'wiki-topcats-page-names.txt'
categories_file = directory_name + 'wiki-topcats-categories.txt'

# Graph class
class Node:
    def __init__(self, value, name, category):
        self.value = value
        self.name = name
        self.category = category

class Graph:
    def __init__(self):
        self.nodes = set()
        self.num_nodes = 0
        self.node_order = dict()
        self.edges = defaultdict(list)
    
    def add_node(self, value):
        self.nodes.add(value)
        self.num_nodes = self.num_nodes + 1
        self.node_order[value] = self.num_nodes -1


    def add_edge(self, node1, node2):
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)

if __name__ == '__main__':
    # Construct graph
    wikipedia_graph = Graph()

    # Construct nodes
    node_dict = {}
    with open(names_file) as infile:
        print('Loading information from: ', names_file)
        for line in tqdm(infile, total=number_lines(names_file)):
            v, name = line.split(" ", 1)
            v = int(v)
            
            # Create node
            node = Node(v, name, None)

            # Add node to dictionary
            node_dict[v] = node

    with open(categories_file) as infile:
        print('Loading information from: ', categories_file)
        for line in tqdm(infile, total=number_lines(categories_file)):
            values = line.split()
            category = values[0]
            nodes    = values[1:]
            
            # Iterate through nodes in category
            for v in nodes:
                v = int(v)
                # Update category
                node_dict[v] = category

    # Construct edges
    with open(edges_file) as infile:
        print('Loading information from: ', edges_file)
        for line in tqdm(infile, total=number_lines(edges_file)):
            v1, v2 = line.split()
            v1 = int(v1); v2 = int(v2)

            node1 = node_dict[v1]
            node2 = node_dict[v2]
            wikipedia_graph.add_node(node1)
            wikipedia_graph.add_node(node2)
            wikipedia_graph.add_edge(node1, node2)

    # Testing
    # TODO


