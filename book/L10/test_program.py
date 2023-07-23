#The main block is only run when the file is run *directly*
#by python. When the file is imported, the main block is not run
#
#One use of this is to put the testing code in the main block, so that
#when you're importing the file (like you would import math)
#you can use the functions, but don't see the output of the testing
#
#An important consequence of this is that you must always initialize
#all global variables *outside* of the main block.


if __name__ == '__main__':
    import program
    program.print_b()
    print(program.a)
    print(program.b)
