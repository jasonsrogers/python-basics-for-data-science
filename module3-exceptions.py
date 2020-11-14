# potential code before try catch

try:
    # code to try to execute
    pass
except ZeroDivisionError:
    pass
    # code to execute if there is a ZeroDivisionError
except NameError:
    pass
    # code to execute if there is a NameError
except:
    pass
    # code to execute if ther is any exception
else:
    pass
    # code to execute if there is no exception
finally:
    pass
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling



a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")




