# Copyright (c) 2021, srowanphys
# All rights reserved.

# This source code is licensed under the Apache 2.0 license found in the
# LICENSE.md file in the root directory of this source tree.

# The following code constructs an basic program for calculating average acceleration
# The program is written in the Python language
# All lines starting with a '#' symbol are so-called 'comments' and are not part of the program, but rather just helpful notes for the reader

# Here we define (def) a function called calculate_average_acceleration()
# - The calculation follows: average_acceleration (a-bar)= (final_velocity (v_f) - initial_velocity (v_0)) / (final_time (t_f) - initial_time (t_0))
# - directionality (think coord system) determines positive or negative result
def calculate_average_acceleration(initial_velocity, final_velocity, initial_time, final_time):
    average_acceleration = ((final_velocity - initial_velocity)/(final_time - initial_time))
    print("Average Acceleration:", average_acceleration, "m/s^2")

# Here we define the values for the initial and final velocity and time
# You may change the values to change the calculated average acceleration

initial_velocity = 1
final_velocity = 5
initial_time = 0
final_time = 2

# Below we run the program and call the calculate_average_acceleration() function
# As a beginner, you may ignore the rest of the code, it is only to ensure the progam file stay open so you can see the result

if __name__ == '__main__':
    try:
        calculate_average_acceleration(initial_velocity, final_velocity, initial_time, final_time)
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        input("\nPlease press [Enter] to exit.")
