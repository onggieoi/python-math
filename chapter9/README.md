# **Finding Optimal Solutions**

The algorithms available to us for minimizing a given function depend on the nature of the function. For instance, a simple linear function containing one or more
variables has different algorithms available compared to a non-linear function with many variables. The minimization of linear functions falls within the category 
of linear programming, which is a well-developed theory. For non-linear functions, we usually make use of the gradient (derivative) of a function in order to find 
the minimum points. We will discuss several methods for minimizing various functions of different types. Finding the minima and maxima of the functions of a single
variable is especially simple, and can be done easily if the derivatives of the function are known. If not, then the method described in the appropriate recipe will 
be applicable. The notes in the Minimizing a nonlinear function recipe give some extra details about this.
## **Minimizing a simple linear function**

> The most basic type of problem we face in optimization is finding the parameters where a function takes its minimum value. Usually, this problem is constrained by some bounds on
the possible values of the parameters, which increases the complexity of the problem. Obviously, the complexity of this problem increases further if the function that we are
minimizing is also complex. For this reason, we must first consider linear functions, which are in the following form:
>
>> `f(x) = cx = c1x1 + c2x2 + ... + cnxn` 
>
> To solve these kinds of problems, we need to convert the constraints into a form that can be
used by the computer. In this case, we usually convert them into a linear algebra problem
(matrices and vectors). Once this is done, we can use the tools from the linear algebra
packages in NumPy and SciPy to find the parameters we seek. Fortunately, since these
kinds of problems occur quite frequently, SciPy has routines that handle this conversion
and subsequent solving.
## **Minimizing a non-linear function**

> We saw how to minimize a very simple linear function.
Unfortunately, most functions are not linear and usually don't have nice properties that we
would like. For these non-linear functions, we cannot use the fast algorithms that have been
developed for linear problems, so we need to devise new methods that can be used in these
more general cases. The algorithm that we will use there is called the Nelder-Mead
algorthim, which is a robust and general-purpose method that's used to find the minimum
value of a function and does not rely on the gradient of the function.

> The Nelder-Mead simplex method – not to be confused with the simplex method for linear
optimization problems – is a simple algorithm for finding the minimum values of a nonlinear function and works even when the objective function does not have a known
derivative. (This is not the case for the function in this recipe; the only gains from using a
gradient-based method is the speed of convergence.) The method works by comparing the
values of the objective function at the vertices of a simplex, which is a triangle in a twodimensional space. The vertex with the largest function value is "reflected" through the
opposite edge and performs an appropriate expansion or contraction that, in effect, moves
the simplex "downhill". 

> The Nelder-Mead algorithm is an example of a "gradient-free" minimization algorithm
since it does not require any information about the gradient (derivative) of the objective
function. There are several such algorithms, all of which typically involve evaluating the
objective function at a number of specified points, and then using this information to move
toward the minimum value. In general, gradient-free methods tend to converge more
slowly than gradient descent models. However, they can be used for almost any objective
function, even where it is not easy to compute the gradient either exactly or by means of
approximation.

## **Using gradient descent methods in optimization**

> We used the Nelder-Mead simplex algorithm to minimize a nonlinear function containing two variables. This is a fairly robust method that works even if
very little is known about the objective function. However, in many situations, we do know
more about the objective function, and this fact allows us to devise faster and more efficient
algorithms for minimizing the function. We can do this by making use of properties such as
the gradient of the function.

> The gradient of a function of more than one variable describes the rate of change of the
function in each of its component directions. This is a vector of the partial derivatives of the
function with respect to each of the variables. From this gradient vector, we can deduce the
direction in which the function is increasing most rapidly and, conversely, the direction in
which the function is decreasing most rapidly from any given position. This gives us the
basis for gradient descent methods for minimizing a function. The algorithm is very simple:
given a starting position, x, we compute the gradient at this x and the corresponding
direction in which the gradient is most rapidly decreasing, then make a small step in that
direction. After a few iterations, this will move from the starting position to the minimum
of the function.

## **Using least squares to fit a curve to data**

> Least squares is a powerful technique for finding a function from a relatively small family
of potential functions that best describe a particular set of data. This technique is especially
common in statistics. For example, least squares is used in linear regression problems –
here, the family of potential functions is the collection of all linear functions. Usually, this
family of functions that we try to fit has relatively few parameters that can be adjusted to
solve the problem. The idea of least squares is relatively simple. For each data point, we compute the square of the residual – the difference between the value of the point and the expected value given a function – and try to make the sum of these squared residuals as small as possible (hence
least squares).