# PR.4-Functional-Treat

PROJECT DOCUMENTATION

Data Analyzer and Transformer Program

1. Objective

The objective of this project is to design a menu-driven program that allows users to analyze and transform numerical data in different ways. The program helps users perform basic data analysis operations using functional programming concepts such as built-in functions, user-defined functions, recursion, lambda functions, sorting, and handling of one-dimensional and two-dimensional data.

2. User Interface Description

The program uses a menu-driven interface where the user is shown a list of options. The user selects an operation by entering the corresponding number. The program continues to run until the user selects the exit option. This interface makes the program easy to understand and user-friendly.

3. Data Input

The program allows the user to input data in two formats:

One-dimensional list (1D list)

Two-dimensional list (2D list or nested list)


The user manually enters numerical values. The entered data is stored globally so that it can be accessed by different operations throughout the program.


4. Built-in Functions Usage

The program uses Python built-in functions to perform basic statistical operations on the dataset. These include:

Finding the total number of elements

Finding the minimum value

Finding the maximum value

Calculating the sum of all values

Calculating the average of the dataset


These operations help in quickly summarizing the dataset.

5. User-Defined Functions

Each operation in the program is handled using separate user-defined functions. This improves readability, modularity, and reusability of the program. Examples of tasks handled by user-defined functions include data input, data summary, filtering, sorting, and statistical calculations.

6. Recursion

The program demonstrates recursion by calculating the factorial of a number. The factorial calculation is performed using a function that repeatedly calls itself until it reaches a base condition. This showcases the use of recursion in a real program.

7. Lambda Function

Lambda functions are used to filter dataset values based on a threshold provided by the user. The lambda function works together with filtering techniques to extract only the values that satisfy the given condition. This demonstrates functional programming concepts in Python.

8. Sorting Operations

The program supports sorting of data in both formats:

One-dimensional data is sorted directly in ascending order.

Two-dimensional data is sorted row-wise to show how structured data can be organized.


This helps users understand different sorting techniques for different data types.

9. Global Variable Usage

A global variable is used to store the dataset so that it can be accessed and modified across multiple functions. This allows smooth data flow between different parts of the program.

10. Returning Multiple Values

The program includes functionality where multiple statistical values such as minimum, maximum, and average are calculated together and returned at once. These values are then displayed individually to the user.

11. Program Flow

1. The program starts and displays the main menu.


2. The user selects an option from the menu.


3. The selected operation is performed on the dataset.


4. The program returns to the main menu after completing the operation.


5. The program exits when the user selects the exit option.

