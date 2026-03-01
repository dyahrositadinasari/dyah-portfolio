import streamlit as st
import pandas as pd

st.title("Architecture & Technical Depth")

tab1, tab2, tab3, tab4 = st.tabs([
    "Data Architecture",
    "SQL Case Study",
    "DBT Concept",
    "KPI & Lineage"
])

# ==========================
# TAB 1
# ==========================
with tab1:
    st.subheader("Modern BI Architecture Philosophy")

    st.markdown("""
Data Source → Warehouse → Transformation Layer → Semantic Layer → Executive Dashboard  
""")

    st.markdown("""
Core Principles:
- Clear grain definition  
- Fact-Dimension modeling discipline  
- Modular transformation logic  
- Data validation layer  
- Role-based governance  
""")

# ==========================
# TAB 2
# ==========================
with tab2:
    st.subheader("Revenue Aggregation & Cohort Logic Example")

    st.code("""
WITH revenue_by_user AS (
    SELECT
        user_id,
        SUM(order_amount) AS total_revenue,
        COUNT(order_id) AS total_orders
    FROM fact_orders
    GROUP BY user_id
),

cohort_analysis AS (
    SELECT
        DATE_TRUNC(order_date, MONTH) AS cohort_month,
        COUNT(DISTINCT user_id) AS active_users
    FROM fact_orders
    GROUP BY 1
)

SELECT *
FROM revenue_by_user;
""", language="sql")

    st.markdown("""
Highlights:
- Clear aggregation grain  
- Avoided double counting  
- Cohort logic separation  
""")

# ==========================
# TAB 3
# ==========================
with tab3:
    st.subheader("DBT Conceptual Structure")

    st.code("""
models/
   staging/
   intermediate/
   marts/
""")

    st.markdown("""
- Modular SQL models  
- ref() dependency management  
- Built-in data tests (not_null, unique)  
- Version control via Git  
- Incremental model capability  
""")

# ==========================
# TAB 4
# ==========================
with tab4:
    st.subheader("KPI Dictionary Sample")

    data = {
        "KPI": ["Revenue", "Active Users"],
        "Definition": [
            "Total confirmed transaction value",
            "Users with at least one transaction in period"
        ],
        "Grain": ["Transaction", "Monthly"],
        "Owner": ["Finance", "Product"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.subheader("Data Lineage Concept")

    st.markdown("""
Source Data  
↓  
Staging Layer  
↓  
Business Mart  
↓  
Executive Dashboard  
""")
