# CSE 101 - IP HW4
# Transformation in Graphs
# Name: Navya Aggarwal
# Roll Number: 2018349
# Section: B
# Group: 6
# Date: 20 November 2018

if __name__=="__main__":
    typ = input()
    if (typ=="disc"):
        from disc import main_func
        main_func()
    elif (typ=="polygon"):
        from polygon import main_func
        main_func()
    else:
        print("Invalid Input")
