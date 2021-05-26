# Copyright (c) 2021, srowanphys
# All rights reserved.

# This source code is licensed under the Apache 2.0 license found in the
# LICENSE.md file in the root directory of this source tree.

# The following code constructs an interactive program for calculating average acceleration
# The program is written in the Python language
# All lines starting with a '#' symbol are so-called 'comments' and are not part of the program, but rather just helpful notes for the reader
# Most of the program consists of simple functions:
# - 'print()' to output a given message and/or result
# - 'input()' to prompt an input from the user (you!), e.g. entering a value for a variable

# Here we define (def) a function called calculate_average_acceleration()
# - The calculation follows: average_acceleration (a-bar)= (final_velocity (v_f) - initial_velocity (v_0)) / (final_time (t_f) - initial_time (t_0))
# - directionality determines positive or negative result
def calculate_average_acceleration(initial_velocity, final_velocity, initial_time, final_time):
    return ((final_velocity - initial_velocity)/(final_time - initial_time))

# Here we define (def) a function called Ch2_Section_2_4() which comprises an interactive acceleration program requiring user input
def Ch2_Section_2_4():
    print("Welcome back to Interative AP\u00AE Physics in Python by Dr. Scott Rowan!")
    print("\nChapter 2: Kinematics, Section 2.4: Acceleration")

    input("\nPlease press [Enter] to continue or [Ctrl + C] to exit...")

    print("\nThe [equation] for the average acceleration of a given object is defined as: ")
    print("\n\u0101 = (v_f - v_0)  /  (t_f - t_0)\n")
    print("\u0101 is the object's [average acceleration].")
    print("v_f is the object's [final/ending] velocity.")
    print("v_0 is the object's [initial/starting] velocity.")
    print("t_f is the object's [final/ending] time.")
    print("t_0 is the object's [initial/starting] time.")

    # The below 2-D graph / coord system is needlessly complicated, plotting with print functions alone would be a nightmare.
    # It is for this reason we use plot features which are part of the extended Python language, such as matplotlib (more in the future)

    print("\nAlthough this is only a one-dimensional example, the direction may be provided, e.g., 'West'.")
    print("As such, we can depicted a global coordinate system as follows:")
    print("                                    [North]")
    print("                             [positive y-direction]")
    print("                                      +y")
    print("                                       ^")
    print("                                       |")
    print("                                       |")
    print("[West][negative x-direction] -x <----- 0 -----> +x [positive x-direction][East]")
    print("                                       |")
    print("                                       |")
    print("                                       \u02C7")
    print("                                      -y")
    print("                             [negative y-direction]")
    print("                                     [South]")

    print("Note how we assign North, East, South & West to correspond with the x and y-axes.")
    print("For example, if an object is travelling due West, it will have negative velocity.")

    input("\nPlease press [Enter] to continue or [Ctrl + C] to exit...")

    # The following code asks the user (you!) for an initial and final position and stores them in variables 'initial_position' and 'final_position', respectively.
    # - The input() function reads whatever input is provided by the user
    # - The float() wrapper ensures the value is stored as a floating-point number rather than a string (text).
    # - Each captured input is wrapped in a try-catch exception-handling while loop to ensure only valid numbers are accepted
    while True:
        try:
            initial_velocity = float(input("\nPlease enter the object's [initial] velocity 'v_0' (in meters/seconds): "))
            break
        except ValueError:
            print("Invalid number, please try again...")
    while True:
        try:
            final_velocity = float(input("Thank you, please enter the object's [final] velocity 'v_f' (in meters/seconds): "))
            break
        except ValueError:
            print("Invalid number, please try again...")
    while True:
        try:
            initial_time = float(input("\nPlease enter the object's [initial] time 't_0' (in seconds): "))
            break
        except ValueError:
            print("Invalid number, please try again...")
    while True:
        try:
            final_time = float(input("Thank you, please enter the object's [final] time 't_f' (in seconds): "))
            assert final_time - initial_time >= 0
            break
        except ValueError:
            print("Invalid number, please try again...")
        except AssertionError:
            print("Error: Final time cannot be before initial time (or the Universe would break!), please try again...")

    input("\nTry and calculate the result yourself! Press [Enter] when you are ready to continue...")

    # Here we call the calculate_average_acceleration() function to calculate the average acceleration based on the acquired inputs
    average_acceleration = calculate_average_acceleration(initial_velocity, final_velocity, initial_time, final_time)

    # The following outputs a message and the calculated average acceleratio. 
    # - If the calculated displacement is positive, a '+' symbol is included in the output to show directionality. 
    # - Negative values have a '-' symbol by default. sep="" simply removes any default automatic spaces. 
    # - If the displacement is exactly 0, the object has either not moved of, after moving, eventually return to it's initial position.
    # - It is good coding practice, when using if elif statements, to include an else for error handling

    print("\n--------------------------------------------------------------")
    print("Answer/Solution:")

    if average_acceleration > 0:
        print("\nFor the given inputs, the calculated average acceleration is: +", average_acceleration, " m/s^2.", sep="")
        print("\nThis means that the object has on average accelerated ", average_acceleration, " meters/seconds^2 in the [positive] direction, i.e., due East. ", sep="")
        if final_velocity - initial_velocity > 0:
            print("Note that the object is still travelling West, though! It is just slowing down (decelerating).")
    elif average_acceleration < 0:
        print("\nFor the given inputs, the calculated average acceleration is: ", average_acceleration, " m/s^2.", sep="")
        print("\nThis means that the object has on average accelerated ", abs(average_acceleration), " meters/seconds^2 in the [negative] direction, i.e., due West. ", sep="")
        if final_velocity - initial_velocity < 0:
            print("Note that the object is still travelling East, though! It is just slowing down (decelerating).")    
    elif average_acceleration == 0:
        print("\nFor the given inputs, the calculated average acceleration is: ", average_acceleration, " m/s^2.", sep="")
        print("\nThis means that the object has on average remained at [constant velocity]. ")
    else:
        print("\nError: You have somehow ended up with an impossible value!")

    if average_acceleration != round(average_acceleration, 15):
        print("\nInteresting! You have run into a limitation of floating-point numbers and the calculated value is not quite right!")
        print("Due to this limitation, you may get only close to the exact number, e.g., 0.30000000000000004 instead of 0.3 etc")
        print("Don't worry, you're not wrong, the computer is!")

    print("--------------------------------------------------------------")

    print("Acceleration advanced.py has successfully completed.")


if __name__ == '__main__':
    try:
        Ch2_Section_2_4()
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        input("\nPlease press [Enter] to exit.")
