import pandas as pd

def calculate_expected_loss(df):
    df['expected_loss'] = df['sum_insured'] * df['probability_of_loss']
    return df

def aggregate_portfolio_risk(df):
    total_expected_loss = df['expected_loss'].sum()
    return total_expected_loss 