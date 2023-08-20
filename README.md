# genetic_hvdc_graph
this code inspired by this reference (just topology implemented): https://ieeexplore.ieee.org/document/9204725

there some brief explaination about the topology:

Vertex Class (class Vertex): In the code, a Vertex class is defined. In the context of topology optimization, a vertex could represent a component or a node in the grid. The Vertex class is responsible for storing information about each node, such as its ID, adjacent nodes, and weights associated with edges (connections).

Graph Class (class Graph): The Graph class represents the entire grid or network in which topology optimization is performed. It contains methods to add vertices (nodes) and edges (connections) between them. This class allows you to create and manipulate the grid's structure, which is essential for topology optimization.

add_edge Method: In topology optimization, one of the primary tasks is to define and adjust connections between components or nodes. The add_edge method in the Graph class is used to add edges (connections) between vertices (nodes). The weight of these edges can represent properties of the grid, such as distances or costs, which are essential for optimization.

gen_to_graph Method: This method in the Graph class appears to generate a specific graph structure based on a binary input string (str). In topology optimization, this could be analogous to defining or modifying the connections between components based on certain optimization criteria, such as minimizing fault current.

Path and Index Calculations: The code includes methods like find_all_paths and fastest_path within the Graph class. These methods seem to calculate paths and indices within the graph, which could be relevant for evaluating different topologies during the optimization process. The paper discusses calculating indices for fault current levels, which may be related to the index calculations in these methods.

Constraints and Fitness Function: The paper mentions the application of constraints and a fitness function during the optimization process. While the code doesn't explicitly implement these aspects, it does provide the foundation for creating and evaluating different topologies (graphs), which are essential for constraint checking and fitness function evaluations.
