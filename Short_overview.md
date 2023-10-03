# Tentative Idea of HW3G4 Task
Our main intention in this task will be "to find the work done at different points along the way, by calculating the change in kinetic energy, where the final velocity for the first point becomes the initial velocity for the second point and hance overall workdone". For this, we will proceed as follows;
- We will first convert a list of velocities from miles per hour to meters per second using the map function and the lambda           function "convert_to_mps". 
- We define a generator function "calculate_work_done" that calculates the work done at each point along the way by calculating the   change in kinetic energy.
- The generator yields the work done at each point.
- Finally, we iterate through the generator to calculate the work done at each point and accumulate it to find the overall work       done.
