import numpy as np
import scipy.sparse as sp

def encode_onehot(labels):
    """
    Input:  labels        | list of categorical data
    Return: labels_onehot | m x n numpy array
                            m = number of data points
                            n = number of labels
    """
    classes = set(labels)
    classes_dict = {}
    for idx, c in enumerate(classes):
        classes_dict[c] = np.identity(len(classes))[idx, :]
    labels_onehot = np.array(list(map(classes_dict.get, labels)), dtype=np.int32)
    return labels_onehot


def load_data(path="email-data/", dataset="email"):
    """
    Input:  path     | dataset path
            dataset  | dataset name

    Return: features | N x D feature matrix
            adj      | N x N adjacency matrix
            labels   | N x E label matrix

    Other:  N -> Number of nodes
            D -> Number of features
            E -> Number of classes
    """
    print('Loading {} dataset...'.format(dataset))

    # Labels
    labels = np.genfromtxt("{}{}-labels.txt".format(path, dataset), dtype=np.int32)
    labels = encode_onehot(labels[:, 1])

    # Features
    features = np.zeros((labels.shape[0], 0))

    # Graph
    edges = np.genfromtxt("{}{}-core.txt".format(path, dataset), dtype=np.int32)
    adj = np.zeros((labels.shape[0], labels.shape[0]))
    for node1, node2 in edges:
        adj[node1][node2] = 1

    print('Dataset has {} nodes, {} edges, {} features.'.format(adj.shape[0], edges.shape[0], features.shape[1]))

    return features, adj, labels
