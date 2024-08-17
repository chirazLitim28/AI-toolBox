import networkx as nx
import matplotlib.pyplot as plt
import heapq
from IPython.display import clear_output
import time

# Code of search algorithms
def breadth_first_search(graph, source_node, goal_node, ax):
    visited = set()
    queue = [(source_node, None)]
    visited.add(source_node)

    # Initialize edge colors to default
    for edge in graph.edges:
        graph.edges[edge]['color'] = 'black'
    ax.clear()
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold',
                    edge_color=[graph.edges[edge]['color'] for edge in graph.edges], ax=ax)
    plt.pause(2)
    path = []
    while queue:
        current_node, parent_node = queue.pop(0)
        path.append(current_node)
        print("Visiting node:", current_node)
  
        if parent_node is not None:
            graph.edges[parent_node, current_node]['color'] = 'yellow'  # Highlight the visited edge
            ax.clear()
            pos = nx.spring_layout(graph, seed=42)
            nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold',
                    edge_color=[graph.edges[edge]['color'] for edge in graph.edges], ax=ax)
            plt.pause(2)

        if current_node == goal_node:
            break

        neighbors = graph.neighbors(current_node)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, current_node))

    if goal_node in path:
        print("Path found:", path)
    else:
        print("Goal node is not reachable from the start node.")

def depth_first_search(graph, source_node, goal_node,ax):
    visited = set()

    def dfs(node, parent_node):
        path.append(node)
        print("Visiting node:", node)
        

        if parent_node is not None:
            graph.edges[parent_node, node]['color'] = 'yellow'  # Highlight the visited edge
            ax.clear()
            pos = nx.spring_layout(graph, seed=42)
            nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold',
                    edge_color=[graph.edges[edge]['color'] for edge in graph.edges], ax=ax)
            plt.pause(2)

        if node == goal_node:
            return

        visited.add(node)
        neighbors = graph.neighbors(node)
        for neighbor in neighbors:
            if neighbor not in visited:
                dfs(neighbor, node)

    # Initialize edge colors to default
    for edge in graph.edges:
        graph.edges[edge]['color'] = 'black'
    ax.clear()
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold',
                    edge_color=[graph.edges[edge]['color'] for edge in graph.edges], ax=ax)
    plt.pause(2)
   

    path = []
    dfs(source_node, None)

    if goal_node in path:
        print("Path found:", path)
    else:
        print("Goal node is not reachable from the start node.")

def h(Node):
        heuristic={}
        file = open("heuristic.txt", 'r')
        data = file.readlines()
        for line in data:
            node,value= line.split()
            node = int(node)
            value = int(value)
            heuristic[node]=value
        print(heuristic)
        return heuristic[Node]

def astar_search(graph, source_node, goal_node,ax):
    visited = set()
    queue = [(0, source_node, None)]  # (f-score, node, parent)
    visited.add(source_node)

    # Initialize edge colors to default
    for edge in graph.edges:
        graph.edges[edge]['color'] = 'black'

    ax.clear()
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold',
                    edge_color=[graph.edges[edge]['color'] for edge in graph.edges], ax=ax)
    plt.pause(2)

    path = []
    while queue:
        f_score, current_node, parent_node = heapq.heappop(queue)
        path.append(current_node)
        print("Visiting node:", current_node)
        # Perform necessary operations during the search process
        # ...

        if parent_node is not None:
            graph.edges[parent_node, current_node]['color'] = 'yellow'  # Highlight the visited edge
            ax.clear()
            pos = nx.spring_layout(graph, seed=42)
            nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold',
                    edge_color=[graph.edges[edge]['color'] for edge in graph.edges], ax=ax)
            plt.pause(2)

        if current_node == goal_node:
            break

        neighbors = graph.neighbors(current_node)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                g_score = 1  # Replace with the actual cost between nodes
                h_score = h(current_node)
                f_score = g_score + h_score
                heapq.heappush(queue, (f_score, neighbor, current_node))

    if goal_node in path:

        print("Path found:", path)
    else:
        print("Goal node is not reachable from the start node.")
        

 
def path_cost(path):
    total_cost = 0
    for node, cost in path:
        total_cost += cost
    return total_cost, path[-1][0]

def ucs(graph, start, goal):
    visited = set()
    queue = [[(start, 0)]]

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
    plt.show()
    time.sleep(1)

    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node, cost = path[-1]
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            # Highlight the path to the goal
            for i in range(len(path) - 1):
                current_node, _ = path[i]
                next_node, _ = path[i + 1]
                if graph.has_edge(current_node, next_node):
                    graph.edges[current_node, next_node]['color'] = 'yellow'
                nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold',
                        edge_color=[graph.edges[edge].get('color', 'black') for edge in graph.edges])
                plt.text(pos[current_node][0], pos[current_node][1] - 0.1, f'Cost: {path[i][1]}', horizontalalignment='center')
                plt.show()
                time.sleep(1)
                clear_output(wait=True)

            return path

        adjacent_nodes = graph.neighbors(node)
        for node2 in adjacent_nodes:
            edge_data = graph.get_edge_data(node, node2)
            if edge_data:
                edge_cost = edge_data['cost']
                new_path = path.copy()
                new_path.append((node2, cost + edge_cost))
                queue.append(new_path)

    return None
    
def create_graph():
    graph = nx.Graph()
    # num_edges = sum(1 for _ in open('graph.txt'))
    file = open("graph.txt", 'r')
    data = file.readlines()
    for line in data:
        node1,node2,weight = line.split()
        node1 = int(node1)
        node2 = int(node2)
        weight = int(weight)
        graph.add_edge(node1, node2, cost=weight)

    return graph

def visualize(start_node,goal_node,algorithm_choice):
    
    print(start_node)
    graph = create_graph()
    
    fig, ax = plt.subplots()
    if algorithm_choice == "A* Search":
        astar_search(graph, start_node, goal_node,ax)
    elif algorithm_choice == "Breadth First Search":
        breadth_first_search(graph, start_node, goal_node,ax)
    elif algorithm_choice == "Deapth First Search":
        depth_first_search(graph, start_node, goal_node,ax)
    elif algorithm_choice == "Uniform Cost Search":
        ucs(graph, start_node, goal_node)
  
     
    
    
    
    




