from re import S
import matplotlib.pyplot as plt
import networkx as nx
import random
import copy
    
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 
    
    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.
    
    G: the graph (must be a tree)
    
    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.
    
    width: horizontal space allocated for this branch - avoids overlap with other branches
    
    vert_gap: gap between levels of hierarchy
    
    vert_loc: vertical location of root
    
    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''
    
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos

            
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)









# leaf_nodes=[]
# G=nx.Graph()
# G.add_node(1);
# x=copy.deepcopy(G.nodes)
# for i in x:
#     for j in range (1,2**1+1):
#         leaf_nodes.append(i+j)
#         G.add_node(i+j)
#         G.add_edge(i,i+j)
# print (leaf_nodes)

# for leafs in leaf_nodes:
#     for j in range (1,2**leafs+1):
#         G.add_node(leafs+j)
#         G.add_edge(leafs,leafs+j)


        
    
    

        

# nx.draw(G)
# plt.draw()
# plt.show()


G=nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_node(10)
G.add_node(11)
# G.add_node(12)
# G.add_node(13)
# G.add_node(14)
# G.add_node(15)
# G.add_node(16)
# G.add_node(17)
# G.add_node(18)
# G.add_node(19)
# G.add_node(20)
# G.add_node(21)
# G.add_node(22)
# G.add_node(23)
# G.add_node(24)
# G.add_node(25)
# G.add_node(26)
# G.add_node(27)
# G.add_node(28)
# G.add_node(29)
# G.add_node(30)
# G.add_node(31)
# G.add_node(32)
# G.add_node(33)
# G.add_node(34)
# G.add_node(35)
# G.add_node(36)
# G.add_node(37)
# G.add_node(38)
# G.add_node(39)
# G.add_node(40)
# G.add_node(41)
# G.add_node(42)
# G.add_node(43)
# G.add_node(44)
# G.add_node(45)
# G.add_node(46)
# G.add_node(47)
# G.add_node(48)
# G.add_node(49)
# G.add_node(50)
# G.add_node(51)
# G.add_node(52)
# G.add_node(53)
# G.add_node(54)
# G.add_node(55)
# G.add_node(56)
# G.add_node(57)
# G.add_node(58)
# G.add_node(59)
# G.add_node(60)
# G.add_node(61)
# G.add_node(62)
# G.add_node(63)
# G.add_node(64)
# G.add_node(65)
# G.add_node(66)
# G.add_node(67)
# G.add_node(68)
# G.add_node(69)
# G.add_node(70)
# G.add_node(71)
# G.add_node(72)
# G.add_node(73)
# G.add_node(74)
# G.add_node(75)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,4)
G.add_edge(2,5)
G.add_edge(2,6)
G.add_edge(2,7)
G.add_edge(3,8)
G.add_edge(3,9)
G.add_edge(3,10)
G.add_edge(3,11)
# G.add_node(12)
# G.add_node(13)
# G.add_node(14)
# G.add_node(15)
# G.add_node(16)
# G.add_node(17)
# G.add_node(18)
# G.add_node(19)
# G.add_edge(4,12)
# G.add_edge(4,13)
# G.add_edge(4,14)
# G.add_edge(4,15)
# G.add_edge(4,16)
# G.add_edge(4,17)
# G.add_edge(4,18)
# G.add_edge(4,19)
array=[21,43,459, 581, 644, 838, 928, 1006, 1347, 1357, 1654, 1738, 1756, 1880, 1920, 2829, 2847, 3025, 3274, 3389, 3521, 3858, 3913, 3956, 4004, 4062, 4113, 4257, 4402, 4840, 4862, 4903, 4958, 5168, 5527, 5879, 6080, 6318, 6446, 6487, 6651, 6919, 7142, 7334, 7552, 7639, 7801, 7830, 8112, 8228, 8272, 8493, 8736, 8855, 9401, 9446, 9465, 9560, 9592, 9659, 9677]

for e,i in enumerate (range (4,12)):
    for j in range (1,2**3+1):
        G.add_edge(i,(8*e)+11+j)
    
labels={}
labels[1]=(21,9920)
labels[2]=(21,4598)
labels[3]=(5168,9920)
labels[4]=(21,1347)
labels[5]=(1352,2847)
labels[6]=(3025,4004)
labels[7]=(4062,4958)
labels[8]=  (5168,6651)
labels[9]=(6950,8112)
labels[10]=(8228,9465)
labels[11]=(9560,9920)
for i in range (61):
    labels[12+i]=array[i]
pos = hierarchy_pos(G,1)    

nx.draw_networkx_nodes(G, pos,node_color="tab:red")
nx.draw_networkx_nodes(G, pos, nodelist=[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], node_color="tab:blue")
nx.draw_networkx_edges(G,pos,width=2,alpha=0.5)
nx.draw_networkx_labels(G, pos, labels, font_size=8)

# nx.draw(G,pos,node_color='red')/
plt.draw()
plt.show()
