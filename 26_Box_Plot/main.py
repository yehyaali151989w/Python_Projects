import plotly.express as px
import pandas as pd
data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
print(data.head())


fig = px.box(data, y="TV")
fig.show()
