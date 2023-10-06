import hw_work_done_G4  # Import the function from the module

# Given data
velocities_mph = [10, 20, 30, 40, 50]  # List of velocities in miles per hour
time_hours = 1  # Time in hours
mph_to_mps = 0.44704  # Conversion factor to convert miles per hour to meters per second
mass_of_car = 1000  # Mass of the car in kilograms

# Convert velocities from miles per hour to meters per second using a lambda function
convert_to_mps = lambda v_mph: v_mph * mph_to_mps
velocities_mps = list(map(convert_to_mps, velocities_mph))

# Calculate work done at each point and store it in a list
work_done_list = list(calculate_work_done(velocities_mps, mass_of_car))
work_done_new=[]
for i in work_done_list:
  work=round(i,2)
  work_done_new.append(work)
print(work_done_new)  # Print the list of work done at each velocity point

# Calculate work done at each point again and estimate the overall work done by summing them up
total_work_done = 0
for delta_ke in calculate_work_done(velocities_mps, mass_of_car):
    total_work_done += delta_ke
total_work=round(total_work_done,2)
# Output the overall work done in Joules
print("Overall Work Done:", total_work, "Joules")
