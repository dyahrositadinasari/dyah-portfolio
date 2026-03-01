import streamlit as st

st.set_page_config(
    page_title="Dyah Dinasari | Senior BI & Analytics Engineer",
    layout="wide"
)

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("""
# Dyah Dinasari  
### Senior Business Intelligence & Analytics Engineer  

Architecting scalable BI ecosystems that transform complex data into trusted executive decisions.
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric("Years in Data Leadership", "10+")
col2.metric("Enterprise BI Systems Built", "20+")
col3.metric("Automation Workflows Delivered", "50+")

st.markdown("---")

st.markdown("""
## What I Do

✔ Design governed KPI frameworks  
✔ Build scalable star-schema data models  
✔ Implement enterprise-grade BI systems  
✔ Ensure data quality & lineage integrity  
✔ Bridge business and engineering through structured analytics  

---

### Explore the navigation panel to view strategic impact, architecture thinking, and live demo dashboard.
""")


--download my resume
with open("Resume Dyah Dinasari.pdf", "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name="Dyah_Dinasari_Resume.pdf",
        mime="application/pdf"
    )
