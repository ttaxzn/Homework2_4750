from heapq import heappush, heappop
from vacuum_state import VacuumState
from vacuum_tree import VacuumTree
import time

def uniform_cost_tree_search(initial_dirt_loc, initial_vacuum_loc):
    tree = VacuumTree(initial_dirt_loc, initial_vacuum_loc)
    start_time = time.time()

    nodes_expanded = 0
    states_printed = 0  # Counter for the first 5 states

    while tree.fringe:
        _, current_index = heappop(tree.fringe)  # Pop node with lowest cost
        current_state = tree.state_list[current_index]

        if states_printed < 5:
            print(f"State {states_printed + 1}: Vacuum location: {current_state.vacuum_loc}, Dirt locations: {current_state.dirt_loc}, Path cost: {current_state.path_cost}")
            states_printed += 1

        if current_state.is_goal_state():
            end_time = time.time()
            return current_state, nodes_expanded, len(tree.state_list), end_time - start_time

        nodes_expanded += 1

        # Expanding to adjacent rooms only
        valid_moves = tree.expand(current_index)
        for move in valid_moves:  # Ensure we only move one room at a time
            if abs(tree.state_list[move].vacuum_loc[0] - tree.state_list[current_index].vacuum_loc[0]) + \
               abs(tree.state_list[move].vacuum_loc[1] - tree.state_list[current_index].vacuum_loc[1]) == 1:  
                heappush(tree.fringe, (tree.state_list[move].path_cost, move))

    end_time = time.time()
    return None, nodes_expanded, len(tree.state_list), end_time - start_time


# Uniform cost graph search
def uniform_cost_graph_search(initial_dirt_loc, initial_vacuum_loc):
    tree = VacuumTree(initial_dirt_loc, initial_vacuum_loc)
    start_time = time.time()

    states_printed = 0  # Counter for first 5 states
    nodes_expanded = 0
    closed = set()

    while tree.fringe:
        _, current_index = heappop(tree.fringe)
        current_state = tree.state_list[current_index]

        if states_printed < 5:
            print(f"State {states_printed + 1}: Vacuum location: {current_state.vacuum_loc}, Dirt locations: {current_state.dirt_loc}, Path cost: {current_state.path_cost}")
            states_printed += 1

        if current_state.is_goal_state():
            end_time = time.time()
            return current_state, nodes_expanded, len(tree.state_list), end_time - start_time

        if current_state not in closed:
            closed.add(current_state)
            nodes_expanded += 1

            for child_index in tree.expand(current_index):
                child_state = tree.state_list[child_index]
                heappush(tree.fringe, (child_state.path_cost, child_index))

    end_time = time.time()
    return None, nodes_expanded, len(tree.state_list), end_time - start_time

# Iterative deepening tree search
def iterative_deepening_tree_search(initial_dirt_loc, initial_vacuum_loc, max_depth):
    tree = VacuumTree(initial_dirt_loc, initial_vacuum_loc)
    start_time = time.time()

    states_printed = 0  # Counter for first 5 states
    nodes_expanded = 0

    for depth_limit in range(max_depth + 1):
        tree.fringe = [(0, 0)]
        tree.state_list = [tree.state_list[0]]
        closed = set()

        while tree.fringe:
            _, current_index = heappop(tree.fringe)
            current_state = tree.state_list[current_index]

            if states_printed < 5:
                print(f"State {states_printed + 1}: Vacuum location: {current_state.vacuum_loc}, Dirt locations: {current_state.dirt_loc}, Path cost: {current_state.path_cost}")
                states_printed += 1

            if current_state.is_goal_state():
                end_time = time.time()
                return current_state, nodes_expanded, len(tree.state_list), end_time - start_time

            if current_state not in closed and current_state.depth <= depth_limit:
                closed.add(current_state)
                nodes_expanded += 1

                for child_index in tree.expand(current_index):
                    child_state = tree.state_list[child_index]
                    heappush(tree.fringe, (child_state.path_cost, child_index))

    end_time = time.time()
    return None, nodes_expanded, len(tree.state_list), end_time - start_time
