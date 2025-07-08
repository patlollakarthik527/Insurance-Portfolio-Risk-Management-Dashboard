import pandas as pd
import numpy as np

def generate_mock_data(num_policies=1000):
    np.random.seed(42)
    policy_types = ['Home', 'Auto', 'Life', 'Health', 'Commercial']
    regions = ['North', 'South', 'East', 'West']
    perils = ['Fire', 'Flood', 'Theft', 'Accident', 'Illness']
    data = {
        'policy_id': np.arange(1, num_policies + 1),
        'policy_type': np.random.choice(policy_types, num_policies),
        'sum_insured': np.random.randint(10000, 1000000, num_policies),
        'region': np.random.choice(regions, num_policies),
        'peril': np.random.choice(perils, num_policies),
        'premium': np.random.randint(200, 10000, num_policies),
        'probability_of_loss': np.round(np.random.uniform(0.001, 0.05, num_policies), 4)
    }
    return pd.DataFrame(data) 