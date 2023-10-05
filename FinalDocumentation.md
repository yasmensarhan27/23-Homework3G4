**Background:**
A brief introduction of lambda function and map function is given.

**Lambda Function:**
A lambda function, also known as an anonymous function or lambda expression, is a way to create small, inline, and nameless functions in Python. Lambda functions are typically used for simple operations or calculations.


**Example of Lambda function**
- add = lambda x, y: x + y  
result = add(3, 5)  
print(result)
##### Output: 8  
- numbers = [1, 2, 3, 4, 5]  
squared = list(map(lambda x: x**2, numbers))  
print(squared)
##### Output: [1, 4, 9, 16, 25]  



**Map Function:**

The map() function in Python is used to apply a given function to all elements of an iterable (e.g., a list, tuple, or other iterable data structures) and return an iterator. It takes two arguments: the function to apply and the iterable to apply it to. The result is an iterator that yields the results of applying the function to each element of the iterable one by one.



**Example of syntax of map function**

- numbers = [1, 2, 3, 4, 5]  
  squared = list(map(lambda x: x**2, numbers))  
 print(squared)
  ##### Output: [1, 4, 9, 16, 25]



>**Work Calculation and Testing Script by using lambda function and map function:**

This Python script defines a function for calculating work done by a car as a function of its velocities and mass.
It also includes a test function to ensure the correctness of the work calculation function.


**Steps:**
1) Define a function calculate_work_done(velocities, mass).
2) Calculates the work done by a car based on its velocities and mass.
3) Define parameters.
   velocities (list of float): A list of velocities (in m/s) at different points in time.
   mass (float): The mass of the car (in kilograms).
4) Returns:
    - `work_done` (list of float): A list of work done (in joules) at each point in time.
5) test_calculate_work_done()`: Tests the `calculate_work_done` function to ensure its correctness.

6) Usage:
    1. Defines given data (velocities in mph, conversion factor, mass of car).
    2. Converts velocities from mph to m/s by using the lambda function.
    3. Get a list of velocities in m/s by using the map function.
    4. Manually calculate the expected work done at each point.
    5. Calls `calculate_work_done` to calculate work done.
    6. Compares the calculated and expected values within a small tolerance.
    7. Prints the calculated work done.


**Code**
[WorkDonebyMapAndLambda.md](https://github.com/sharmistharanit/23-Homework3G4/files/12807475/WorkDonebyMapAndLambda.md)

**Pylint Output**
[pylint_output_WorkDone.txt](https://github.com/sharmistharanit/23-Homework3G4/files/12810929/pylint_output_WorkDone.txt)

**References:**
1) https://docs.python.org/3/howto/functional.html#small-functions-and-the-lambda-expression
2) https://docs.python.org/3/library/functions.html#map
3) https://docs.python.org/3/howto/functional.html
4) ChatGPT
