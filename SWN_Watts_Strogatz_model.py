import networkx as nx
import matplotlib.pyplot as plt

def generate_small_world_network(n, k, p):
    """
    Generates a small-world network using the Watts-Strogatz model.

    Parameters:
        n (int): Number of nodes.
        k (int): Number of nearest neighbors to connect initially for each node.
        p (float): Probability of rewiring each edge.

    Returns:
        networkx.Graph: Small-world network.
    """
    # Create a regular ring lattice
    G = nx.watts_strogatz_graph(n, k, p)

    return G

# Parameters for the Watts-Strogatz model
n = 10  # Number of nodes
k = 5   # Number of nearest neighbors to connect initially for each node
p = 0.1  # Probability of rewiring each edge

# Generate a small-world network
small_world_network = generate_small_world_network(n, k, p)

# Plot the network
pos = nx.circular_layout(small_world_network)
nx.draw(small_world_network, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
plt.title('Small World Network (Watts-Strogatz Model)')
plt.show()

