# Importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Tips Dashboard",
    page_icon="💡",  # Added an emoji as a page icon for better visual appeal
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data  # Cache the data to improve performance on reruns
def load_data():
    return pd.read_csv('tips.csv')

df = load_data()

# Sidebar
st.sidebar.header("Tips Dashboard")
st.sidebar.image('tips.webp', use_column_width=True)  # Ensure the image fits the sidebar width
st.sidebar.write("Welcome! This dashboard lets you interactively explore the Tips dataset, uncovering trends in restaurant tips and customer behavior.")
st.sidebar.markdown("---")  # Add a horizontal line for better visual separation

# Filters
st.sidebar.subheader("Filter Your Data")
cat_filter = st.sidebar.selectbox("Categorical Filtering", [None, 'sex', 'smoker', 'day', 'time'])
num_filter = st.sidebar.selectbox("Numerical Filtering", [None, 'total_bill', 'tip'])
row_filter = st.sidebar.selectbox("Row Filtering", [None, 'sex', 'smoker', 'day', 'time'])
col_filter = st.sidebar.selectbox("Column Filtering", [None, 'sex', 'smoker', 'day', 'time'])
st.sidebar.markdown("---")

# Footer in sidebar
st.sidebar.markdown("Made by Eng. [Mahmoud Elbadrawy](https://www.linkedin.com/in/mahmoud-elbadrawy)")
st.sidebar.markdown(f"Software Engineer and master's student in Automotive Software Engineering at TU Chemntiz")

# Body

# Row A: Key Metrics
st.subheader("Key Metrics")
a1, a2, a3, a4 = st.columns(4)
a1.metric("Max. Total Bill", f"${df['total_bill'].max():.2f}")  # Format as currency
a2.metric("Max. Tip", f"${df['tip'].max():.2f}")  # Format as currency
a3.metric("Min. Total Bill", f"${df['total_bill'].min():.2f}")  # Format as currency
a4.metric("Min. Tip", f"${df['tip'].min():.2f}")  # Format as currency

# Row B: Scatter Plot
st.subheader("Total Bills vs. Tips")
fig = px.scatter(
    data_frame=df,
    x='total_bill',
    y='tip',
    color=cat_filter,
    size=num_filter,
    facet_col=col_filter,
    facet_row=row_filter,
    title="Relationship Between Total Bills and Tips"  # Add a title for clarity
)
st.plotly_chart(fig, use_container_width=True)

# Row C: Visualizations
st.subheader("Detailed Analysis")
c1, c2, c3 = st.columns((4, 3, 3))

with c1:
    st.markdown("**Sex vs. Total Bills**")  # Use markdown for better text formatting
    fig = px.bar(
        data_frame=df,
        x='sex',
        y='total_bill',
        color=cat_filter,
        title="Total Bills by Gender"
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.markdown("**Smoker/Non-smoker vs. Tips**")
    fig = px.pie(
        data_frame=df,
        names='smoker',
        values='tip',
        color=cat_filter,
        title="Tips Distribution by Smoking Status"
    )
    st.plotly_chart(fig, use_container_width=True)

with c3:
    st.markdown("**Days vs. Tips**")
    fig = px.pie(
        data_frame=df,
        names='day',
        values='tip',
        color=cat_filter,
        hole=0.4,
        title="Tips Distribution by Day"
    )
    st.plotly_chart(fig, use_container_width=True)