import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interactive Executive Dashboard Demo")

df = pd.read_csv("data/demo_sales.csv")

df["profit"] = df["revenue"] - df["cost"]

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${df['revenue'].sum():,.0f}")
col2.metric("Total Profit", f"${df['profit'].sum():,.0f}")
col3.metric("Avg Margin %", f"{(df['profit'].sum()/df['revenue'].sum()*100):.1f}%")

fig = px.line(df, x="month", y=["revenue","profit"], markers=True)

st.plotly_chart(fig, use_container_width=True)
