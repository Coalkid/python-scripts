import requests
import json
import plotly.express as px
import pandas as pd
import chart_studio.tools as tls


x = requests.get('https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json')
data = json.loads(x.text)


del data[0]


for a in data:

    a[1] = float(a[1])


df = pd.DataFrame(data)


graph = px.line(df, x=0, y=1, height=400)

graph.show()

graph.write_html("graph.html")