import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from generate_graph import *
import sys

graph_choice = str(sys.argv[1])
print(graph_choice)

# Generate graph parameters (choose between g1--g6)
probs, sizes, nb_class, method = property_graph(graph=graph_choice)

# Generate the graph and the associated node attribute s (dictionnary)
if graph_choice == 'g6':
    g, s_all = get_graph_prot(sizes=sizes, probs=probs, number_class=nb_class,
     choice=method, nb_sens=2)
    
    # Compute the assortativity coefficient 
    print('Assortativity coefficient wrt to the first attribute: %0.3f'%
      nx.attribute_assortativity_coefficient(g, 's'))
    
    # Compute the assortativity coefficient 
    print('Assortativity coefficient wrt to the second attribute: %0.3f'%
      nx.attribute_assortativity_coefficient(g, 's2'))

else:
    g, s = get_graph_prot(sizes=sizes, probs=probs, number_class=nb_class,
     choice=method)
    # Compute the assortativity coefficient 
    print('Assortativity coefficient: %0.3f'%
      nx.attribute_assortativity_coefficient(g, 's'))


if graph_choice == 'g5':
    #Retrieve indexes of node in each group
    s_idx = np.fromiter(s.values(), dtype=int)
    prot0 = np.where(s_idx == 0)[0]
    prot1 = np.where(s_idx == 1)[0]
    prot2 = np.where(s_idx == 2)[0]

    # Draw the graph 
    pos = nx.spring_layout(g, seed=1)
    nx.draw_networkx_nodes(g, pos=pos, node_size=250,  nodelist=prot0, node_color='powderblue',edgecolors='darkslategrey', label='A = 0')
    nx.draw_networkx_nodes(g, pos=pos, node_size=250, nodelist=prot1, node_color='darkmagenta',edgecolors='darkslategrey', label='A = 1')
    nx.draw_networkx_nodes(g, pos=pos, node_size=250, nodelist=prot2, node_color='orange',edgecolors='darkslategrey', label='A = 2')

    nx.draw_networkx_edges(g, pos=pos)
    plt.legend(loc="upper left", scatterpoints=1, prop={'size': 15})
    plt.tight_layout()
    plt.savefig('g5_paper.pdf', dpi=300, bbox_inches='tight')
    plt.show()
    
elif graph_choice == 'g6': 
    
    s = s_all[0]
    s2 = s_all[1]
    
    s_idx = np.fromiter(s.values(), dtype=int)
    s2_idx = np.fromiter(s2.values(), dtype=int)
    
    prot0 = np.where(s_idx == 0)[0]
    prot1 = np.where(s_idx == 1)[0]

    prot0_b = np.where(s2_idx == 0)[0]
    prot1_b = np.where(s2_idx == 1)[0]

    prot_0_0 = np.intersect1d(prot0, prot0_b)
    prot_0_1 = np.intersect1d(prot0, prot1_b)
    prot_1_0 = np.intersect1d(prot1, prot0_b)
    prot_1_1 = np.intersect1d(prot1, prot1_b)

    pos = nx.spring_layout(g, seed=1)
    nx.draw_networkx_nodes(g, pos=pos, node_shape="<", node_size=250, nodelist=prot_0_0, node_color='powderblue',edgecolors='darkslategrey', label="A = 0 $\cap$ A'=0")
    nx.draw_networkx_nodes(g, pos=pos, node_shape = '<', node_size=250, nodelist=prot_0_1, node_color='darkmagenta',edgecolors='darkslategrey', label="A = 0 $\cap$ A'=1")
    nx.draw_networkx_nodes(g, pos=pos, node_shape = 'o', node_size=250, nodelist=prot_1_0, node_color='powderblue',edgecolors='darkslategrey', label="A = 1 $\cap$ A'=0")
    nx.draw_networkx_nodes(g, pos=pos, node_shape = 'o', node_size=250, nodelist=prot_1_1, node_color='darkmagenta',edgecolors='darkslategrey', label="A = 1 $\cap$ A'=1")
    nx.draw_networkx_edges(g, pos=pos)
    plt.legend(loc="upper left", scatterpoints=1, prop={'size': 15})
    plt.tight_layout()
    plt.savefig('g6_paper.pdf', dpi=300, bbox_inches='tight')
    plt.show()
    
else: 
    s_idx = np.fromiter(s.values(), dtype=int)
    prot0 = np.where(s_idx == 0)[0]
    prot1 = np.where(s_idx == 1)[0]

    # Draw the graph 
    pos = nx.spring_layout(g, seed=1)
    nx.draw_networkx_nodes(g, pos=pos, node_size=250, nodelist=prot0, node_color='powderblue',edgecolors='darkslategrey', label='A = 0')
    nx.draw_networkx_nodes(g, pos=pos, node_size=250, nodelist=prot1, node_color='darkmagenta',edgecolors='darkslategrey', label='A = 1')
    nx.draw_networkx_edges(g, pos=pos)
    plt.legend(loc="upper left", scatterpoints=1, prop={'size': 15})
    plt.tight_layout()
    plt.savefig(graph_choice+'_paper.pdf', dpi=300, bbox_inches='tight')
    plt.show()

print("Done!")
        