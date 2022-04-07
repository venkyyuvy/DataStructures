import networkx as nx
from node import Node
from search import \
    bfs_constant_space, dfs_constant_space, dfs_iterative
import matplotlib.pyplot as plt

graph = nx.DiGraph()
nodes = [Node(i) for i in range(10)]
graph.add_edge(nodes[0], nodes[1])
graph.add_edge(nodes[0], nodes[2])
graph.add_edge(nodes[1], nodes[3])
graph.add_edge(nodes[1], nodes[4])
graph.add_edge(nodes[3], nodes[4])
graph.add_edge(nodes[4], nodes[9])
graph.add_edge(nodes[2], nodes[5])
graph.add_edge(nodes[2], nodes[6])
graph.add_edge(nodes[3], nodes[7])
graph.add_edge(nodes[3], nodes[8])
graph.add_edge(nodes[8], nodes[7])

nx.draw(graph, node_color=range(10), 
    cmap=plt.cm.Blues,  with_labels=True, font_weight='bold')

def graph_reset(graph):
    for n in graph.nodes():
        n.nxt_node=None

def test_bfs():
    graph_reset(graph)
    solution = bfs_constant_space(
        graph, nodes[0])
    assert solution == \
        '-'.join(f'{i}' for i in range(10))

def test_dfs():
    graph_reset(graph)
    solution = dfs_constant_space(
        graph=graph, start_node=nodes[0])
    assert solution == \
        '0-2-6-5-1-4-9-3-8-7'

def test_dfs_iterative():
    graph_reset(graph)
    solution = dfs_iterative(
        graph, nodes[0])
    assert solution == \
        '0-2-6-5-1-4-9-3-8-7'