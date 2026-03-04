import random
import copy # Needed to clone the game state

def generate_level_iterative(target_requirements, max_slots, num_lanes):
    # 1. Define the Initial State
    initial_state = {
        'targets_left': target_requirements.copy(), # e.g., ['Shrimp', 'Egg', ...]
        'buffer': [],
        'lanes': [ [] for _ in range(num_lanes) ]
    }
    
    # 2. Initialize the DFS Stack
    dfs_stack = [initial_state]
    
    # 3. The Main Search Loop
    while dfs_stack:
        # Pop the most recent state (LIFO -> Depth First)
        current_state = dfs_stack.pop()
        
        # Win Condition Check
        if not current_state['targets_left'] and not current_state['buffer']:
            # We found a valid generation path!
            return current_state['lanes']
            
        # Find all valid moves from this exact state
        valid_next_states = []
        
        # Move A: Target -> Buffer (Un-solve)
        if current_state['targets_left'] and len(current_state['buffer']) < max_slots:
            # CREATE A CLONE OF THE STATE
            new_state = copy.deepcopy(current_state)
            item = new_state['targets_left'].pop()
            new_state['buffer'].append(item)
            valid_next_states.append(new_state)
            
        # Move B: Buffer -> Lane (Un-pop)
        if current_state['buffer']:
            # In a real game, you'd pick a random lane. Let's try all valid lanes.
            for lane_index in range(num_lanes):
                # Optional: check if lane reached max height here
                
                # CREATE A CLONE OF THE STATE
                new_state = copy.deepcopy(current_state)
                # Pick a random item from buffer to bury
                item_idx = random.randint(0, len(new_state['buffer']) - 1)
                item = new_state['buffer'].pop(item_idx)
                
                # Insert at index 0 (bottom-to-top building)
                new_state['lanes'][lane_index].insert(0, item) 
                valid_next_states.append(new_state)
                
        # Shuffle the valid next states to ensure randomness, then push to stack
        random.shuffle(valid_next_states)
        for state in valid_next_states:
            dfs_stack.append(state)
            
    # If the while loop finishes and we never returned, it's impossible.
    
    return "Generation Failed - No valid path found."

if __name__ == "__main__":
    print("test")