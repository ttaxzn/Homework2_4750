class VacuumState:
    def __init__(self, dirt_loc, vacuum_loc, depth, path, path_cost, parent, state_index):
        self.dirt_loc = dirt_loc  # Location
        self.vacuum_loc = vacuum_loc  # Vacuum location
        self.depth = depth  # Depth of the node
        self.path = path  # Path
        self.path_cost = path_cost  # Path cost
        self.parent = parent  # Parent reference
        self.state_index = state_index  # State index list

    def is_goal_state(self):
        return len(self.dirt_loc) == 0 

    def __eq__(self, other):
        return self.vacuum_loc == other.vacuum_loc and set(self.dirt_loc) == set(other.dirt_loc)

    def __lt__(self, other):
        return self.path_cost < other.path_cost
    
    def __hash__(self):
        return hash((self.vacuum_loc, frozenset(self.dirt_loc)))
