import streamlit as st
import pandas as pd
from data_loader import generate_mock_data
from risk_calculator import calculate_expected_loss, aggregate_portfolio_risk
from correlation_analysis import compute_correlation_matrix, detect_risk_concentration
from stress_testing import simulate_stress_event
import io

st.set_page_config(page_title='Insurance Portfolio Risk Dashboard', layout='wide')
st.title('Insurance Portfolio Risk Management Dashboard')

st.sidebar.header('Data Source')
uploaded_file = st.sidebar.file_uploader('Upload Policy Data (CSV)', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success('Custom policy data loaded!')
else:
    df = generate_mock_data(1000)
    st.info('Using mock data. Upload a CSV to analyze your own portfolio.')

df = calculate_expected_loss(df)
total_expected_loss = aggregate_portfolio_risk(df)

st.sidebar.header('Stress Test Scenario')
region = st.sidebar.selectbox('Select Region for Stress Test', ['None'] + sorted(df['region'].unique().tolist()))
peril = st.sidebar.selectbox('Select Peril for Stress Test', ['None'] + sorted(df['peril'].unique().tolist()))
loss_multiplier = st.sidebar.slider('Loss Multiplier', 1.0, 5.0, 2.0, 0.1)

corr_matrix = compute_correlation_matrix(df)

high_region, high_peril = detect_risk_concentration(df, threshold=0.2)

stress_region = region if region != 'None' else None
stress_peril = peril if peril != 'None' else None
total_stressed_loss, stressed_df = simulate_stress_event(df, region=stress_region, peril=stress_peril, loss_multiplier=loss_multiplier)

col1, col2 = st.columns(2)
with col1:
    st.metric('Total Expected Loss', f"${total_expected_loss:,.0f}")
    st.metric('Stressed Portfolio Loss', f"${total_stressed_loss:,.0f}")
    st.subheader('Risk Concentration by Region')
    st.bar_chart(df.groupby('region')['expected_loss'].sum())
    if not high_region.empty:
        st.warning(f"High risk concentration in regions: {', '.join(high_region.index)}")
with col2:
    st.subheader('Risk Concentration by Peril')
    st.bar_chart(df.groupby('peril')['expected_loss'].sum())
    if not high_peril.empty:
        st.warning(f"High risk concentration in perils: {', '.join(high_peril.index)}")
    st.subheader('Correlation Matrix')
    st.dataframe(corr_matrix)

st.subheader('Sample Policy Data')
st.dataframe(df.head(20))

st.subheader('Download Risk Report')
report_buffer = io.StringIO()
df.to_csv(report_buffer, index=False)
st.download_button(
    label='Download Portfolio Risk Report (CSV)',
    data=report_buffer.getvalue(),
    file_name='portfolio_risk_report.csv',
    mime='text/csv'
) 