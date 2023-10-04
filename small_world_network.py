# Import the necessary libraries.
import random, os
import scipy, pylab
import netgraph

# Import your network definitions
import networkx as nx
import networkx.generators.random_graphs as nx_random
import matplotlib.pyplot as plt

#import imp
#imp.reload(networkx)	# Helps with ipython %run command

def MakeRingGraph(num_nodes, Z):
    """
    Makes a ring graph with Z neighboring edges per node.
    """
 # Create an empty ring graph
    G = nx.Graph()

    # Add nodes
    for i in range(num_nodes):
        G.add_node(i)

    # Connect each node to its Z neighbors
    for i in range(num_nodes):
        for j in range(1, Z + 1):
            neighbor = (i + j) % num_nodes
            G.add_edge(i, neighbor)

    return G
num_nodes = 20
Z=8
ring_graph = MakeRingGraph(num_nodes, Z)
# Plot the ring graph
pos = nx.circular_layout(ring_graph)
nx.draw(ring_graph, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold', edge_color='red')
plt.title('Ring Graph')
plt.show()


def AddRandomEdges(graph, num_edges_tried):
    """Attempts to add num_edges_tried random bonds to a graph. It may add 
    fewer, if the bonds already exist."""
    pass

def MakeSmallWorldNetwork(L, Z, p):
    """
    Makes a small--world network of size L and Z neighbors,
    with p*Z*L/2 shortcuts added.  This is the Watts-Newman variant
    of the original Watts-Strogatz model.  The original model
    used a rewiring technique, replacing a randomly selected short-range
    bond with a randomly-selected long-range shortcut.  The Watts-Newman
    model keeps all short-range bonds intact, and adds p*Z*L/2 random
    shortcuts.  This revised model is both simpler to treat analytically
    (see the renormalization group analysis by Watts and Newman) and
    avoids the potential for subgraphs to become disconnected from
    one another due to rewiring.
    """
    pass
    
def SmallWorldSimple(L, Z, p):
    """
    Generate and display small world network. Creates a graph g using
    MakeSmallWorldNetwork, and uses the NetGraphics command 
    DisplayCircleGraph, with only the mandatory argument g. Returns g.
    """
    pass

def MakePathLengthHistograms(L=100, Z=4, p=0.1):
    """
    Plots path length histograms for small world networks.
    Find list of all lengths
    Use pylab.hist(lengths, bins=range(max(lengths)), normed=True) """
    pass

def FindAverageAveragePathLength(L, Z, p, numTries):
    """Finds mean and standard deviation for path length between nodes,
    for a small world network of L nodes, Z bonds to neighbors, 
    p*Z*L/2 shortcuts, averaging over numTries samples"""
    pass

def GetPathLength_vs_p(L, Z, numTries, parray):
    """Calculates array of mean pathlengths and sigmas for small
    world networks; returns pathlengths and sigmas"""
    pass

def PlotPathLength_vs_p(L, Z, numTries=2,
                        parray=10.**scipy.arange(-3., 0.001, 0.25)):
    """Plots path length versus p"""
    pass

def PlotScaledPathLength_vs_pZL(LZarray, numtries=2, 
                                pZLarray=10.**scipy.arange(-1., 2.001, 0.25)):
    """
    PlotScaledPathLength_vs_pZL(((L1,Z1),(L2,Z2),...), numtries,
    				   [pZLa,pZLb,pZLc...])
    will plot the scaled path length for small world networks of size Li and
    neighbors Zi, at scaled rewiring probabilities pZLa, pZLb, ...
    Uses either MultiPlot.py to do the scaling, or rescales by hand, depending
    on the implementation chosen.
    To rescale, p is multiplied by Z*L and the mean path length ell is
    multiplied by 2*Z/L.
    """
    pass
    
def FindAverageClusteringCoefficient(L, Z, p, numTries):
    """Finds clustering coefficient for small world graph"""
    pass

def GetClustering_vs_p(L, Z, numTries, parray):
    pass

def PlotClustering_vs_p(L, Z, numTries,
                        parray=10.**scipy.arange(-3., 0.001, 0.1)):
    pass

def PlotWattsStrogatzFig2(L, Z, numTries,
                          parray=10.**scipy.arange(-4, 0.001, 0.25)):
    """Duplicate Watts and Strogatz Figure 2: rescale vertical axes"""
    pass

def TestBetweennessSimple():
    """
    Makes a simple graph for which one can calculate the betweenness by 
    hand, to check your algorithm.
    """
    pass
def SmallWorldBetweenness(L, Z, p, dotscale=4, linescale=2, windowMargin=0.02):
    """
    Display small world network with edge and node betweenness,
    using NetGraphics routine DisplayCircleGraph, passing in arguments
    for edge-weights and node_weights. Passes through the arguments for 
    dotscale, linescale, and windowMargin, to fine-tune the graph
    """
    pass

