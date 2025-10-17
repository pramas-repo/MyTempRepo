from bokeh.plotting import figure, show, output_file

x =   [1, 2, 3]
y =   [1.2, 2.5, 3.7]

output_file('vbar.html')

p = figure(width=600, height=600, title="Vertical Bar Example")

p.hbar(x, width=0.5, left=0, right=y, color="navy")

show(p)