[WorkDonebyMapAndLambda.md](https://github.com/sharmistharanit/23-Homework3G4/files/12806367/WorkDonebyMapAndLambda.md)>**Work Calculation and Testing Script by using lambda function and map function:**

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



 **Code:**

import math

# Define a function to calculate work done
def calculate_work_done(velocities, mass):
    work_done = []
    prev_velocity = 0
    for velocity in velocities:
        delta_ke = 0.5 * mass * (velocity**2 - prev_velocity**2)
        prev_velocity = velocity
        work_done.append(delta_ke)
    return work_done

# Define a function to test the calculate_work_done function
def test_calculate_work_done():
    # Given data
    velocities_mph = [10, 20, 30, 40, 0]
    mph_to_mps = 0.44704
    mass_of_car = 1000

    # Convert velocities from mph to m/s using the same lambda function
    convert_to_mps = lambda v_mph: v_mph * mph_to_mps
    velocities_mps = list(map(convert_to_mps, velocities_mph))
# Calculate the expected work done at each point manually
    expected_work_done = []
    prev_velocity = 0
    for velocity in velocities_mps:
        delta_ke = 0.5 * mass_of_car * (velocity**2 - prev_velocity**2)
        prev_velocity = velocity
        expected_work_done.append(delta_ke)

    # Calculate work done using the calculate_work_done function
    calculated_work_done = list(calculate_work_done(velocities_mps, mass_of_car))

    # Assert that the calculated work done matches the expected values
    for expected, calculated in zip(expected_work_done, calculated_work_done):
        assert math.isclose(expected, calculated, rel_tol=1e-9), f"Expected {expected}, but got {calculated}"

    print(calculated_work_done)

# Run the test function
test_calculate_work_done()
```

    [9992.238079999997, 29976.714239999994, 49961.1904, 69945.66655999998, -159875.80927999996]



```python

```
ploading WorkDonebyMapAndLambda.md…]()

