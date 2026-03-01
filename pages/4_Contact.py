meimport streamlit as st

st.title("Contact & Credentials")

st.markdown("""
If you're looking for a Senior BI professional who combines 
business strategy, system architecture, and governance discipline — let's connect.
""")

st.markdown("### Resume")
with open("Resume Dyah Dinasari.pdf", "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name="Resume_Dyah_Dinasari.pdf",
        mime="application/pdf"
    )

st.markdown("### Professional Links")
st.markdown(""" 
- 🔗 LinkedIn: https://www.linkedin.com/in/dyah-dinasari-751943193/
- 🔗 GitHub: https://github.com/dyahrositadinasari/
- 📧 Email: ochi_dyah@yahoo.com  
""")
