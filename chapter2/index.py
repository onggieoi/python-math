import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


def f(x):
    return x*(x - 2)*np.exp(3 - x)


x = np.linspace(-0.5, 3.0)  # 100 values between -0.5 and 3.0

y = f(x)                    # evaluate f on the x points => [f(x)[0-100]]

plt.plot(x, y)               # plot data

# plt.figure()                          # manually create a new figure
# plt.plot(x, f(x), x, x**2, x, 1 - x)  # muilty lines

# -------
# fig, ax = plt.subplots()  # subplot
# l1 = ax.plot(x, f(x))
# l2 = ax.plot(x, x**2)
# l3 = ax.plot(x, 1 - x)

# y1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
# y2 = np.array([1.2, 1.6, 3.1, 4.2, 4.8])
# y3 = np.array([3.2, 1.1, 2.0, 4.9, 2.5])

# fig, ax = plt.subplots()  # subplot
# lines = ax.plot(y1, 'o', y2, 'x', y3, '*')  # add styles line

# ax.set_title("Plot of the data y1, y2, and y3")
# ax.set_xlabel("x axis label")
# ax.set_ylabel("y axis label")

# ax.axis([-0.5, 5.5, 0, 5.5])  # set axes
# ax.set_xticks([0.5*i for i in range(9)])  # set xticks
# ax.set_yticks([0.5*i for i in range(11)])  # set yticks
# ax.grid()

# # add a legend follow order of plot(1, 2, 3)
# ax.legend(("data y1", "data y2", "data y3"))


# ------ seprate figure -----------------------------------------------------------------
# def generate_newton_iters(x0, number):
#     iterates = [x0]
#     errors = [abs(x0 - 1.)]
#     for _ in range(number):
#         x0 = x0 - (x0*x0 - 1.)/(2*x0)
#         iterates.append(x0)
#         errors.append(abs(x0 - 1.))
#     return iterates, errors


# iterates, errors = generate_newton_iters(2.0, 5)

# # print(iterates, errors)

# fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)  # 1 row, 2 columns

# ax1.plot(iterates, "x")
# ax1.set_title("Iterates")
# ax1.set_xlabel("$i$")
# ax1.set_ylabel("$x_i$")

# ax2.semilogy(errors, "x")  # plot y on logarithmic scale
# ax2.set_title("Error")
# ax2.set_xlabel("$i$")
# ax2.set_ylabel("Error")
# ---------------------------------------------------------------------------------------


# -------------- Surface and contour plots
# X = np.linspace(-2, 2)
# Y = np.linspace(-1, 1)

# x, y = np.meshgrid(X, Y)

# z = x**2 * y**3

# fig = plt.figure()
# ax = fig.add_subplot(projection="3d")  # declare 3d plot

# surface
# ax.plot_surface(x, y, z)

# ax.set_xlabel("$x$")
# ax.set_ylabel("$y$")
# ax.set_zlabel("$z$")

# ax.set_title("Graph of the function $f(x) = x^2y^3$")

# coutour
# plt.contour(x, y, z)
# plt.title("Contours of $f(x) = x^2y^3$")
# plt.xlabel("$x$")
# plt.ylabel("$y$")

# x = np.array([0.19, -0.82, 0.8, 0.95, 0.46, 0.71,
#               -0.86, -0.55, 0.75, -0.98, 0.55, -0.17, -0.89,
#               -0.4, 0.48, -0.09, 1., -0.03, -0.87, -0.43])
# y = np.array([-0.25, -0.71, -0.88, 0.55, -0.88, 0.23,
#               0.18, -0.06, 0.95, 0.04, -0.59, -0.21, 0.14, 0.94,
#               0.51, 0.47, 0.79, 0.33, -0.85, 0.19])
# z = np.array([-0.04, 0.44, -0.53, 0.4, -0.31, 0.13,
#               -0.12, 0.03, 0.53, -0.03, -0.25, 0.03, -0.1,
#               -0.29, 0.19, -0.03, 0.58, -0.01, 0.55, -0.06])

# # ------- trisurf
# fig = plt.figure(tight_layout=True)  # force new figure
# ax1 = fig.add_subplot(1, 2, 1, projection="3d")  # 3d axes
# ax1.plot_trisurf(x, y, z)
# ax1.set_xlabel("$x$")
# ax1.set_ylabel("$y$")
# ax1.set_zlabel("$z$")
# ax1.set_title("Approximate surface")

# ax2 = fig.add_subplot(1, 2, 2)  # 2d axes
# ax2.tricontour(x, y, z)
# ax2.set_xlabel("$x$")
# ax2.set_ylabel("$y$")
# ax2.set_title("Approximate contours")


# ------------- Customizing three-dimensional plots
# X = np.linspace(-2, 2)
# Y = np.linspace(-2, 2)
# x, y = np.meshgrid(X, Y)
# t = x**2 + y**2  # small efficiency
# z = np.cos(2*np.pi*t)*np.exp(-t)

# fig = plt.figure()
# ax = fig.add_subplot(projection="3d")
# ax.plot_surface(x, y, z, cmap="binary_r")

# ax.set_title("Surface with colormap")
# ax.set_xlabel("$x$")
# ax.set_ylabel("$y$")
# ax.set_zlabel("$z$")

# fig = plt.figure()
# plt.contour(x, y, z, cmap="binary_r")
# plt.xlabel("$x$")
# plt.ylabel("$y$")
# plt.title("Contour plot with colormap set")

plt.show()
