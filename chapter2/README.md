# **Mathematical Plotting with Matplotlib**
Plotting is a fundamental tool in all of mathematics. A good plot can reveal hidden details,
suggest future directions, verify results, or reinforce an argument. It is no surprise, then,
that the scientific Python stack features a powerful and flexible plotting library called
Matplotlib.
> `import matplotlib.pyplot as plt`

## **Basic plotting with Matplotlib**
To plot the data, we simply need to call the plot function from
the pyplot interface, which is imported under the plt alias. The first argument
is the x data and the second is the y data. The function returns a handle to the
axes object on which the data is plotted
> `plt.plot(x, y)`

Plot the y values against the x values on a new figure
> `plt.show()`

If there are currently no `Figure` or `Axes` objects, the `plt.plot` routine creates a new
`Figure` object, adds a new `Axes` object to the figure, and populates this `Axes` object with
the plotted data. A list of handles to the plotted lines is returned. Each of these handles is
a `Lines2D` object. In this case, this list will contain a single `Lines2D` object

Sometimes useful to manually instantiate a Figure object prior to calling
the plot routine—for instance, to force the creation of a new figure
> `fig = plt.figure()` # manually create a figure \

It is occasionally useful to create a new figure and explicitly create a new set of axes in this 
figure together. The best way to accomplish this is to use the `subplots` routine in the `pyplot` 
interface. This routine returns a pair, where the first object is `Figure` and the second is an 
`Axes` object:
> `fig, ax = plt.subplots()` \
  `l1 = ax.plot(x, f(x))` \
  `l2 = ax.plot(x, x**2)` \
  `l3 = ax.plot(x, 1 - x)`

## **Changing the plotting style**
The easiest way to control the style of a plot is to use a **format string**, which is provided as 
an optional argument after the x-y pair or the y data in the `plot` command. When plotting multiple 
sets of data, a different format string can be provided for each set of arguments.
> `fig, ax = plt.subplots()` \
  `lines = ax.plot(y1, 'o', y2, 'x', y3, '*')`

The format string has three optional parts, each consisting of one or more characters. 
  - The first part controls the `marker style`, which is the symbol that is `printed at each data point`\
  - the second controls the `style of the line` that connects the data points: 
    - a solid line (-)
    - a dashed line (--)
    - a dash-dot line (-.)
    - a dotted line (:)
  - the third controls the `color of the plot`
    - *red, green, blue, cyan, yellow, magenta, black, and white*
    - **OR** --- *r, g, b, c, y, m, k, and w*

Other aspects of the plot can be customized by using methods on the `Axes` object. The axes ticks can be 
modified using the `set_xticks` and `set_yticks` methods on the `Axes` object, and the `grid` appearance 
can be configured using the grid method
> `ax.axis([-0.5, 5.5, 0, 5.5])` # set axes \
  `ax.set_xticks([0.5*i for i in range(9)])` # set xticks \
  `ax.set_yticks([0.5*i for i in range(11)]` # set yticks \
  `ax.grid()` # add a grid

## **Adding labels and legends to plots**

we have a reference to the Axes object on which our data is plotted, and so we can start to customize these 
axes by adding labels and titles. The title and axes labels can be added to a figure by using the set_title,
set_xlabel, and set_ylabel methods on the ax object created by the subplots routine
> `ax.set_title("Plot of the data y1, y2, and y3")` \
  `ax.set_xlabel("x axis label")` \
  `ax.set_ylabel("y axis label")` \
  `ax.legend(("data y1", "data y2", "data y3"))`

## **Adding subplots**

We use the `subplots` routine to create a new figure and references to all of the `Axes` objects in each subplot,
arranged in a grid with one row and two columns. We also set the `tight_layout` keyword argument to `True` to fix 
the layout of the resulting plots. This isn't strictly necessary, but it is in this case as it produces a better 
result than the default:
> `fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)` # 1 row, 2 columns

We use an alternative plotting method that uses a logarithmic scale on the `y-axis`, called `semilogy`. The signature 
for this method is the same as the standard plot method
> `ax2.semilogy(errors, "x")` # plot y on logarithmic scale

## **Saving Matplotlib figures**

There are plenty of situations where it would be more appropriate to store a figure directly to a file, rather than
rendering it on screen

The savefig method on fig to save this figure to a file. The only required argument is the path to output to or 
a file-like object that the figure can be written to. We can adjust various settings for the output format, such 
as the resolution, by providing the appropriate keyword arguments.
> `fig.savefig("savingfigs.png", dpi=300)`

Matplotlib will infer that we wish to save the image in the Portable Network Graphics (PNG) format from the extension 
of the file given. Alternatively, a format can be explicitly provided as a keyword argument (by using the format 
keyword), or it will fall back to the default from the configuration file.


## **Surface and contour plots**

Matplotlib can also plot three-dimensional data in a variety of ways. Two common choices for displaying data 
like this are by using `surface` plots or `contour` plots (think of contour lines on a map). In this recipe, we 
will see a method for plotting surfaces from threedimensional data and how to plot contours of three-dimensional data.

To plot three-dimensional `surfaces`, we need to load a `Matplotlib` toolbox, `mplot3d`, which comes with the `Matplotlib` 
package. This won't be used explicitly in the code, but behind the scenes, it makes the three-dimensional plotting
utilities available to `Matplotlib`:
> `from mpl_toolkits import mplot3d` \
  `fig = plt.figure()` \
  `ax = fig.add_subplot(projection="3d") # declare 3d plot` \
  `ax.plot_surface(x, y, z)`

`Contour` plots do not require the `mplot3d` toolkit, and there is a contour routine in the pyplot interface that 
produces `contour` plots. However, unlike the usual (two-dimensional) plotting routines, the contour routine requires 
the same arguments as the `plot_surface` method. 
> `plt.contour(x, y, z)`

The routines described in the preceding section, `contour` and `plot_contour`, only work with highly structured 
data where the x, y, and z components are arranged into grids. Unfortunately, real-life data is rarely so structured. 
In this case, you need to perform some kind of `interpolation` between known points to approximate the value on a 
uniform grid, which can then be plotted. A common method for performing this `interpolation` is by `triangulating` 
the collection of (x, y) pairs and then using the values of the function on the vertices of each triangle to estimate
the value on the grid points. Fortunately, Matplotlib hasa method that does all of these steps and then plots the 
result, which is the `plot_trisurf` routine. 


## **Customizing three-dimensional plots**

Contour plots can hide some detail of the surface that they represent since they only show
where the "height" is similar and not what the value is, even in relation to the surrounding
values. On a map, this is remedied by printing the height onto certain contours. Surface
plots are more revealing, but the problem of projecting three-dimensional objects into 2D to
be displayed on a screen can itself obscure some details. To address these issues, we can
customize the appearance of a three-dimensional plot (or contour plot) to enhance the plot
and make sure the detail that we wish to highlight is clear. The easiest way to do this is by
changing the colormap of the plot.

we simply apply one of the built-in colormaps, `binary_r`, which is done by providing the `cmap="binary_r"` 
keyword argument to the `plot_surface` routine:

> `fig = plt.figure()`
  `ax = fig.add_subplot(projection="3d")`
  `ax.plot_surface(x, y, z, cmap="binary_r")`

The contour plot, the method for changing the colormap is the same we simply specify a value for the 
cmap keyword argument:

> `fig = plt.figure()`
  `plt.contour(x, y, z, cmap="binary_r")`