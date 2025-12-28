import numpy as np
import pandas as pd

np.random.seed(42)

N = 5000

data = {
    "order_id": range(1, N + 1),
    "order_hour": np.random.randint(0, 24, N),
    "distance_km": np.round(np.random.uniform(0.5, 15, N), 2),
    "prep_time_min": np.random.randint(5, 40, N),
    "delivery_time_min": np.random.randint(15, 90, N),
    "order_value": np.round(np.random.uniform(5, 60, N), 2),
    "surge_multiplier": np.round(np.random.choice([1, 1.2, 1.5, 2.0], N, p=[0.6, 0.2, 0.15, 0.05]), 2),
    "rating": np.round(np.random.normal(4.2, 0.5, N), 1),
    "cuisine": np.random.choice(
        ["Italian", "Chinese", "Indian", "Mexican", "American", "Thai"], N
    ),
    "traffic_level": np.random.choice(
        ["Low", "Medium", "High"], N, p=[0.4, 0.4, 0.2]
    ),
    "weather": np.random.choice(
        ["Clear", "Rain", "Storm"], N, p=[0.7, 0.2, 0.1]
    ),
}

df = pd.DataFrame(data)

df["rating"] = df["rating"].clip(1, 5)

df.to_csv("data/uber_eats_orders.csv", index=False)

print("Dataset generated successfully.")
