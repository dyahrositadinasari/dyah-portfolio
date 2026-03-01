import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interactive Executive Dashboard Demo")

df = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Revenue": [120000,135000,150000,170000,160000,180000],
    "Cost": [80000,82000,90000,95000,88000,97000]
})

df["Profit"] = df["Revenue"] - df["Cost"]

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${df['Revenue'].sum():,}")
col2.metric("Total Profit", f"${df['Profit'].sum():,}")
col3.metric("Avg Margin", f"{(df['Profit'].sum()/df['Revenue'].sum()*100):.1f}%")

fig = px.line(df, x="Month", y=["Revenue","Profit"], markers=True)
st.plotly_chart(fig, use_container_width=True)
