import pandas as pd
import csv
import plotly.express as go

df = pd.read_csv('data.csv')
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = go.scatter(mean, x="student_id", y="level", color="attempt", size="attempt")
fig.show()