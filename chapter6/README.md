# **Working with Data and Statistics**
=================================================

Statistics is the systematic study of data using mathematical—specifically, probability—theory. There are two aspects to statistics. The first is to find numerical values
that describe a set of data, including characteristics such as the center (mean or median) and spread (standard deviation or variance) of the data. The second aspect of statistics is
inference, describing a much larger set of data (a population) using a relatively small sample dataset.


## **Creating Series and DataFrame objects**

> Most data handling in Python is done using the pandas library, which builds on NumPy to provide R-like structures for holding data. These structures allow the easy indexing of rows
and columns, using strings or other Python objects besides just integers. Once data is loaded into a pandas DataFrame or Series, it can be easily manipulated, just as if it were
in a spreadsheet. This makes Python when combined with pandas a powerful tool for processing and analyzing data.

### **[Padas](https://pandas.pydata.org/docs/user_guide/indexing.html)**

> The pandas package provides the Series and DataFrame classes, which mirror the function and capabilities of their R counterparts. Series is used to store one-dimensional
data, such as time-series data, and DataFrame is used to store multidimensional data; DataFrame object could be seem as a "spreadsheet." What separates Series from a simple 
NumPy ndarray is the way that Series indexes its items. A NumPy array is indexed by integers, which is also the default for a Series object. However, Series can be indexed by 
any hashable Python object, including strings and datetime objects. This makes Series useful for storing time-series data. A Series can be created in a number of ways. In this 
recipe, we used a NumPy array, but any Python iterable, such as a list, can be used instead. Each column in a DataFrame object is a series containing rows, just as in a traditional
database or spreadsheet. In this recipe, the columns are given labels when the DataFrame object is constructed via the keys of the dictionary. The DataFrame and Series objects 
create a summary of the data they contain when printed. This includes column names, the number of rows and columns, and the first and last five rows of the frame (series). This 
is useful for quickly obtaining an overview of the object and the spread of data it contains.

> The individual rows (records) of a Series object can be accessed using the usual index notation by providing the corresponding index. We can also access the rows by their
numerical position using the special iloc property object. This allows us to access the rows by their numerical (integer) index, such as with Python lists or NumPy arrays.
The columns in a DataFrame object can be accessed using the usual index notation, providing the name of the column. The result of this is a Series object that contains the
data from the selected column. DataFrames also provides two properties that can be used to access data. The loc attribute provides access to individual rows by their index,
whatever this object may be. The iloc attribute provides access to the rows by numerical index, just as for the Series object. You can provide selection criteria to loc 
(or just using index notation for the object) to select data. This includes a single label, a list of labels, a slice of labels,  or a Boolean array (of an appropriate size).
The iloc selection method accepts similar criteria. There are other ways to select data from a Series or DataFrame object beyond the simple methods we describe here. For example, 
we can use the at attribute to access a single value at a specified row (and column) in the object.


## **Getting descriptive statistics from a DataFrame**

> Descriptive statistics, or summary statistics, are simple values associated with a set of data, such as the mean, median, standard deviation, minimum, maximum, and quartile 
values. These values describe the location and spread of a dataset in various ways. The mean and median are measures of the center (location) of the data, and the other values 
measure the spread of the data from the mean and median. These statistics are vital in understanding a dataset and form the basis for many techniques for analysis.


## **Understanding a population using sampling**

> One of the central problems in statistics is to make estimations and quantify how good these estimations are of the distribution of an entire population given only a small
(random) sample. A classic example is to estimate the average height of all the people in a country when measuring the height of a randomly selected sample of people. These kinds
of problems are particularly interesting when the true population distribution, by which we usually mean the mean of the whole population, cannot feasibly be measured. In this case,
we must rely on our knowledge of statistics and a (usually much smaller) randomly selected sample to estimate the true population mean and standard deviation, and also
quantify how good our estimations are. It is the latter that is the source of confusion, misunderstanding, and misrepresentation of statistics in the wider world. 
