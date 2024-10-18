import requests
import json
import plotly.express as px
import pandas as pd
import chart_studio.tools as tls
import plotly.graph_objects as go

#with open('TX_STAID025054.txt',encoding='utf8') as f: file = f.read()

#print(file)
#data = pd.read_csv('TX_STAID025054.txt', names=['STAID','SOUID','DATE','TX','Q_TX'], sep=',')

#data.drop([0], inplace = True)

df  = pd.read_csv('TX_STAID025054.txt', sep=',')





data = pd.DataFrame(df)

del data['STAID']
del data['SOUID']
del data['Q_TX']


convert_dict = {'DATE': str, 'TX': float}

data = data.astype(convert_dict)
data['TX'] = df['TX'] * 0.1
data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d')




#print(data)

# print(data)


#     #x += x

print(data)





#print(data)
#print(df)

graph = px.line(data, x='DATE', y='TX', height=400)
#raph.update_xaxes(rangeslider_visible=True)
graph.update_traces(line_color='limegreen')

graph.show()
graph.write_html("ocieplenie_czy_nie.html")
#for a in df:
#
#
#   print(a)


#    a[1] = float(a[1])