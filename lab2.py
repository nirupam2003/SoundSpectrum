import heapq

# Define the goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Define the initial state
initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)

# Define a function to calculate the number of misplaced tiles (heuristic)
def misplaced_tiles(state):
    return sum(1 for i, j in zip(state, goal_state) if i != j)

# Define a function to find the valid moves for the empty tile
def get_valid_moves(state):
    moves = []
    empty_tile_index = state.index(0)
    if empty_tile_index % 3 > 0:
        moves.append(-1)  # Move left
    if empty_tile_index % 3 < 2:
        moves.append(1)   # Move right
    if empty_tile_index >= 3:
        moves.append(-3)  # Move up
    if empty_tile_index < 6:
        moves.append(3)   # Move down
    return moves

# Define the A* search algorithm
def astar(initial_state):
    open_set = [(misplaced_tiles(initial_state), initial_state)]
    closed_set = set()
    came_from = {}
    g_score = {initial_state: 0}
    f_score = {initial_state: g_score[initial_state] + misplaced_tiles(initial_state)}

    while open_set:
        current_f, current_state = heapq.heappop(open_set)

        if current_state == goal_state:
            path = [current_state]
            while current_state in came_from:
                current_state = came_from[current_state]
                path.insert(0, current_state)
            return path

        closed_set.add(current_state)

        for move in get_valid_moves(current_state):
            new_state = list(current_state)
            empty_tile_index = new_state.index(0)
            new_tile_index = empty_tile_index + move
            new_state[empty_tile_index], new_state[new_tile_index] = new_state[new_tile_index], new_state[empty_tile_index]
            new_state = tuple(new_state)

            tentative_g_score = g_score[current_state] + 1

            if new_state in closed_set and tentative_g_score >= g_score.get(new_state, 0):
                continue

            if tentative_g_score < g_score.get(new_state, 0) or new_state not in [state for (_, state) in open_set]:
                came_from[new_state] = current_state
                g_score[new_state] = tentative_g_score
                f_score[new_state] = g_score[new_state] + misplaced_tiles(new_state)
                heapq.heappush(open_set, (f_score[new_state], new_state))

    return None

# Solve the 8-puzzle problem
solution = astar(initial_state)

if solution:
    print("Solution found!")
    for step, state in enumerate(solution):
        print(f"Step {step}:\n")
        for i in range(3):
            print(state[i * 3:i * 3 + 3])
        print("\n")
else:
    print("No solution found.")
