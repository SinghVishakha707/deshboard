import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Vishakha Singh")
st.header("Python")
st.write("MSC DASI")

df=pd.read_csv("C:/Users/MSCIT/Downloads/only_road_accidents_data_month2.csv")

df

df.head()
df.tail()
df.columns
df.describe()

fig=px.bar(x=df["YEAR"],y=df['JANUARY'])
st.plotly_chart(fig)
fig=px.line(x=df["FEBRUARY"],y=df["SEPTEMBER"])

st.plotly_chart(fig)

fig=px.histogram(x=df["FEBRUARY"],y=df["SEPTEMBER"])
st.plotly_chart(fig)

fig=px.scatter(x=df["FEBRUARY"],y=df["SEPTEMBER"])
st.plotly_chart(fig)