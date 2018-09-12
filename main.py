from flask import Flask, render_template, Markup
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.embed import components
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/runpandas')
def runpandas():
    df = pd.read_csv('https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2017-financial-year-provisional/Download-data/annual-enterprise-survey-2017-financial-year-provisional-csv.csv')
    sample_stats_df = df.describe()
    sample_stats = dict(zip(list(sample_stats_df.index), list(sample_stats_df.values)))
    return render_template('runpandas.html', data=sample_stats)

@app.route('/bokehscatterplot')
def bokehscatterplot():
    return render_template('bokehscatterplot.html')

@app.route('/bokehhistogram')
def bokehhistogram():
    return render_template('bokehhistogram.html')

@app.route('/bokehplot2')
def createplot():
    # create a blank figure with labels
    p = figure(plot_width=600, plot_height = 600,
               title = 'Example Glyphs',
               x_axis_label = 'X', y_axis_label = 'Y')

    # Example data
    squares_x = [1, 3, 4, 5, 8]
    squares_y = [8, 7, 3, 1, 10]
    circles_x = [9, 12, 4, 3, 15]
    circles_y = [8, 4, 11, 6, 10]

    # add squares glyph
    p.square(squares_x, squares_y, size=12, color='navy', alpha=0.6)
    # add circles glyph
    p.circle(circles_x, circles_y, size=12, color='red')

    # create javascript and div compeonent for html
    script, div = components(p)
    script = Markup(script)
    div = Markup(div)
    return render_template('bokehplot2.html', script=script, div=div)


if __name__ == '__main__':
  app.run(debug=True)
