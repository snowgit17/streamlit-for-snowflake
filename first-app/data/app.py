
import streamlit as st 

# st.title("Hierarchical Data Viewer")
# st.header("this is a header")
# st.subheader("subheader")
# st.caption("caption")

# st.write("this is write")
# st.text("fixed text")
# st.code("v = variable()\nanother_call()", "python")
# st.markdown("*bold*")
# st.divider()

# st.latex("...")

# st.error("this is an error")
# st.info("this is info")
# st.warning("this is a warning")
# st.success("this is success")

# st.title("WISHING YOU A VERY HAPPY ANNIVARSARY NAMRATA")
# st.balloons()
# st.snow()
import pandas as pd
import webbrowser
import urllib.parse
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("D:/STREAMLIT_COURSE/streamlit-for-snowflake/first-app/data/employees.csv", header=0).convert_dtypes()
st.dataframe(df)
labels = df[df.columns[0]]
parents = df[df.columns[1]]

data = go.Treemap(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgray"
)
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)

data = go.Icicle(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgrey")
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)


data = go.Sunburst(
    ids=labels,
    labels=labels,
    parents=parents,
    insidetextorientation='horizontal')
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)


data = go.Sankey(
    node=dict(label=labels),
    link=dict(
        source=[list(labels).index(x) for x in labels],
        target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
        label=labels,
        value=list(range(1, len(labels)))))
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)