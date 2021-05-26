# Copyright (c) 2021, srowanphys
# All rights reserved.

# This source code is licensed under the Apache 2.0 license found in the
# LICENSE.md file in the root directory of this source tree.

# The following code constructs an interactive program for calculating displacement
# The program is written in the Python language
# All lines starting with a '#' symbol are so-called 'comments' and are not part of the program, but rather just helpful notes for the reader
# Most of the program consists of simple functions:
# - 'print()' to output a given message and/or result
# - 'input()' to prompt an input from the user (you!), e.g. entering a value for a variable

# Here we define (def) a function called calculate_displacement()
# - The calculation follows the equation in a readable format: displacement (dx) = final_position (x_f) - initial_position (x_0)
def calculate_displacement(initial_position, final_position):
    return final_position - initial_position

# Here we define (def) a function called Ch2_Section_2_1() which comprises an interactive displacement program requiring user input
def Ch2_Section_2_1():
    print("Welcome back to Interative AP\u00AE Physics in Python by Dr. Scott Rowan!")
    print("\nChapter 2: Kinematics, Section 2.1: Displacement")

    input("\nPlease press [Enter] to continue or [Ctrl + C] to exit...")

    print("\nThe [equation] for the displacement of a given object is defined as: ")
    print("\n\u0394x = x_f - x_0\n")
    print("\u0394x is the object's [change/difference] in position, i.e., displacement.")
    print("x_f is the object's [final/ending] position.")
    print("x_0 is the object's [initial/starting]s position.")

    print("\nThis is a one-dimensional displacement example and the axis of movement can simply be depicted as follows:")
    print("\n[negative direction] -x <------------------------ x_0 ------------------------> +x [positive direction]")

    input("\nPlease press [Enter] to continue or [Ctrl + C] to exit...")

    # The following code asks the user (you!) for an initial and final position and stores them in variables 'initial_position' and 'final_position', respectively.
    # - The input() function reads whatever input is provided by the user
    # - The float() wrapper ensures the value is stored as a floating-point number rather than a string (text).
    # - Each captured input is wrapped in a try-catch exception-handling while loop to ensure only valid numbers are accepted
    while True:
        try:
            initial_position = float(input("\nPlease enter the object's [initial] position 'x_0' (in meters): "))
            break
        except ValueError:
            print("Invalid number, please try again...")
    while True:
        try:
            final_position = float(input("Thank you, please enter the object's [final] position 'x_f' (in meters): "))
            break
        except ValueError:
            print("Invalid number, please try again...")

    input("\nTry and calculate the result yourself! Press [Enter] when you are ready to continue...")

    # Here we call the calculate_displacement() function to calculate the displacement based on the acquired inputs
    displacement = calculate_displacement(initial_position, final_position)

    # The following outputs a message and the calculated displacement. 
    # - If the calculated displacement is positive, a '+' symbol is included in the output to show directionality. 
    # - Negative values have a '-' symbol by default. sep="" simply removes any default automatic spaces. 
    # - If the displacement is exactly 0, the object has either not moved of, after moving, eventually return to it's initial position.
    # - It is good coding practice, when using if elif statements, to include an else for error handling

    print("\n--------------------------------------------------------------")
    print("Answer/Solution:")

    if displacement > 0:
        print("\nFor the given inputs, the calculated object displacement is: +", displacement, " m.", sep="")
        print("\nThis means that the object has moved ", displacement, " meters relative to its initial position in the [positive] direction. ", sep="")
    elif displacement < 0:
        print("\nFor the given inputs, the calculated object displacement is: ", displacement, " m.", sep="")
        print("\nThis means that the object has moved ", abs(displacement), " meters relative to its initial position in the [negative] direction. ", sep="")
    elif displacement == 0:
        print("\nFor the given inputs, the calculated object displacement is: ", displacement, " m.", sep="")
        print("\nThis means that the object has either [not moved] or eventually [returned] to it's starting location. ")
    else:
        print("\nError: You have somehow ended up with an impossible value!")

    print("--------------------------------------------------------------")

    print("\nDisplacement.py has successfully completed.")


if __name__ == '__main__':
    try:
        Ch2_Section_2_1()
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        input("\nPlease press [Enter] to exit.")
