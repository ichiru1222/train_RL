class Planner():

    def __init__(self, env):
        self.env = env
        self.log = []

    def initialize(self):
        self.env.reset()
        self.log = []

    def plan(self, gamma=0.9, threshold=0.0001):
        raise Exception("Planner have to implements plan method.")

    def transitions_at(self, state, action):
        transiton_probs = self.env.transit_func(state, action) #type {next_state: prob, ...}
        for next_state in transiton_probs:
            prob = transiton_probs[next_state]
            reward, _ = self.env.reward_func(next_state)
            yield prob, next_state, reward
    
    def dict_to_grid(self, state_reward_dict):
        grid = []
        for i in range(self.env.row_length):
            row = [0] * self.env.column_length
            grid.append(row)
        for s in state_reward_dict:
            grid[s.row][s.column] = state_reward_dict[s]

        return grid

