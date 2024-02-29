# Python code - UniTS
This is the repository regarding the Introduction to Programming exam, specifically the Python section.

Assignment:

A univariate time series is a sequence of values ordered over time, expressing the variation of a certain phenomenon over time. For each pair of points, the first element corresponds to a specific moment or time interval, while the second is the value of a quantity related to that moment or interval.
The file 'data.csv' contains the time series of the total monthly number of passengers in thousands on international airlines, from January 1949 to December 1960. The first element of each row represents the date and is in Year-Month format.
The data is formatted as follows:

                                 date,passengers
                                 1949-01,112
                                 1949-02,118
                                 1949-03,132
                                 ...
We want to read this type of data and find for each year the month with the minimum and maximum number of passengers

More information about the assignment:
You must take into consideration that there may be missing data! In the measurements for a year, the number of passengers can be missing for one or more months. Additionally, there may be missing measurements for one or more entire years.
Use the `CSVTimeSeriesFile` class, modified or extended from the `CSVFile` class seen in class (or written from scratch). The class should be instantiated with the file name using the variable `name` and should have a method `get_data()` that returns a list of lists. In each nested list, the first element is the date, and the second is the number of passengers in numeric format.

This class should be used as follows:


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()


The content of the `time_series` variable returned by the `get_data()` method should be structured as a list of lists:


[
  ["1949-01", 112],
  ["1949-02", 118],
  ["1949-03", 132],
  ...
]


To find the months with the minimum and maximum monthly number of passengers, you need to create a separate function (defined NOT within the `CSVTimeSeriesFile` class but directly in the main program), named `find_min_max`. This function should take the time series as input and be used like this:


find_min_max(time_series)


The function should return an output dictionary of dictionaries, where the keys of the outer dictionary are the years (as strings), and the value for each year is another dictionary with two keys ('min' and 'max'). These keys should have lists as values containing the months (still in string format) with the minimum and maximum number of passengers for that specific year:


{"1951": {"min":["03"], "max":["01","07"]},
 "1952": {}, ...}


The file in which to write your code must be named "esame.py". The exceptions to be raised in case of incorrect input or edge cases must be instances of a specific class `ExamException`, defined in the code as follows (copy-paste these two lines):


class ExamException(Exception):
    pass


This exception should then be used as a regular exception, for example:

raise ExamException('Error, empty values list')

  - Please note, as mentioned above, that in the CSV file, we may have missing measurements for one or more months or even for one or more entire years.
  - As mentioned, we may also have years with multiple months having the same minimum or maximum number of passengers. For example, for the year 1949, we may have March and June with the minimum number of passengers and August with the         maximum number. The output of the function should include at least the months of March and June with the months ordered chronologically and at most only the month of August.
  - Expect the values read from the CSV file to be of integer type. A non-numeric value, or an empty or null value, or a negative value should not be accepted, but everything should proceed without raising exceptions.
  - Consider the time series in the CSV file to always be ordered. If there happens to be a timestamp out of order, an exception should be raised (within the get_data() function) without attempting to reorder the series. The same applies       if there is a duplicate timestamp: an exception is raised.
  - The CSV file can contain anything. From incomplete lines to pieces of text that have nothing to do with the data. Every error, except for a timestamp out of order or duplicate, should be ignored (i.e., ignore the line containing the        error and move on to the next). Note: if you can read two values (date and number of passengers) but there is an extra field on the same line, this should not be considered an error, and that line should not be ignored.
  - The CSVTimeSeriesFile class checks the existence of the file only when the get_data() method is called. In case the file does not exist or is not readable, an exception is raised."


Note well: your file should include ONLY one class, one function, and one exception. It should not include any "main" code or request user input.


