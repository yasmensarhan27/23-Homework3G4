# Import the required libraries for testing
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
    velocities_mph = [10, 5, 4, 3, 4]
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

    rounded_work = []
    for i in calculated_work_done:
        rounded_number = round(i, 2)
        rounded_work.append(rounded_number)
    print(rounded_work)


# Run the test function
test_calculate_work_done()
