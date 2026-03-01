import streamlit as st

# download my resume
with open("Resume Dyah Dinasari.pdf", "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name="Dyah_Dinasari_Resume.pdf",
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
Architecting governed BI ecosystems that transform fragmented data into trusted executive decisions.
""")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Years in Data", "10+")
col2.metric("Enterprise Systems Built", "20+")
col3.metric("Automation Workflows", "50+")
col4.metric("Cross-Functional Projects", "High Complexity")

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

with open("Resume Dyah Dinasari.pdf", "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name="Dyah_Dinasari_Resume.pdf",
        mime="application/pdf"
    )

st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/dyah-dinasari-751943193/) | 🔗 [GitHub](https://github.com/dyahrositadinasari/)")


