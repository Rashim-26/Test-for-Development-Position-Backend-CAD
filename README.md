# Test-for-Development-Position-Backend-CAD
## Overview
This repository contains the solution for reading and processing graph data representing a workpiece and its feature graph. The workpiece graph contains nodes (surfaces) and edges (connections between surfaces), while the feature graph is a smaller subgraph of the workpiece, representing a specific feature.
### Tasks Completed
1. **Task 1: Create a New Repository and Setup Graph Data**
   - Created a new repository based on the provided content.
2. **Task 2: Read Graph Data from JSON Files and Create Graph Objects in Python**
   - Read the graph data from `workpiece_graph.json` and `feature_graph.json` files.
   - Used **networkx** to create graph objects from the JSON data.
     - Nodes represent the surfaces of the workpiece and are categorized into types like **cylinder**, **cone**, or **plane**.
     - Edges define the connections between these surfaces and include attributes such as **angular_type** (e.g., **convex**, **concave**).
   - Implemented the graph creation logic in `graph_search_task.py` under the following sections:
     - **1)** Reading the JSON files and loading the graph data.
     - **2)** Creating graph objects and setting node and edge attributes.
    
     - Optional Task: Also implemented the visualization of the Graph
