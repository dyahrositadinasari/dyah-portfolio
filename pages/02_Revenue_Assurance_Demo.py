import streamlit as st
import pandas as pd
import numpy as np

st.title("Revenue Assurance & Billing Intelligence System")

st.markdown("""
### Business Context
Fragmented invoice documentation and delayed PO approvals caused revenue leakage and billing inefficiencies.
This system centralizes invoice ingestion, reconciliation, and approval governance.
""")

# Generate Synthetic Data
np.random.seed(42)

vendors = ["Vendor A", "Vendor B", "Vendor C"]
clients = ["Client X", "Client Y"]
status = ["Matched", "Flagged", "Pending Approval"]

data = {
    "Invoice_ID": range(1, 101),
    "Vendor": np.random.choice(vendors, 100),
    "Client": np.random.choice(clients, 100),
    "Invoice_Amount": np.random.randint(5000, 50000, 100),
    "Status": np.random.choice(status, 100),
    "Days_Outstanding": np.random.randint(1, 90, 100)
}

df = pd.DataFrame(data)

st.divider()
st.subheader("Executive Snapshot")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Invoice Value", f"${df['Invoice_Amount'].sum():,.0f}")
col2.metric("Unbilled (Flagged)", f"${df[df['Status']=='Flagged']['Invoice_Amount'].sum():,.0f}")
col3.metric("Match Rate", f"{(len(df[df['Status']=='Matched'])/len(df))*100:.1f}%")
col4.metric("Avg Aging (Days)", f"{df['Days_Outstanding'].mean():.1f}")

st.divider()
st.subheader("Invoice Status Distribution")

st.bar_chart(df["Status"].value_counts())

st.divider()
st.subheader("Sample Data")

st.dataframe(df.head(20))

st.divider()
st.subheader("System Architecture Overview")

st.markdown("""
Invoice PDFs → Python OCR Extraction → SQL Data Warehouse  
↓  
Azure Data Factory → Reconciliation Logic  
↓  
Power BI Executive Dashboard  
↓  
Power Apps Flag Resolution  
↓  
Power Automate Approval Workflow
""")

st.markdown("""
---
*This demonstration uses fully synthetic data and simplified architecture 
to showcase system design capability. No confidential data is exposed.*
""")
