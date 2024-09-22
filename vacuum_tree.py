from vacuum_state import VacuumState
from heapq import heappush, heappop
class VacuumTree:
    def __init__(self, initial_dirt_loc, initial_vacuum_loc):
        initial_state = VacuumState(initial_dirt_loc, initial_vacuum_loc, 0, [], 0, None, 0)
        self.state_list = [initial_state] 
        self.fringe = []  # Queue for fringe
        heappush(self.fringe, (0, 0))  # Push to fringe
        self.solution = None  # Placeholder for solution

    def take_action(self, state_index, action):
        movements = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)] 
        costs = [0.6, 0.8, 0.7, 0.9, 1.0]

        parent_state = self.state_list[state_index]
        new_vacuum_loc = (parent_state.vacuum_loc[0] + movements[action][0],
                          parent_state.vacuum_loc[1] + movements[action][1])

        if not (1 <= new_vacuum_loc[0] <= 4 and 1 <= new_vacuum_loc[1] <= 5):
            return None  # Invalid move

        new_dirt_loc = parent_state.dirt_loc.copy()
        if action == 0 and new_vacuum_loc in new_dirt_loc:
            new_dirt_loc.remove(new_vacuum_loc)

        new_depth = parent_state.depth + 1
        new_path = parent_state.path + [action]
        new_path_cost = parent_state.path_cost + costs[action]
        new_state = VacuumState(new_dirt_loc, new_vacuum_loc, new_depth, new_path, new_path_cost, state_index, len(self.state_list))

        self.state_list.append(new_state)
        return len(self.state_list) - 1 

    def expand(self, state_index):
        successors = []
        for action in range(5): 
            child_index = self.take_action(state_index, action)
            if child_index is not None:
                successors.append(child_index)
        return successors