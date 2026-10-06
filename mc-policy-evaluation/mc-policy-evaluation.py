import numpy as np

def mc_policy_evaluation(episodes: list, gamma: float, n_states: int) -> np.ndarray:
    """
    Returns the state values as a NumPy array of length n_states,
    calculated via First-Visit Monte Carlo evaluation and rounded to 4 decimal places.
    """
    returns_sum = np.zeros(n_states, dtype=float)
    returns_count = np.zeros(n_states, dtype=int)
    
    for episode in episodes:
        # Step 1: Calculate discounted returns backwards for efficiency
        G = 0.0
        returns = [0.0] * len(episode)
        
        for t in reversed(range(len(episode))):
            _, reward = episode[t]
            G = reward + gamma * G
            returns[t] = G
            
        # Step 2: Track first-visit for each state in the episode
        visited_states = set()
        for t, (state, _) in enumerate(episode):
            if state not in visited_states:
                visited_states.add(state)
                returns_sum[state] += returns[t]
                returns_count[state] += 1
                
    # Step 3: Compute mean return for each state
    state_values = np.zeros(n_states, dtype=float)
    non_zero_mask = returns_count > 0
    state_values[non_zero_mask] = returns_sum[non_zero_mask] / returns_count[non_zero_mask]
    
    return np.round(state_values, 4)