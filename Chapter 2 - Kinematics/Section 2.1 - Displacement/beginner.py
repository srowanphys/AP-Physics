# Copyright (c) 2021, srowanphys
# All rights reserved.

# This source code is licensed under the Apache 2.0 license found in the
# LICENSE.md file in the root directory of this source tree.

# The following code constructs an basic program for calculating displacement
# The program is written in the Python language
# All lines starting with a '#' symbol are so-called 'comments' and are not part of the program, but rather just helpful notes for the reader

# Here we define (def) a function called calculate_displacement() which contains the displacement equation in a readable code format
# After calculating the displacement, the function then prints the result in the python window

def calculate_displacement(initial_position, final_position):
    displacement = final_position - initial_position
    print("Displacement:", displacement, "m")

# Here we define the values for the initial and final positions
# You may change the values to change the calculated displacement

initial_position = 1
final_position = -5

# Below we run the program and call the calculate_displacement() function
# As a beginner, you may ignore the rest of the code, it is only to ensure the progam file stay open so you can see the result

if __name__ == '__main__':
    try:
        calculate_displacement(initial_position, final_position)
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        input("\nPlease press [Enter] to exit.")
