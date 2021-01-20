# **Randomness and Probability**
===========================================

  ## **Selecting items at random**

> At the core of probability and randomness is the idea of selecting an item from some kind of collection. As we know, the probability of selecting an item from a collection quantifies
the likelihood of that item being selected. Randomness describes the selection of items from a collection according to the probabilities without any additional bias. The opposite of a
random selection might be described as a deterministic selection. In general, it is very difficult to replicate a purely random process using a computer, because computers and
their processing are inherently deterministic. However, we can generate sequences of pseudo-random numbers that, when properly constructed, demonstrate a reasonable
approximation of randomness.


  ## **Generating random data**

> Many tasks involve generating large quantities of random numbers, which, in their most basic form, are either integers or floating-point numbers (double precision) lying in the
range 0 ≤ x < 1. Ideally, these numbers should be selected uniformly, so that if we draw a large quantity of such numbers, they should be distributed roughly evenly across the
range 0 ≤ x < 1. In this recipe, we will see how to generate large quantities of random integers and floatingpoint numbers using NumPy, and show the distribution of these numbers 
using a histogram

  ## **Changing the random number generator**

> The random module in NumPy provides several alternatives to the default PRNG, which uses a 128-bit permutation congruential generator. While this is a good general-purpose
random number generator, it might not be sufficient for your particular needs. For example, this algorithm is very different from the one used in Python’s internal random
number generator. We will follow the guidelines for best practice set out in the NumPy documentation for running repeatable, but suitably random, simulations.
In this recipe, we will show you how to change to an alternative pseudo random number generator, and how to use seeds effectively in your programs.

  ## **Generating normally distributed random numbers**

> In the Generating random data recipe, we generated random floating-point numbers following a uniform distribution between 0 and 1, but not including 1. However, in most
cases where we require random data, we need to instead follow one of several different distributions. Roughly speaking, a distribution function is a function f(x)
that describes the probability that a random variable has a value that is below x. In practical terms, the distribution describes the spread of the random data over a range.
In particular, if we create a histogram of data that follows a particular distribution, then it should roughly resemble the graph of the distribution function.

  ## **Working with random processes**

> Random processes exist everywhere. Roughly speaking, a random process is a system of related random variables, usually indexed with respect to time t ≥ 0, for a continuous
random process, or by natural numbers n = 1, 2, …, for a discrete random process. Many (discrete) random processes satisfy the Markov property, which makes them a Markov
chain. The Markov property is the statement that the process is memoryless, in that only the current value is important for the probabilities of the next value. 

  ## **Analyzing conversion rates with Bayesian techniques**

> Bayesian probability allows us to systematically update our understanding (in a probabilistic sense) of a situation by considering data. In more technical language, we
update the prior distribution (our current understanding) using data to obtain a posterior distribution

  ## **Estimating parameters with Monte Carlo simulations**

> Monte Carlo methods broadly describe techniques that use random sampling to solve problems. These techniques are especially powerful when the underlying problem involves
some kind of uncertainty. The general method involves performing large numbers of simulations, each sampling different inputs according to a given probability distribution,
and then aggregating the results to give a better approximation of the true solution than any individual sample solution. Markov Chain Monte Carlo (MCMC) is a specific kind 
of Monte Carlo simulation in which we construct a Markov chain of successively better approximations of the true distribution that we seek. This works by accepting or rejecting
a proposed state, sampled at random, based on carefully selected acceptance probabilities at each stage, with the aim of constructing a Markov chain whose unique stationary 
distribution is precisely the unknown distribution that we wish to find.
