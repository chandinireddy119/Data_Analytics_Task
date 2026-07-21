import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("Interactive Sales Dashboard")

df = pd.read_csv("sales_dashboard.csv")

st.write("### Sales Dataset")
st.dataframe(df)

st.write("## Dashboard Summary")

st.metric("Total Sales", int(df["Sales"].sum()))
st.metric("Total Profit", int(df["Profit"].sum()))
st.metric("Total Customers", int(df["Customers"].sum()))

st.write("## Monthly Sales")
st.line_chart(df.set_index("Month")["Sales"])

st.write("## Monthly Profit")
st.bar_chart(df.set_index("Month")["Profit"])

st.write("## Monthly Customers")
st.area_chart(df.set_index("Month")["Customers"])

st.success("Dashboard Loaded Successfully!")