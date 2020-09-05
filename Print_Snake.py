import check
import math

def snake():
    '''
    returns None and consumes nothing prints a picture of a beautiful picture 
    of a snake to the screen. It reads input from the user by displaying
    corrosponding messages to height, length, and frame of the snake.
    If the input is not integer for height or length , it prints "invalid
    character to the screen. similarly if the input length for the frame is
    not equal to 1 , it agains prints "invalid character" and again asks user 
    to enter the frame. when the user has finally inputed all the valid inputs 
    a snake it printed.
    
    effects:
    prompts to the screen and takes user input from keyboard that 3 things 
    'Enter height:','Enter length:', "Enter frame:".If the user enters a wrong 
    value 'Invalid input' is printed and user gets prompted with the same
    message again until the corrected is entered.
    
    After the correct value is entered a snake gets printed to the screen.
    
    snake: None -> None
    
    Examples:
    Enter height: 1
    Enter length: 0
    Enter frame: #
    #########
    #   --:~#
    #  /    #
    #--     #
    #########
    Sample 2:
    Enter height: a
    Invalid input.
    Enter height: 0
    Invalid input.
    Enter height: 3
    Enter length: 1
    Enter frame: $$
    Invalid input.
    Enter frame: hello
    Invalid input.
    Enter frame: *
    *********************
    *     --        --:~*
    *    /  \      /    *
    *   /    \    /     *
    *  /      \  /      *
    *--        --       *
    *********************
    
    '''
    x = input("Enter height: ")
    while x.isdigit() == False or int(x) < 1:
        print('Invalid input.')
        x = input('Enter height: ')
    x = int(x)
    
    y = input("Enter length: ")
    while y.isdigit() == False or int(y) < 0:
        print('Invalid input.')
        y= input('Enter length: ')
    y = int(y)    
    
    z = input("Enter frame:")
    while not(len(z) == 1):
        print('Invalid input.')
        z= input('Enter frame: ')
    
    print((8 + x + 2 * y * ( x + 2 )) * z)
    print(z + (2 + x)*" " + "--" + y*((2*x + 2)*' '+'--') + ":~" + z)
    i = 0
    while i < x :
        print(z + (1 + x - i) *" " + "/" + y*((2 + 2*i)*" " + "\\" + \
                        (2* (x - i ))*" " + "/") + ((4 + i) * " ") + z)
        i = i + 1
    print(z + "--" + y*((2 * x + 2) * " " + "--") + (4 + x) * " " + z)
    print((8 + x + 2 * y * ( x + 2 )) * z)

#examples
check.set_input('a','1','0','#')
check.set_screen('Invalid input.\n#########\n\
#   --:~#\n#  /    #\n#--     #\n#########')
check.expect("ex1", snake(), None)


check.set_input('a','0','3', '1', '$$', "hello", "*")
check.set_screen('Invalid input.\nInvalid input.\nInvalid input.\n\
Invalid input.\n*********************\n*     --        --:~*\n\
*    /  \      /    *\n*   /    \    /     *\n*  /      \  /      *\n\
*--        --       *\n*********************')
check.expect("ex2", snake(), None)

#tests

check.set_input('1','0','#')
check.set_screen('#########\n#   --:~#\n#  /    #\n#--     #\n#########')
check.expect("Test1", snake(), None)

check.set_input('3', '1', "*")
check.set_screen('*********************\n\
*     --        --:~*\n\
*    /  \      /    *\n\
*   /    \    /     *\n\
*  /      \  /      *\n\
*--        --       *\n\
*********************')
check.expect("Test2", snake(), None)
