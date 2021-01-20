# **Calculus and Differential Equations**
Calculus is the branch of mathematics that concerns the processes of differentiation and integration. 
Geometrically, the derivative of a function represents the gradient of the curve of the function, and 
the integral of a function represents the area below the curve of the function

## **Working with polynomials and calculus**

Polynomials are among the simplest functions in mathematics and are defined as a sum:
> `p(x) = a0 + a1x + a2x^2 + ... + a(n)x^n`

Calculus concerns the differentiation and integration of functions. Integration is, roughly speaking, 
anti-differentiation, in the sense that first integrating and then differentiating yields the original 
function.

Polynomials offer an easy introduction to the basic operations of calculus, but it isn't so
easy to construct Python classes for other general classes of functions. That being said,
polynomials are extremely useful because they are well understood and, perhaps more
importantly, calculus for polynomials is very easy. For powers of a variable x, the rule for
differentiation is to multiply by the power and reduce the power by 1, so
that `xn` becomes `nxn-1`.

Integration is more complex, since the integral of a function is not unique. We can add any
constant to an integral and obtain a second integral. For powers of a variable x, the rule for
integration is to increase the power by 1 and divide by the new power, so
that `xn` becomes `(x^(n+1))/(n+1)`, so to integrate a polynomial, we increase each power of x by 1
and divide the corresponding coefficient by the new power.

## **Differentiating and integrating symbolically using SymPy**
## **Solving equations**
## **Integrating functions numerically using SciPy**
## **Solving simple differential equations numerically**
## **Solving systems of differential equations**
## **Solving partial differential equations numerically**
## **Using discrete Fourier transforms for signal processing**