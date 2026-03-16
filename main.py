from jump_diffusion_model import JumpDiffusionModel
from monte_carlo_simulator import MonteCarloSimulator
from price_engine import PriceEngine

model = JumpDiffusionModel(
    kappa=1.2,
    mu=60,
    sigma=8,
    jump_intensity=0.4,
    jump_mean=15,
    jump_std=5
)

simulator = MonteCarloSimulator(model, n_simulations=2000)

engine = PriceEngine(simulator)

result = engine.forecast(
    P0=55,
    T=1,
    dt=1/252
)

print(result["expected_price"])
