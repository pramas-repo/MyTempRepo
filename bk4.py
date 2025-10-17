from bokeh.plotting import figure, output_file, show
import numpy as np

n = 400
x = np.random.random(size=n) * 100
y = np.random.random(size=n) * 100

rad = np.random.random(size=n) * 1.5
colors = np.random.choice(['red', 'green', 'blue', 'orange', 'purple'], size=n)
output_file("scatter.html")
tools = "crosshair,pan,wheel_zoom,box_zoom,reset"

p = figure(tools=tools, x_range=(0, 100), y_range=(0, 100))
p.circle(x, y, radius=rad, fill_color=colors, 
         fill_alpha=0.6, line_color=None)

show(p)