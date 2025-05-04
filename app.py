from dash import Dash, dcc, html, Input, Output, callback

import pandas as pd

import plotly.express as px

from bs4 import BeautifulSoup

import requests

app = Dash()

# Websites BeautifulSoup is taking data from
url = "https://www.medicalnewstoday.com/articles/322731"

rul = "https://www.cnn.com/2025/04/03/style/michelangelo-smk-3d-printing-factum-arte"

lur = "https://www.cbsnews.com/news/florida-orange-juice-production-plummets-crop-disease-shrinking-demand-natural-disasters/"

# Setting up the ability to get the text

result = requests.get(url)

resull = requests.get(rul)

resullt = requests.get(lur)

dob = BeautifulSoup(resullt.text, "html.parser")

don = BeautifulSoup(resull.text, "html.parser")

doc = BeautifulSoup(result.text, "html.parser")

# Finding all tags with text, usually under the tag "p"

articla = dob.find_all("p")

artic = don.find_all("p")

article = doc.find_all("p")

# Taking the text from all of the 'p' tags in list format
a = []

b = []

c = []

for tag in article:

    a.append(tag.get_text())

for tag in artic:

    b.append(tag.get_text())

for tag in articla:

    c.append(tag.get_text())

# Counting how many tags were put in the lists

i = 0

o = 0

s = 0

for line in a:

    i += 1

for line in b:

   o += 1

for line in c:

   s += 1

# Making the graphs
df = pd.DataFrame({
    "article": ['cranberry', 'art', 'orange'],
    "p tags counted": [i, o, s]

})

fig = px.bar(df, x="article", y="lines counted")


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    
    dcc.Dropdown(
        id='graph-selector',
        options=[
            {'label': 'Bar Chart', 'value': 'bar'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'pie chart' , 'value': 'pie' }
        ],
  
        value = 'bar'
    ),
    dcc.Graph(id='graph-output')
]),

    # Define the callback to update the graph
@app.callback(
    Output('graph-output', 'figure'),
    [Input('graph-selector', 'value')]
)
def update_graph(selected_graph):
    if selected_graph == 'bar':
        fig = px.bar(df, x='article', y='p tags counted', title="Amount of p tags counted in articles")
    elif selected_graph == 'scatter':
        fig = px.scatter(df, x='article', y='p tags counted', color='article', size='p tags counted', title="Amount of p tags counted in articles")
    elif selected_graph == 'pie':
        fig = px.pie(df, values="p tags counted", names="article", title="Amount of p tags counted in articles")
    return fig



if __name__ == '__main__':
    app.run(debug=True)
