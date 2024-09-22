from heapq import heappush, heappop
from vacuum_state import VacuumState
from vacuum_tree import VacuumTree
import time

# Uniform cost tree search
def uniform_cost_tree_search(initial_dirt_loc, initial_vacuum_loc):
    tree = VacuumTree(initial_dirt_loc, initial_vacuum_loc)
    start_time = time.time()

    nodes_expanded = 0
    while tree.fringe:
        _, current_index = heappop(tree.fringe)  # Pop node with lowest cost
        current_state = tree.state_list[current_index]

        if current_state.is_goal_state():
            end_time = time.time()
            return current_state, nodes_expanded, len(tree.state_list), end_time - start_time  # Found solution

        nodes_expanded += 1
        successors = tree.expand(current_index)
        for succ_index in successors:
            successor = tree.state_list[succ_index]
            heappush(tree.fringe, (successor.path_cost, succ_index))  # Push to fringe based on path cost

# Uniform cost graph search
def uniform_cost_graph_search(initial_dirt_loc, initial_vacuum_loc):
    tree = VacuumTree(initial_dirt_loc, initial_vacuum_loc)
    closed = set()
    start_time = time.time()

    nodes_expanded = 0
    while tree.fringe:
        _, current_index = heappop(tree.fringe)
        current_state = tree.state_list[current_index]

        if current_state.is_goal_state():
            end_time = time.time()
            return current_state, nodes_expanded, len(tree.state_list), end_time - start_time

        if current_state not in closed:
            closed.add(current_state)
            nodes_expanded += 1
            successors = tree.expand(current_index)
            for succ_index in successors:
                successor = tree.state_list[succ_index]
                heappush(tree.fringe, (successor.path_cost, succ_index))

# Iterative deepening tree search
def iterative_deepening_tree_search(initial_dirt_loc, initial_vacuum_loc, max_depth):
    start_time = time.time() 
    for depth_limit in range(max_depth):
        result = depth_limited_search(initial_dirt_loc, initial_vacuum_loc, depth_limit)
        if result is not None:
            end_time = time.time() 
            solution, expanded, generated = result
            time_taken = end_time - start_time
            return solution, expanded, generated, time_taken 
    return None, 0, 0, 0  # Failure in case no solution is found

# Depth limited search for iterative deepening tree search to use
def depth_limited_search(initial_dirt_loc, initial_vacuum_loc, depth_limit):
    tree = VacuumTree(initial_dirt_loc, initial_vacuum_loc)
    nodes_expanded = 0

    while tree.fringe:
        _, current_index = heappop(tree.fringe)
        current_state = tree.state_list[current_index]

        if current_state.is_goal_state():
            return current_state, nodes_expanded, len(tree.state_list)

        if current_state.depth < depth_limit:
            nodes_expanded += 1
            successors = tree.expand(current_index)
            for succ_index in successors:
                successor = tree.state_list[succ_index]
                heappush(tree.fringe, (successor.path_cost, succ_index))

    return None