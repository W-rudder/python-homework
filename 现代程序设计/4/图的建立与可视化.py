from GraphStat.Graph import *
from GraphStat.Visualization import plotgraph
from GraphStat.Visualization import plotnodes
filepath = r"C:\Users\86186\Desktop\现代程序设计\newmovies.txt"

nodelist=node.init_node(filepath)


edgelist=graph.init_edge(filepath)

graphlist=graph.init_graph(nodelist,edgelist)

#degree=stat.degreestat(graphlist)
#plotgraph.plotdegree(degree)
#weigh=stat.weighstat(graphlist)
#plotnodes.plotweigh(weigh)
#type=stat.typestat(graphlist)
#plotnodes.plottype(type)
plotgraph.plotgraph(filepath)


