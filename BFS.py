# Created a function Readgraph which takes a file as a parameter and opens the file. 
# File.readline function reads all lines and returns them as a list of string. 
# For loop is then run on the lines of file and strip function removes spaces.
# Then an if statement is started which checks if the line is not empty if not then split line into strings for each index, as the start node is the first index in line start node =[0] and similarly the end node 
# then another if statement is started inside which checks for the start node in the dictionary of graph, if its not there it just creates a list start node and appends its end nodes
# Then created the Bfs function which receives 3 parameters 
# and a queue is initialised as a tuple containing the initial node 
# and a list of that initial node which represents the path 
# then an empty list is initialised which keeps a track of nodes visited 
# while loop runs untill all the nodes are explored in the queue
# and the first element is picked up from the start of the queue using queue.pop(0) and assighned it to the variable current_node, path
# and if the current node == to the goal node  return its path 
# if not, then add the current node into visited list
# The neighbors of the current_node are retrieved from the graph using graph.get(current_node, []).
# If the current_node does not exist as a key in the graph dictionary, an empty list is returned.
# then a for loop is




def ReadGraph(file):
    graph = {}
    with open(file, 'r') as my_file:
        whole_text = my_file.readlines()
        for line in whole_text:
            line = line.strip()
            if line:
                key = line.split()
                start_node = key[0]
                end_node = key[4]
                if start_node not in graph:
                    graph[start_node] = []
                graph[start_node].append(end_node)
    return graph

def bfs(graph, initial_node, goal_node):
    queue = [(initial_node, [initial_node])]
    visited = []
    while queue:
        current_node, path = queue.pop(0)
        if current_node == goal_node:
            return path
        if current_node not in visited:
            visited.append(current_node)
            neighbors = graph.get(current_node, [])
            for neighbour in neighbors:
                queue.append((neighbour, path + [neighbour]))
    print("No Path found!")



graph = ReadGraph('Graph_info.txt')
initial_node = input("Please enter the initial node(starting with hash) >> ") 
goal_node = input("Please enter the goal node(starting with hash) >> ")

bfs_path = bfs(graph, initial_node, goal_node)

print("BFS Path:", bfs_path)
