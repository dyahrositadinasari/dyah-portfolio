import streamlit as st

st.title("Project Case Study")

st.subheader("Enterprise Marketing Performance Dashboard")

st.markdown("""
**Problem:**  
Fragmented reporting across business units created inconsistent KPI definitions.

**Approach:**  
- Designed star schema data model
- Defined standardized KPI framework
- Implemented Row-Level Security (RLS)
- Optimized DAX measures

**Impact:**  
- Unified metric definitions
- Reduced reporting discrepancies
- Improved executive decision speed
""")

st.divider()

st.subheader("Workflow Automation: Email → AI → Dashboard")

st.markdown("""
**Architecture:**  
Email → Power Automate → SharePoint → AI Extraction → Power Apps → Power BI

**Impact:**  
- Reduced manual workload
- Improved data validation
- Accelerated reporting cycle
""")
