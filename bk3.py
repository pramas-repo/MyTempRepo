from bokeh.plotting import figure, output_file, show

a = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
a0 = [i**2 for i in a]
a1 = [10**i for i in a]
a2 = [10**(i**2) for i in a]

output_file("loglines.html")

p = figure(
   tools="pan,box_zoom,reset,save",
   y_axis_type="log", y_range=[0.001, 10**11], title="Log axis example",
   x_axis_label='sections', y_axis_label='particles'
)

p.line(a, a, legend_label="y=a")
p.circle(a, a, legend_label="y=a", fill_color="white", size=8)

p.line(a, a0, legend_label="y=a^2", line_width=3)
p.circle(a, a0, legend_label="y=a^2", fill_color="red", line_color="red", size=6)

p.line(a, a1, legend_label="y=10^a", line_color="red")
p.circle(a, a1, legend_label="y=10^a", fill_color="red", line_color="red", size=6)

p.line(a, a2, legend_label="y=10^a^2", line_color="orange", line_dash="4 4")
p.circle(a, a2, legend_label="y=10^a^2", line_color="blue", line_dash="4 4")
show(p)