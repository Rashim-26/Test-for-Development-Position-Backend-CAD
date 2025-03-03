# ##################################################
# 1) Load workpiece graph and feature graph data from  json file
# ##################################################

# Note: Available files are: workpiece_graph.json, feature_graph.json
import json
import networkx as nx
from pyvis.network import Network

# Open and read the JSON file
with open('backend_application_test\\feature_graph.json', 'r') as file:
    feature_graph = json.load(file)

with open('backend_application_test\\workpiece_graph.json', 'r') as file:
    workpiece_graph = json.load(file)

# Print the data to see the structure
print(feature_graph)
print(workpiece_graph)

nt = Network(notebook=True) 

# TODO

# ##################################################
# 2) Create graphs from loaded data
# ##################################################

# Hint: The library networkx helps you to create a graph. You can use the nx.Graph() class to create a graph.
# Note: Other appraoches are also possible.

# Function to add nodes and edges from a graph
def add_graph_data(graph, color):
    for node in graph["nodes"]:
        node_id = node[0]
        node_data = node[1]
        nt.add_node(node_id, label=str(node_id), title=str(node_data), color=color)
    
    for edge in graph["edges"]:
        nt.add_edge(edge[0], edge[1], title=str(edge[2]))

# Add nodes and edges from both graphs with different colors
add_graph_data(feature_graph, "blue")      # Feature graph in blue
add_graph_data(workpiece_graph, "green")   # Workpiece graph in green

# Disable physics to keep layout stable
nt.toggle_physics(False)

# Save and display the graph
nt.show("My_graph.html")  # Optional Task

# TODO

# Note: Optional task - Visualize the graph
# Example code:
# from pyvis.network import Network
# nt = Network()
# nt.from_nx(workpiece_graph)
# nt.show("graph.html", notebook=False)

# ##################################################
# 3) Check if the feature graph is a subgraph of the workpiece workpiece and find any other matching subgraphs
# ##################################################


# TODO

# ##################################################
# 4) Results
# ##################################################

# Print results if matches are found. Return the number of matches and the node ids.

# TODO
