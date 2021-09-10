import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
print(df)

studentdf = df.loc[df["student_id"] == "TRL_xyz"]
print(studentdf)

fig = go.Figure(go.Bar(
    x = ["level 1", "level 2", "level 3", "level 4"],
    y = studentdf.groupby("level")["attempt"].mean(),
    orientation = "v"
))
fig.show()