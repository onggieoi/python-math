# **Finding Optimal Solutions**
==============================================================================

The algorithms available to us for minimizing a given function depend on the nature of the function. For instance, a simple linear function containing one or more 
variables has different algorithms available compared to a non-linear function with many variables. The minimization of linear functions falls within the category 
of linear programming, which is a well-developed theory. For non-linear functions, we usually make use of the gradient (derivative) of a function in order to find 
the minimum points. We will discuss several methods for minimizing various functions of different types. Finding the minima and maxima of the functions of a single
variable is especially simple, and can be done easily if the derivatives of the function are known. If not, then the method described in the appropriate recipe will 
be applicable. The notes in the Minimizing a nonlinear function recipe give some extra details about this.


## **Minimizing a simple linear function**

> The most basic type of problem we face in optimization is finding the parameters where a function takes its minimum value. Usually, this problem is constrained by some bounds on
> the possible values of the parameters, which increases the complexity of the problem. Obviously, the complexity of this problem increases further if the function that we are
> minimizing is also complex. For this reason, we must first consider linear functions, which are in the following form:
