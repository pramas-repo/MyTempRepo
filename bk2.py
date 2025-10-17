# Line glyph in Bokeh
from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5] # x series
y = [60, 70, 72, 64, 75]  # y series

output_file("bokeh-line.html")

p = figure(title="Scores of the Students in 2025", x_axis_label='Student rno', \
           y_axis_label='Student Percentage')

p.line(x, y, legend_label="Scores in Exam", line_width=2) # line function draws the line
show(p)