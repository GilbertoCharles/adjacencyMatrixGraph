'''
 # @ Author: Gilberto Charles
 # @ Create Time: 2019-08-13 20:33:23
 # @ Modified by: Gilberto Charles
 # @ Modified time: 2019-08-14 12:18:09
 # @ Description: Implementation of matplotlib to draw a graph
 '''
import matplotlib.pyplot as plt
import networkx as nx
from copy import deepcopy

class AdjacencyMatrix(object):

    def __init__(self, nodes):
        self.nodes = nodes

    def plot_graph_1(self, graph, title='Grafo 1'):

        graph_layout = nx.Graph()
        adjacent_matrix = deepcopy(graph)

        for n in range(1, self.nodes+1):
            graph_layout.add_node(n)

        for i in range(self.nodes):
            for j in range(self.nodes):

                if(adjacent_matrix[i][j] != 0):
                    graph_layout.add_edge(i+1, j+1)
                    adjacent_matrix[i][j] = 0
                    adjacent_matrix[j][i] = 0

        dictionary = nx.spring_layout(graph_layout)
        nx.draw_networkx_nodes(graph_layout, dictionary)
        nx.draw_networkx_labels(graph_layout, dictionary)
        nx.draw_networkx_edges(graph_layout, dictionary)
        plt.title(title)
        plt.show()