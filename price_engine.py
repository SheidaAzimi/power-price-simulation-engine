import numpy as np

class PriceEngine:

    def __init__(self, simulator):

        self.simulator = simulator

    def forecast(self, P0, T, dt):

        paths = self.simulator.simulate(P0, T, dt)

        expected_price = np.mean(paths[:, -1])

        price_std = np.std(paths[:, -1])

        return {
            "expected_price": expected_price,
            "price_std": price_std,
            "paths": paths
        }
