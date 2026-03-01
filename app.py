with open("Resume Dyah Dinasari.pdf", "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name="Dyah_Dinasari_Resume.pdf",
        mime="application/pdf"
    )
