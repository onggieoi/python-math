# **Basic Packages, Functions, and Concepts**

## **Python numerical types**

Python provides basic numerical types such as arbitrarily sized integers and floating-point
numbers (double precision) as standard, but it also provides several additional types that
are useful in specific applications where precision is especially important. Python also
provides (built-in) support for complex numbers, which are useful for some more advanced
mathematical applications.

#### **Decimal type**
> `from decimal import Decimal` \
  `num1 = Decimal('1.1')` \
  `num2 = Decimal('1.563')` \
  `num1 + num2` # Decimal('2.663')

The Decimal type is based on the [IBM General Decimal Arithmetic Specification](http://speleotrove.com/decimal/decarith.html)

The decimal package also provides a Context object, which allows fine-grained control
over the precision, display, and attributes of Decimal objects.

#### **Fraction type**
Alternatively, for working with applications that require accurate representations of integer
fractions, such as when working with proportions or probabilities, there is the
Fraction type from the fractions module in the Python Standard Library
> `from fractions import Fraction` \
  `num1 = Fraction(1, 3)` \
  `num2 = Fraction(1, 7)` \
  `num1 * num2` # Fraction(1, 21)

#### **Complex type**
Special "complex number" - aware mathematical functions are provided in the
cmath module of the Python Standard Library.
> `z = 1 + 1j` \
  `z + 2 # 3 + 1j` \
  `z.conjugate()` # 1 - 1j

## **Basic mathematical functions**
Logarithms can be used to scale data that grows exponentially to give linear data. The exponential function and trigonometric functions are common fixtures when working with geometric information, the gamma function appears in combinatorics, and the Gaussian error function is important in statistics.

The *math* module in the Python Standard Library provides all of the standard
mathematical functions, along with common constants and some utility functions
> `import math` \
  `math.sqrt(4)` # 2.0

The trigonometric functions, sine, cosine, and tangent, are available under their common
abbreviations sin, cos, and tan
> `theta = pi/4` \
  `math.cos(theta)` # 0.7071067811865476 \
  `math.sin(theta)` # 0.7071067811865475 \
  `math.tan(theta)` # 0.9999999999999999

The inverse trigonometric functions are named acos, asin, and atan
> `math.asin(-1)` # -1.5707963267948966 \
  `math.acos(-1)` # 3.141592653589793 \
  `math.atan(1)` # 0.7853981633974483

The log function in the math module performs logarithms. It has an optional argument to
specify the base of the logarithm (note that the second argument is positional only). By
default, without the optional argument, it is the **natural logarithm** with base e. The e
constant can be accessed using `math.e`
> `math.log(10)` # 2.302585092994046 \
  `math.log(10, 10)` # 1.0

The math module also contains the function gamma, which is the gamma function, and the
function erf, the Gaussian error function, which is important in statistics. Both of these
functions are defined by integrals.
> `math.gamma(5)` # 24.0
  `math.erf(2)` # 0.9953222650189527

The functions comb and factorial, which are useful in a variety of applications. The comb function called with arguments n and k returns the number of ways to choose k items from a collection of n without repeats if order is not important
> `math.comb(5, 2)` # 10 \
  `math.factorial(5)` # 120

The **math** module also contains a function that returns the **greatest common divisor** of its arguments called **gcd**. The greatest common divisor of a and b is the largest integer k such
that k divides both a and b exactly:
> `math.gcd(2, 4)` # 2 \
`math.gcd(2, 3)` # 1

The **fsum** function performs addition on an iterable of numbers and keeps track of the sums
each step to reduce the error in the result
> `nums = [0.1]*10` # list containing 0.1 ten times \
  `sum(nums)` # 0.9999999999999999 \
  `math.fsum(nums)` # 1.0

The **isclose** function returns **True** if the difference between the arguments is smaller than the tolerance

The **floor** and **ceil** functions from math provide the floor and ceiling of their
argument.
  - The floor of a number *x* is the largest integer *f* with *f ≤ x*,
  - the ceiling of *x* is the smallest integer *c* with *x ≤ c*.

## **NumPy arrays**
NumPy provides high performance array types and routines for manipulating these arrays
in Python. These arrays are useful for processing large datasets where performance is
crucial. NumPy forms the base for the numerical and scientific computing stack in Python.
Under the hood, NumPy makes use of low-level libraries for working with vectors and
matrices, such as the **Basic Linear Algebra Subprograms (BLAS)** package, and the **Linear
Algebra Package (LAPACK)** contains more advanced routines for linear algebra.

> `import numpy as np`

The basic type provided by the NumPy library is the ndarray type (henceforth referred to
as a NumPy array). Generally, you won't create your own instances of this type, and will
instead use one of the helper routines such as array to set up the type correctly. The array
routine creates NumPy arrays from an array-like object, which is typically a list of numbers
or a list of lists (of numbers).

> `array = np.array([1, 2, 3, 4])` # array([1, 2, 3, 4]) \
  `np.array([1, 2, 3, 4], dtype=np.float32)` # array([1., 2., 3., 4.], dtype=float32)

Under the hood, a NumPy array of any shape is a buffer containing the raw data as a flat
(one-dimensional) array, and a collection of additional metadata that specifies details such
as the type of the elements.

Modifying the dtype attribute will have undesirable consequences since the raw
bytes that constitute the data in the array will simply be reinterpreted as the new data type.

> `arr = np.array([1, 2, 3, 4])` \
`print(arr.dtype)` # dtype('int64') \
`arr.dtype = np.float32` \
`print(arr)` # [1.e-45 0.e+00 3.e-45 0.e+00 4.e-45 0.e+00 6.e-45 0.e+00]

> `arr = arr.astype(np.float32)` # [1. 2. 3. 4.]

#### **Element access**
> `ary = np.array([1, 2, 3, 4])`\
  `ary[0]` # 1\
  `ary[2]` # 3

This also includes the usual slice syntax for extracting an array of data from an existing
array. A slice of an array is again an array, containing the elements specified by the slice\
The syntax for a slice is start:stop:step.
> `first_two = ary[:2]` # array([1, 2]) \
  `even_idx = ary[::2]` # array([1, 3])

#### **Array arithmetic and functions**
NumPy provides a number of *universal functions* (ufunc), which are routines that can
operate efficiently on NumPy array types.

#### **Useful array creation routines**
To generate arrays of numbers at regular intervals between two given end points, you can
use either the arange routine or the linspace routine. The difference between these two
routines is that linspace generates a number (the default is 50) of values with equal
spacing between the two end points, including both endpoints, while arange generates
numbers at a given step size up to, but not including, the upper limit. 
- The linspace routine generates values in the closed interval **a ≤ x ≤ b**
- The arange routine generates values in the half-open interval **a ≤ x < b**
> `np.linspace(0, 1, 5)` # array([0., 0.25, 0.5, 0.75, 1.0])\
  `np.arange(0, 1, 0.3)` # array([0.0, 0.3, 0.6, 0.9])

#### **Higher dimensional arrays**
NumPy can create arrays with any number of dimensions, which are created using the
same array routine as simple one-dimensional arrays. The number of dimensions of an
array is specified by the number of nested lists provided to the array routine
> `mat = np.array([[1, 2], [3, 4]])`

NumPy arrays have a shape attribute, which describes the arrangement of the elements in
each dimension.
> `vec = np.array([1, 2])`\
  `mat.shape` # (2, 2)\
  `vec.shape` # (2,)

Since the data in a NumPy array is stored in a flat (one-dimensional) array, an array can be
reshaped with little cost by simply changing the associated metadata. This is done using
the reshape method on a NumPy array
> `mat.reshape(4,)` # array([1, 2, 3, 4])


## **Matrices**

One of the most important attributes of a matrix is its shape, defined exactly as for NumPy
arrays. A matrix with m rows and n columns is usually described as an m × n matrix. A
matrix that has the same number of rows as columns is said to be a square matrix, and these
matrices play a special role in the theory of vectors and matrices.

The *identity matrix* (of size n) is the n × n matrix where the (i, i)-th entry is 1, and the (i, j)-th entry is zero for i ≠ j. There is an array creation routine that gives an n × n identity matrix for a specified n value:

> `np.eye(3)` array([[1., 0., 0.],
                    [0., 1., 0.],
                    [0., 0., 1.]])

#### **Basic methods and properties**
There are a large number of terms and quantities associated with matrices. We only
mention two such properties here, since they will be useful later. These are the `transpose` of a matrix, where rows and columns are interchanged, and the trace of a square matrix, which
is the sum of the elements along the leading diagonal. The leading diagonal consists of the
elements aii along the line from the top left of the matrix to the bottom right.
> `mat = np.array([[1, 2], [3, 4]])` \
  `mat.transpose()` # array([[1, 3],
                            [2, 4]]) \
  `mat.T` # array([[1, 3],[2, 4]])

Another quantity associated with matrices that is occasionally useful is the `trace`.
The trace of a square matrix A, with entries as in the preceding code, is defined to be the
sum of the elements along the leading diagonal, which consists of the elements starting
from the top left diagonally to the bottom right
> `A = np.array([[1, 2], [3, 4]])` \
  `A.trace()` # 5

#### **Matrix multiplication**
Matrix multiplication is an operation performed on two matrices, which preserves some of
the structure and character of both matrices. Formally, if A is an `l × m` matrix, and B is an
`m × n` matrix

Python has an operator reserved for matrix multiplication @, this is fundamentally different from the component-wise multiplication of arrays *
> `A = np.array([[1, 2], [3, 4]])`\
  `B = np.array([[-1, 1], [0, 1]])`\
  `A @ B` # array([[-1, 3],
                  [-3, 7]]) \
  `A * B` # different from A @ B =>  array([[-1, 2],
                                        [ 0, 4]])

The identity matrix is a neutral element under matrix multiplication. That is, if A is any l ×
m matrix, and I is the m × m identity matrix, then AI = A.
> `A = np.array([[1, 2], [3, 4]])` \
  `I = np.eye(2)` \
  `A @ I` # array([[1, 2],
                  [3, 4]])

#### **Determinants and inverses**
The `determinant` of a square matrix is important in most applications because of its strong
link with finding the inverse of a matrix. A matrix is `square` if the number of rows and
columns are equal. In particular, a matrix that has a non-zero determinant has a (unique)
inverse, which translates to unique solutions of certain systems of equations. The
determinant of a matrix is defined recursively

The NumPy routine for computing the determinant of a matrix is contained in a separate
module called `linalg`. This module contains many common routines for `linear algebra`,
which is the branch of mathematics that covers vector and matrix algebra
> `from numpy import linalg` \
  `linalg.det(A)` # -2.0000000000000004

The `inverse` of an `n × n` matrix A is the (necessarily unique) `n × n` matrix B, such
that `AB = BA = I`, where I denotes the n × n identity matrix and the multiplication
performed here is matrix multiplication. Not every square matrix has an inverse; those that
do not are sometimes called `singular` matrices. In fact, a matrix is non-singular (that is, has an inverse) if, and only if, the determinant of that matrix is not 0. When A has an inverse, it is customary to denote it by A -1.
> `linalg.inv(A)` # array([[-2. , 1. ],
                          [ 1.5, -0.5]])

> `Ainv = linalg.inv(A)` \
  `Ainv @ A` # Approximately array([[1., 0.],
                                    [0., 1.]]) \
  `A @ Ainv` # Approximately array([[1., 0.],
                                    [0., 1.]])

The linalg package also contains a number of other methods such as `norm`, which
computes various norms of a matrix. It also contains functions for decomposing matrices in
various ways and solving systems of equations. 

There are also the matrix analogues of the exponential function `expm`, the logarithm
`logm`, sine `sinm`, cosine `cosm`, and tangent `tanm`. The matrix exponential function is defined using a "power series" of matrices.

#### **Systems of equations**
Solving systems of (linear) equations is one of the main motivations for studying matrices
in mathematics. Problems of this type occur frequently in a variety of applications.

> `import numpy as np` \
  `from numpy import linalg` \
  \
  `A = np.array([[3, -2, 1], [1, 1, -2], [-3, -2, 1]])` \
  `b = np.array([7, -4, 1])` \
  `linalg.solve(A, b)` # array([ 1., -1., 2.])

The `solve` function expects two inputs, which are the matrix of coefficients A and the righthand side vector b. It solves the system of equations using LAPACK routines that
decompose matrix A into simpler matrices to quickly reduce to an easier problem that can
be solved by simple substitution. This technique for solving matrix equations is extremely
powerful and efficient, and is less prone to the floating-point rounding errors that dog
some other methods. For instance, the solution to a system of equations could be computed
by multiplying (on the left) by the inverse of the matrix A, if the inverse is known.
However, this is generally not as good as using the solve routine since it may be slower or
result in larger numerical errors.

#### **Eigenvalues and eigenvectors**
Consider the matrix equation `Ax = λx`, where A is a square (n × n) matrix, x is a vector, and λ is a number. Numbers λ for which there is an x that solves this equation are
called eigenvalues, and the corresponding vectors x are called eigenvectors. Pairs of
eigenvalues and corresponding eigenvectors encode information about the matrix A, and
are therefore important in many applications where matrices appear.
> `import numpy as np` \
  `from numpy import linalg` \
  `A = np.array([[3, -1, 4], [-1, 0, -1], [4, -1, 2]])`

The eig routine in the linalg module is used to find the eigenvalues and eigenvectors of a
square matrix. This routine returns a pair (v, B) where v is a one-dimensional array
containing the eigenvalues and B is a two-dimensional array whose columns are the
corresponding eigenvectors:
> `v, B = linalg.eig(A)`

It is perfectly possible for a matrix with only real entries to have complex eigenvalues and
eigenvectors. For this reason, the return type of the eig routine will sometimes be a
complex number type such as complex32 or complex64. In some applications, complex
eigenvalues have a special meaning, while in others we only consider the real eigenvalues.

> `i = 0` # first eigenvalue/eigenvector pair \
  `lambda0 = v[i]` \
  `print(lambda0)` # 6.823156164525971 \
  `x0 = B[:, i]` # ith column of B \
  `print(x0)` # array([ 0.73271846, -0.20260301, 0.649672352])

The eigenvectors returned by the `eig` routine are `normalized` so that they have norm (length) 1. (The `Euclidean norm` is defined to be the square root of the sum of the squares of the members of the array.)
> `linalg.norm(x0)` # 1.0 - eigenvectors are normalized.

we can check that these values do indeed satisfy the definition of an
eigenvalue/eigenvector pair by computing the product `A @ x0` and checking that, up to
floating-point precision, this is equal to `lambda0*x0`:
> `lhs = A @ x0` \
  `rhs = lambda0*x0` \
  `linalg.norm(lhs - rhs)` # 2.8435583831733384e-15 - very small.

The `eig` routine is a wrapper around the low-level LAPACK routines for computing
eigenvalues and eigenvectors. The theoretical procedure for finding eigenvalues and
eigenvectors is to first find the eigenvalues by solving the equation

One key application of eigenvalues and eigenvectors is in `principal component analysis`,
which is a key technique for reducing a large, complex dataset to better understand the
internal structure. We can only compute eigenvalues and eigenvectors for square matrices; for non-square matrices, the definition does not make sense. There is a generalization of eigenvalues and eigenvalues to non-square matrices called `singular values`.

#### **Sparse matrices**
Systems of linear equations such as those discussed earlier are extremely common
throughout mathematics and, in particular, in mathematical computing. In many
applications, the coefficient matrix will be extremely large, with thousands of rows and
columns, and will likely be obtained from an alternative source rather than simply entering
by hand. In many cases, it will also be a sparse matrix, where most of the entries are 0.

A matrix is `sparse` if a large number of the elements are zero. The exact number of elements
that need to be zero in order to call a matrix sparse is not well defined. Sparse matrices can
be represented more efficiently, for example, by simply storing the indexes `(i, j)` and the
values `ai,j` that are non-zero. There are entire collections of algorithms for sparse matrices that offer great improvements in performance, assuming the matrix is indeed sufficiently sparse.

Sparse matrices appear in many applications, and often follow some kind of pattern. In
particular, several techniques for solving **partial differential equations (PDEs)** involve
solving sparse matrix equations, and matrices associated with networks are often sparse.

The `sparse` module contains several different classes representing the different means of
storing a sparse matrix. The most basic means of storing a sparse matrix is to store three
arrays, two containing integers representing the indices of non zero elements, and the third
the data of the corresponding element. This is the format of the `coo_matrix` class. Then
there are the compressed column CSC `(csc_matrix)` and the compressed row CSR
`(csr_matrix)` formats, which provide efficient column or row slicing, respectively. There
are three additional sparse matrix classes in `sparse`, including `dia_matrix`, which
efficiently stores matrices where the non-zero entries appear along a diagonal band.

> `import numpy as np` \
  `from scipy import sparse` \
  \
  `A = np.array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])` \
  `sp_A = sparse.csr_matrix(A)` \
  `T = sparse.diags([-1, 2, -1], (-1, 0, 1), shape=(5, 5), format="csr")`
  `T.toarray()`\
   array([[ 2, -1, 0, 0, 0], \
          [-1, 2, -1, 0, 0], \
          [ 0, -1, 2, -1, 0], \
          [ 0, 0, -1, 2, -1], \
          [ 0, 0, 0, -1, 2]])

Once a matrix is stored in a sparse format, we can use the sparse solving routines in
the linalg submodule of sparse.
> `from scipy.sparse import linalg` \
  `linalg.spsolve(T.tocsr(), np.array([1, 2, 3, 4, 5]))` \
    array([ 5.83333333, 10.66666667, 13.5 , 13.33333333, 9.16666667])