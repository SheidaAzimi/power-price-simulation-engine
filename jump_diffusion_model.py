import numpy as np

class JumpDiffusionModel:

    def __init__(self, kappa, mu, sigma, jump_intensity, jump_mean, jump_std):

        self.kappa = kappa
        self.mu = mu
        self.sigma = sigma

        self.jump_intensity = jump_intensity
        self.jump_mean = jump_mean
        self.jump_std = jump_std

    def simulate_path(self, P0, T, dt):

        steps = int(T / dt)
        prices = np.zeros(steps)

        prices[0] = P0

        for t in range(1, steps):

            prev_price = prices[t-1]

            drift = self.kappa * (self.mu - prev_price) * dt

            diffusion = self.sigma * np.sqrt(dt) * np.random.normal()

            jump = 0

            if np.random.poisson(self.jump_intensity * dt) > 0:

              if np.random.rand() < 0.8:
                 jump = np.random.normal(20, 5)   # upward spike
            else:
                 jump = np.random.normal(-5, 2)   # downward spike

            prices[t] = prev_price + drift + diffusion + jump

        return prices
