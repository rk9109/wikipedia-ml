import numpy as np 

def vectorize(graph, node):
	if node in graph.nodes:
		vector = np.zeros(graph.num_nodes)
		for connected_node in graph.edges[node]:
			vector[graph.node_order[connected_node]] = 1
		return vector
	else:
		raise KeyError

def wordEmbed(graph):
	pass
