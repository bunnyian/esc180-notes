def print_b():
    print(b)



def initialize():
    global a, b
    a = 0
    b = 0


#if you have global variables, you must
#initialize them outside the main block
initialize()

if __name__ == '__main__':
    c = 0       #If you import program elsewhere, 
                #you will not be able to access
                #program.c because the main block
                #will not be executed!
    print(a)
    print(b)
