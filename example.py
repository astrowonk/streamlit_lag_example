import streamlit as st

import numpy as np
import altair as alt
import pandas as pd
import plotly.express as px

name = {}
value1 = {}
value2 = {}
n_elements = 2

st.markdown("""

## Text lag example

Type text in any form field, it should work ok. Then pick plotly and submit and try again. There is ~300ms or more lag for each character typed into any field after the plotly graphs are rendered.

""")

with st.form('my-form'):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption("Value 0")
        for p in range(n_elements):
            name[p] = st.text_input("", key=f"name_{p}")
    with col2:
        st.caption("Value 1")
        for p in range(n_elements):
            value1[p] = st.number_input("", key=f"value_{p}", step=1, value=1)
    with col3:
        st.caption("Value 2")
        for p in range(n_elements):
            value2[p] = st.text_input(
                "",
                key=f"value2_{p}",
            )
    chart_type = st.selectbox("Chart type", ['Plotly', 'Altair'])

    submitted = st.form_submit_button("Submit")

if submitted:
    # df = px.data.iris()  # iris is a pandas DataFrame
    # fig = px.scatter(df, x="sepal_width", y="sepal_length")
    #st.plotly_chart(fig)

    tab_names = [f"Example {x+1}" for x in range(5)]
    mytabs = st.tabs(tab_names)

    for tab in mytabs:
        with tab:

            df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
            fig = df.plot.scatter(x='a', y='b', color='c', backend='plotly')
            c = alt.Chart(df).mark_circle().encode(x='a',
                                                   y='b',
                                                   size='c',
                                                   color='c',
                                                   tooltip=['a', 'b', 'c'])
            if chart_type == 'Altair':
                st.altair_chart(c, use_container_width=True)
            else:
                st.plotly_chart(fig)

# st.scatter(df, x="sepal_width", y="sepal_length")
#st.plotly_chart(fig)
#st.plotly_chart(fig)
