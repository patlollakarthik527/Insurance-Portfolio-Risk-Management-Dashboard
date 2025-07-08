import pandas as pd

def simulate_stress_event(df, region=None, peril=None, loss_multiplier=2.0):
    stressed_df = df.copy()
    if region:
        stressed_df.loc[stressed_df['region'] == region, 'expected_loss'] *= loss_multiplier
    if peril:
        stressed_df.loc[stressed_df['peril'] == peril, 'expected_loss'] *= loss_multiplier
    total_stressed_loss = stressed_df['expected_loss'].sum()
    return total_stressed_loss, stressed_df 