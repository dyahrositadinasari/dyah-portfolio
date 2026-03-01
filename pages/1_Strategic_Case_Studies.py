import streamlit as st

st.title("Strategic Case Studies")

st.markdown("""
These selected case studies demonstrate my ability to solve complex, cross-functional 
business problems by combining data modeling, automation engineering, and governance discipline.
""")

# ==========================
# PROJECT 1
# ==========================

st.header("Intelligent Revenue Recovery & Billing Automation Platform")

st.markdown("""
Designed and implemented an end-to-end automated billing intelligence platform 
that reduced revenue leakage and operational friction through system architecture and workflow orchestration.
""")

with st.expander("Business Problem"):
    st.markdown("""
- Missing vendor invoices  
- Manual reconciliation  
- Delayed billing cycles  
- PO approval bottlenecks  
- Revenue realization delays  
""")

with st.expander("Architecture & System Design"):
    st.markdown("""
Vendor Invoice → Python Parsing → SQL Server  
↓  
Azure Data Factory Reconciliation  
↓  
Power BI Billing Readiness Dashboard  
↓  
Power Apps Exception Handling  
↓  
Power Automate Approval Workflow  
""")

with st.expander("Business Impact"):
    st.markdown("""
✔ Reduced billing delays  
✔ Improved revenue visibility  
✔ Automated reconciliation process  
✔ Increased financial governance  
""")

st.markdown("---")

# ==========================
# PROJECT 2
# ==========================

st.header("Cross-Source TV Market Intelligence Framework")

st.markdown("""
Engineered a unified TV benchmarking system by reconciling structurally inconsistent datasets 
to enable agency-wide visibility and investment-driven insights.
""")

with st.expander("Core Challenge"):
    st.markdown("""
- Two independent datasets  
- Completely inconsistent brand naming  
- No unified aggregation layer  
- High manual reconciliation effort  
""")

with st.expander("Strategic Approach"):
    st.markdown("""
- Designed brand normalization mapping  
- Built SQL transformation layer  
- Created consolidated TV mart  
- Delivered executive benchmark dashboard  
""")

with st.expander("Business Impact"):
    st.markdown("""
✔ First holistic TV campaign visibility  
✔ Enabled investment insight generation  
✔ Reduced manual reconciliation  
✔ Strengthened decision confidence  
""")

st.markdown("---")

# ==========================
# PROJECT 3
# ==========================

st.header("Campaign Intelligence & Budget Optimization System")

st.markdown("""
Built an integrated cross-channel campaign intelligence system enabling real-time 
budget optimization and performance-driven decision making.
""")

with st.expander("Business Problem"):
    st.markdown("""
- Fragmented reporting across channels  
- Reactive optimization  
- No mid-campaign visibility  
""")

with st.expander("Strategic Role"):
    st.markdown("""
- Defined standardized KPI framework  
- Designed unified performance fact model  
- Built executive decision dashboard  
""")

with st.expander("Business Impact"):
    st.markdown("""
✔ Real-time campaign visibility  
✔ Enabled budget reallocation mid-campaign  
✔ Improved ROI decision capability  
✔ Increased client transparency  
""")
