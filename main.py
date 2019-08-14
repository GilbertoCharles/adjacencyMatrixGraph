'''
 # @ Author: Gilberto Charles
 # @ Create Time: 2019-08-14 12:17:02
 # @ Modified by: Gilberto Charles
 # @ Modified time: 2019-08-14 12:17:33
 # @ Description: Main function to read and populate the Adjacency Matrix
 '''


# -*- coding: utf-8 -*-
import numpy as np
from Graph import AdjacencyMatrix

def main():
    ## Preenchimento da matriz
    qt_nodes = int(input(f"Quantos vértices deseja adicionar? "))
    qt_arestas = int(input(f"Quantas arestas deseja adicionar? "))
    matriz_adjacencia = np.zeros([qt_nodes, qt_nodes], dtype = int)
    for i in range(0, qt_arestas):
        aresta1 = int(input(f"Entre com o primeiro número da aresta {i + 1}: "))
        aresta2 = int(input(f"Entre com o segundo número da aresta {i + 1}: "))
        matriz_adjacencia[aresta1 -1 ,aresta2 - 1] = 1
        matriz_adjacencia[aresta2 - 1,aresta1 - 1] = 1
        print()
    ## Print da matriz para o terminal
    print('-='*20)
    print('Imprimindo a matriz completa')
    print(matriz_adjacencia)

    Object = AdjacencyMatrix(qt_nodes)
    Object.plot_graph_1(matriz_adjacencia, 'Matriz de Adjacencia')
if __name__ == '__main__':
    main()
