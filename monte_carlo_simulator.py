import numpy as np

class MonteCarloSimulator:

    def __init__(self, model, n_simulations=1000):

        self.model = model
        self.n_simulations = n_simulations

    def simulate(self, P0, T, dt):

        simulations = []

        for i in range(self.n_simulations):

            path = self.model.simulate_path(P0, T, dt)

            simulations.append(path)

        return np.array(simulations)
