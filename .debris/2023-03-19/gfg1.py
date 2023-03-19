import pandas as pd
import chart_studio.plotly as py
import plotly.offline as po
import plotly.graph_objs as pg
import matplotlib.pyplot as plt
AE = pd.read_csv('AgriculturalExport.csv')
AE.head()
data = dict(type = 'choropleth', 
 locations = ['AL', 'AK', 'AR', 'CA'], 
 locationmode = 'USA-states', 
 z = [1,2,30,40,50], 
 text = ['alabama', 'alaska', 'arizona', 'pugger', 'california'])

layout = dict(geo = {'scope':'usa'})
x = pg.Figure(data = [data] ,
 layout = layout)
po.iplot(x)
