import streamlit as st

# download my resume
with open("Resume Dyah Dinasari.pdf", "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name="Resume_Dyah_Dinasari.pdf",
        mime="application/pdf"
    )

# main page
import streamlit as st

st.set_page_config(
    page_title="Dyah Dinasari | Senior BI & Analytics Engineer",
    layout="wide"
)

st.title("Dyah Dinasari")
st.subheader("Senior Business Intelligence & Analytics Engineer")

st.markdown("""
# Architecting governed Business Intelligence ecosystems  
that transform fragmented operational data into trusted executive decision systems.

I specialize in building scalable data models, automation pipelines, and KPI governance frameworks 
that enable real-time business optimization across marketing, finance, and operations.
""")

st.markdown("---")

st.markdown("### Executive Impact Snapshot")

kpi_html = """
<style>
.kpi-card {
    background-color: #1E293B;
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #334155;
    transition: all 0.3s ease;
}
.kpi-card:hover {
    transform: scale(1.05);
    border-color: #3B82F6;
}
.kpi-value {
    font-size: 36px;
    font-weight: 700;
    color: #38BDF8;
}
.kpi-label {
    font-size: 14px;
    color: #94A3B8;
}
</style>
"""

st.markdown(kpi_html, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">10+</div>
        <div class="kpi-label">Years in Data & Analytics</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">20+</div>
        <div class="kpi-label">Enterprise BI Systems Delivered</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">High</div>
        <div class="kpi-label">Cross-Functional Complexity</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("### Core Expertise")

st.markdown("""
- Enterprise KPI Framework Design  
- Star Schema & Fact-Dimension Modeling  
- Revenue & Operational Intelligence Systems  
- Automation (Python, Power Platform, Azure)  
- Data Governance & Validation Architecture  
""")

st.markdown("---")


st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/dyah-dinasari-751943193/) | 🔗 [GitHub](https://github.com/dyahrositadinasari/)")


