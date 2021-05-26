def Welcome():
    print("Checking Python install... ")
    print("Success! Python is correctly installed.")
    name = input("\nPlease enter your name: ")

    print("\nHello ", name, "! Welcome to Interactive AP\u00AE Physics in Python by former CERN engineer Dr. Scott Rowan.", sep="")
    print("\nResume:", sep="")
    print("- M.Eng. in Electronics and Electrical Engineering at the University of Glasgow, Scotland, UK.", sep="")
    print("- Ph.D. in Accelerator Physics at CERN, Geneva, Switzerland.", sep="")
    print("- 8 years' experience working as part of the Large Hadron Collider project.", sep="")
    print("- 10 years' software development experience.", sep="")
    print("- Dedicated to bringing industry-quality programming practices to physics research.", sep="")

if __name__ == '__main__':
    try:
        Welcome()
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        input("\nPlease press [Enter] to exit.")
