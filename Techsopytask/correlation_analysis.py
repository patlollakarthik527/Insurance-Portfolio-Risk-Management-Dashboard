import pandas as pd

def compute_correlation_matrix(df):
    numeric_cols = ['sum_insured', 'premium', 'probability_of_loss', 'expected_loss']
    return df[numeric_cols].corr()

def detect_risk_concentration(df, threshold=0.2):
    region_concentration = df.groupby('region')['expected_loss'].sum() / df['expected_loss'].sum()
    peril_concentration = df.groupby('peril')['expected_loss'].sum() / df['expected_loss'].sum()
    high_region = region_concentration[region_concentration > threshold]
    high_peril = peril_concentration[peril_concentration > threshold]
    return high_region, high_peril 