"""In python, we can pass a variable number of items"""

"""Note that we use these arguments when we have no doubt about the number of arguments we should pass in the 
function """

# there exist two special symbols
# the *args as the non-keyword arguments
# the **kwargs as the keyword arguments


def my_function(*args):
    print(args[0])
    print(args[1])
    print(args)


def the_arguments():
    my_function(0, 1)


"""these automatically become objects in this particular module"""
if "__name__" == "__main__":
    the_arguments()
