import rlhw.agent as agents
from rlhw.env import env_builder
from rlhw.valueiter import FLVI
import numpy as np


def main():
    map_name = "8x8"
    is_slippery = True
    params = {
        "render": False,
        "discount_factor": 0.95,
        "epsilon": 1,
        "epsilon_decay": .99999999999999999999999999999999,
        "min_epsilon": 0.01,
        "learning_rate": 1,
        "min_learning_rate": 0.01,
        "learning_rate_decay": .99999999999999999999999999999999,
    }
    build_env = env_builder(
        "FrozenLake-v1", {"map_name": map_name, "is_slippery": is_slippery}
    )
    agent = agents.QLearningAgent(build_env, params)
    agent.run(10000, 100, True)
    eval_res = agent.run(100, 100, False)
    total = sum(list(eval_res.values()))
    success_rate = total / 100.0
    print(f"success_rate: {success_rate}")

    np.set_printoptions(suppress=True)
    learned = np.max(agent.policy, axis=1)
    print("Learned state values:\n", learned)
    computed = FLVI(map_name, params["discount_factor"], is_slippery)
    print("True state values:\n", computed)
    print("Value error norm: ", np.linalg.norm(learned - computed))


if __name__ == "__main__":
    main()
