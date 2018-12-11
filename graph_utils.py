import numpy as np
import scipy.sparse as sp

from collections import Counter


def encode_onehot(labels):
    """
    Input:  labels        | list of categorical data
    Return: labels_onehot | m x n numpy array
                            m = number of data points
                            n = number of labels
    """
    # Hardcode number
    num_labels = 42

    classes = set(labels)
    classes_dict = {}
    for c in classes:
        classes_dict[c] = np.identity(num_labels)[c, :]
    labels_onehot = np.array(list(map(classes_dict.get, labels)), dtype=np.int32)
    return labels_onehot


def nearest_neighbor(node, labels, graph):
    """
    docstring
    """
    neighbors = np.where(graph[node] == 1)[0]
    preds = []

    for n in neighbors:
        preds.append(int(labels[np.where(labels[:, 0] == n)][:, 1]))

    counter = Counter(preds)
    return counter.most_common(1)[0][0]


def load_email_data(path="email_data/", dataset="email", sparse=True):
    """
    Input:  path     | dataset path
            dataset  | dataset name
            sparse   | return sparse matrices

    Return: features | N x D feature matrix
            adj      | N x N adjacency matrix
            labels   | N x E label matrix

    Other:  N -> Number of nodes
            D -> Number of features
            E -> Number of classes
    """
    print('Loading {} dataset...'.format(dataset))

    # Labels
    labels_data = np.genfromtxt("{}{}_labels.txt".format(path, dataset), dtype=np.int32)
    labels = encode_onehot(labels_data[:, 1])

    # Graph
    edges = np.genfromtxt("{}{}_core.txt".format(path, dataset), dtype=np.int32)
    adj = np.zeros((labels.shape[0], labels.shape[0]))
    for node1, node2 in edges:
        adj[node1][node2] = 1
        adj[node2][node1] = 1

    # Random Features
    # pass

    # Features
    features = np.zeros(labels.shape[0], dtype=np.int32)
    for node in range(labels.shape[0]):
        features[node] = nearest_neighbor(node, labels_data, adj)
    features = encode_onehot(features)

    print('Dataset has {} nodes, {} edges, {} features.'.format(adj.shape[0], edges.shape[0], features.shape[1]))

    if sparse:
        features = sp.csr_matrix(features)
        adj      = sp.coo_matrix(adj)

    return features, adj, labels
