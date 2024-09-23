from vacuum_cleaner_world import uniform_cost_tree_search, uniform_cost_graph_search, iterative_deepening_tree_search

if __name__ == "__main__":
    # Instances initalization
    instance_1_dirt = [(1, 2), (2, 4), (3, 5)]
    instance_1_vacuum = (2, 2)

    instance_2_dirt = [(1, 2), (2, 1), (2, 4), (3, 3)]
    instance_2_vacuum = (3, 2)

    print("*** Instance 1 ***")
    
    # Uniform Cost Tree Search for Instance 1
    print("Uniform Cost Tree Search for Instance 1...")
    solution, expanded, generated, time_taken = uniform_cost_tree_search(instance_1_dirt, instance_1_vacuum)
    print(f"Solution: {solution.path}, Moves: {len(solution.path)}, Cost: {solution.path_cost}")
    print(f"Nodes expanded: {expanded}, Nodes generated: {generated}, Time taken: {time_taken:.4f} seconds\n")

    # Uniform Cost Graph Search for Instance 1
    print("Uniform Cost Graph Search for Instance 1...")
    solution, expanded, generated, time_taken = uniform_cost_graph_search(instance_1_dirt, instance_1_vacuum)
    print(f"Solution: {solution.path}, Moves: {len(solution.path)}, Cost: {solution.path_cost}")
    print(f"Nodes expanded: {expanded}, Nodes generated: {generated}, Time taken: {time_taken:.4f} seconds\n")

    # Iterative Deepening Tree Search for Instance 1
    max_depth = 50  # Setting a max depth
    print("Iterative Deepening Tree Search for Instance 1...")
    solution, expanded, generated, time_taken = iterative_deepening_tree_search(instance_1_dirt, instance_1_vacuum, max_depth)
    print(f"Solution: {solution.path}, Moves: {len(solution.path)}, Cost: {solution.path_cost}")
    print(f"Nodes expanded: {expanded}, Nodes generated: {generated}, Time taken: {time_taken:.4f} seconds\n")


    print("*** Instance 2 ***")
    
    # Uniform Cost Tree Search for Instance 2
    print("Uniform Cost Tree Search for Instance 2...")
    solution, expanded, generated, time_taken = uniform_cost_tree_search(instance_2_dirt, instance_2_vacuum)
    print(f"Solution: {solution.path}, Moves: {len(solution.path)}, Cost: {solution.path_cost}")
    print(f"Nodes expanded: {expanded}, Nodes generated: {generated}, Time taken: {time_taken:.4f} seconds\n")

    # Uniform Cost Graph Search for Instance 2
    print("Uniform Cost Graph Search for Instance 2...")
    solution, expanded, generated, time_taken = uniform_cost_graph_search(instance_2_dirt, instance_2_vacuum)
    print(f"Solution: {solution.path}, Moves: {len(solution.path)}, Cost: {solution.path_cost}")
    print(f"Nodes expanded: {expanded}, Nodes generated: {generated}, Time taken: {time_taken:.4f} seconds\n")

    # Iterative Deepening Tree Search for Instance 2
    max_depth = 50  # Setting a max depth
    print("Iterative Deepening Tree Search for Instance 2...")
    solution, expanded, generated, time_taken = iterative_deepening_tree_search(instance_2_dirt, instance_2_vacuum, max_depth)
    print(f"Solution: {solution.path}, Moves: {len(solution.path)}, Cost: {solution.path_cost}")
    print(f"Nodes expanded: {expanded}, Nodes generated: {generated}, Time taken: {time_taken:.4f} seconds\n")
