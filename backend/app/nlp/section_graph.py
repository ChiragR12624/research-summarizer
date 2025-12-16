# backend/app/nlp/section_graph.py

import networkx as nx

def build_section_graph(section_titles: list[str]):
    graph = nx.DiGraph()
    previous = None

    for section in section_titles:
        graph.add_node(section)
        if previous:
            graph.add_edge(previous, section)
        previous = section

    return graph

def graph_to_dict(graph):
    return {
        "nodes": list(graph.nodes),
        "edges": list(graph.edges)
    }
