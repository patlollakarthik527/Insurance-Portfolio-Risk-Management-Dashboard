# Insurance Portfolio Risk Management Dashboard

A modular, interactive dashboard for monitoring, analyzing, and stress-testing risk exposure across an insurance company’s entire policy portfolio.

---

## Overview

This project provides a user-friendly dashboard to help insurance companies and analysts:
- Monitor overall portfolio risk
- Detect risk concentrations by region and peril
- Perform stress testing for catastrophic scenarios
- Visualize and download risk analysis reports

The dashboard is built with Python and Streamlit, and is modular for easy extension and integration with real-world data.

---

## How It Works

1. **Data Ingestion:**  
   - Upload your own policy data as a CSV file or use the provided sample data.
   - The data should include: `policy_id`, `policy_type`, `sum_insured`, `region`, `peril`, `premium`, `probability_of_loss`.

2. **Risk Calculation:**  
   - The app calculates the expected loss for each policy and aggregates the total expected loss for the portfolio.

3. **Correlation & Concentration Analysis:**  
   - The dashboard computes correlations between key risk variables.
   - It detects and alerts on high risk concentrations by region and peril.

4. **Stress Testing:**  
   - Simulate catastrophic events by selecting a region or peril and adjusting the loss multiplier.
   - Instantly see the impact on portfolio risk.

5. **Visualization & Reporting:**  
   - Interactive charts and tables display risk metrics, concentrations, and correlations.
   - Download the full risk analysis as a CSV report.

---

## Main Output

- **Total Expected Loss:** The sum of expected losses across all policies.
- **Stressed Portfolio Loss:** The total expected loss after simulating a catastrophic event.
- **Risk Concentration Alerts:** Warnings if a region or peril has a high concentration of risk.
- **Correlation Matrix:** Table showing relationships between key risk variables.
- **Downloadable Report:** Export the risk analysis for further review.

---



## Usage

1. **Run the dashboard:**
    ```bash
    streamlit run dashboard.py
    ```

2. **Open the dashboard in your browser** (usually at http://localhost:8501).

3. **Upload your own data** (CSV) or use the provided `sample_policies.csv`.

4. **Explore:**
    - View total and stressed expected loss
    - See risk concentrations and alerts
    - Analyze the correlation matrix
    - Download the risk report

---

## Sample Data

A sample dataset (`sample_policies.csv`) is included for demonstration.  
The expected columns are:

| Column               | Description                        |
|----------------------|------------------------------------|
| policy_id            | Unique identifier for the policy   |
| policy_type          | Type of insurance (Home, Auto, etc.)|
| sum_insured          | Amount insured                     |
| region               | Geographic region                  |
| peril                | Type of risk/peril (Fire, Flood, etc.)|
| premium              | Policy premium amount              |
| probability_of_loss  | Estimated probability of loss      |

---





