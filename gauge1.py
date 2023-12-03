import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.graph_objects as go

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

alt.data_transformers.disable_max_rows()

st.write("# Testing Gauge Viz")

st.write('\n')

fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 450,
    mode = "gauge+number",
    title = {'text': "Resume Length"},
    #delta = {'reference': 300},
    gauge = {'axis': {'range': [0, 600]},
             'bar': {'color': 'navy'},
             'steps' : [
                 {'range': [0, 350], 'color': "whitesmoke"},
                 {'range': [350, 550], 'color': "green"},
                 {'range': [550, 600], 'color': "darkred"}]
             }))

fig.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})

st.plotly_chart(fig)

st.write('\n')

fig2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 45,
    mode = "gauge+number",
    title = {'text': "Similarity Score (Percentage)"},
    #delta = {'reference': 300},
    gauge = {'axis': {'range': [0, 100]},
             'bar': {'color': 'navy'},
             'steps' : [
                 {'range': [0, 40], 'color': "whitesmoke"},
                 {'range': [40, 60], 'color': "gold"},
                 {'range': [60, 100], 'color': "forestgreen"}]
             }))

fig2.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})

st.plotly_chart(fig2)