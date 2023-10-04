import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def watts_newman_model(n, m, p_rewire):
    """
    Generates a network using the Watts-Newman model.

    Parameters:
        n (int): Number of nodes.
        m (int): Number of edges to attach from a new node to existing nodes.
        p_rewire (float): Probability of rewiring each edge.

    Returns:
        networkx.Graph: Watts-Newman model network.
    """
    G = nx.barabasi_albert_graph(n, m)
    
    # Rewire edges with a given probability
    for node in G.nodes():
        for neighbor in list(G.neighbors(node)):
            if np.random.rand() < p_rewire:
                new_neighbor = np.random.choice(G.nodes())
                # Ensure it's not already a neighbor and not itself
                while new_neighbor == node or G.has_edge(node, new_neighbor):
                    new_neighbor = np.random.choice(G.nodes())
                G.remove_edge(node, neighbor)
                G.add_edge(node, new_neighbor)
    
    return G

# Parameters for the Watts-Newman model
n = 30  # Number of nodes
m = 5   # Number of edges to attach from a new node to existing nodes
p_rewire = 0.2  # Probability of rewiring each edge

# Generate a network using the Watts-Newman model
watts_newman_network = watts_newman_model(n, m, p_rewire)

# Plot the network
pos = nx.circular_layout(watts_newman_network)
nx.draw(watts_newman_network, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
plt.title('Watts-Newman Model Network')
plt.show()

