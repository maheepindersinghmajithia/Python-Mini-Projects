def acc_scrabble(s, acc):
    '''
    Returns the score of the word s in scrabble and 
    the acc by consuming a string s and positive 
    integer acc. It returns 0 if the string s has 
    any non-alphabetical characters and prints a message 
    "Invalid character!"to the screen.
    
    If s.isalpha() == False
    Effects:
    Prints "Invalid character!" to the screen
    
    acc_scrabble: Str Int -> (Anyof Nat 0)
    
    Requires:
    acc >= 0
    
    Examples:
    acc_scrabble("Hello") => 8
    acc_scrabble("Hello!") => 0, and prints "Invalid character!"
    
    '''
    if s == "":
        return acc
    elif not(s.isalpha()):
        return 0   
    elif (s[0:1] == "a") or (s[0:1] == "e") or (s[0:1] == "i") or \
         (s[0:1] == "l") or (s[0:1] == "n") or (s[0:1] == "o") or (s[0:1] == "r") or (s[0:1] == "s") or \
         (s[0:1] == "t") or (s[0:1] == "u") or (s[0:1] == "T") or (s[0:1] == "U") or \
         (s[0:1] == "A") or (s[0:1] == "E") or (s[0:1] == "I") or (s[0:1] == "L") or \
         (s[0:1] == "N") or (s[0:1] == "O") or (s[0:1] == "R") or (s[0:1] == "S") :
        return acc_scrabble(s[1:], acc + 1)
    elif (s[0:1] == "b") or (s[0:1] == "c") or (s[0:1] == "d") or (s[0:1] == "g") or \
         (s[0:1] == "m") or (s[0:1] == "p") or (s[0:1] == "B") or (s[0:1] == "C") or \
         (s[0:1] == "D") or (s[0:1] == "G") or (s[0:1] == "M") or (s[0:1] == "P") :
        return acc_scrabble(s[1:], acc + 2)
    elif (s[0:1] == "F") or (s[0:1] == "H") or (s[0:1] == "K") or (s[0:1] == "V") or \
         (s[0:1] == "W") or (s[0:1] == "Y") or (s[0:1] == "f") or (s[0:1] == "h") or \
         (s[0:1] == "k") or (s[0:1] == "v") or (s[0:1] == "w") or (s[0:1] == "y") :
        return acc_scrabble(s[1:], acc + 4)    
    elif (s[0:1] == "j") or (s[0:1] == "q") or (s[0:1] == "x") or (s[0:1] == "z") or \
         (s[0:1] == "J") or (s[0:1] == "Q") or (s[0:1] == "X") or (s[0:1] == "Z") :
        return acc_scrabble(s[1:], acc + 8)    
    
def scrabble_score(s):
    '''Returns the score in of creating a word in
    Scrabble by consuming string s, or returns 0 if
    s has any non-alphabetical character and prints 
    message "Invalid character!" to the screen.
    
    Every letter is given value, and the total score 
    is the sum of the indiviadual prints for each letter
    The point values for each letter are as follows:
    # 1point: A,E,I,L,N,O,R,S,T,U 
    # 2points: B,C,D,G,M,P
    # 4points: F,H,K,V,W,Y
    # 8points: J,Q,X,Z
    
    Letters are accepted in both uppercase and lowercase.
    
    Effects: 
    Prints "Invalid character!" to the screen if
    s.isalpha() == False
    
    scrabble_score: Str -> (Anyof 0 Nat)
    
    Examples:
    scrabble_score("Hello") => 8
    
    scrabble_score("Hello!") => 0, 
    and prints "Invalid character!"
    
    scrabble_score("zyZZyx") => 40
    
    scrabble_score("I like Zyzzyx") => 0, 
    and prints "Invalid character!"
    '''    
    if not(s.isalpha()):
        print("Invalid character!")  
        return 0
    else:
        return acc_scrabble(s, 0)

#Examples:
check.expect('example1',scrabble_score("Hello"),8)
    
check.set_print_exact("Invalid character!")
check.expect('example2',scrabble_score("Hello!"),0)
    
check.expect('example3',scrabble_score("zyZZyx"),40)
    
check.set_print_exact("Invalid character!")
check.expect('example4',scrabble_score("I like Zyzzyx"),0)

#Tests:
check.expect('Test1',scrabble_score(""),0)

check.set_print_exact("Invalid character!")
check.expect('Test2',scrabble_score("jatt jeona mod"),0)

check.expect('Test1',scrabble_score("Adi"), 4)
