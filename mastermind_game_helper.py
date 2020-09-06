import check

def match(L1,L2):
    '''Returns the number of elements that occur
    in the same position in both given lists L1 and L2
    that are the consumed list of integers.
    
    match: (listof Int) (listof Int) -> (Anyof Nat 0)
    
    Examples:
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 2]
    L3 = [1, 2, 3, 4, 4, 5, 5]
    
    match(L1, L2) => 1
    
    match(L1, L3) => 4
    '''
    
    if L1==[]:
        return 0
    
    elif L2==[]:
        return 0
    
    elif L1[0]==L2[0]:
        return 1 + match(L1[1:],L2[1:])
    
    else:
        return match(L1[1:],L2[1:])
    
    

def remove_x(L,x):
    '''Returns the list of integers L after removing 
    all occurences of element or integer x from L.
    
    remove_x: (listof Int) Int -> (listof Int)
    
    Examples:
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 2]
    L3 = [1, 2, 3, 4, 4, 5, 5]
    
    remove_x(L3,4) => [1, 2, 3, 5, 5]
    
    remove_x(L1,6) => [1, 2, 3, 4, 5]
    
    remove_x(L2,2) => [4]
    '''
    
    return list(filter(lambda a: a!=x , L))



def intersection_size(L1,L2):
    '''Returns the number of common elements
    between the given list of integers L1 and L2
    If an element occurs n times in L1 and
    m times in L2, the minimum of m and n elements
    are shared.
    
    intersection_size: (listof Int) (listof Int) -> (Anyof Nat 0)
    
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 2]
    L3 = [1, 2, 3, 4, 4, 5, 5]
    
    intersection_size(L1, L2) => 2
    
    intersection_size(L1, L3) => 5
    '''
   
    if L1==[]:
        return 0
    
    elif L2==[]:
        return 0
    
    elif L1[0] in L2:
        return min(L1.count(L1[0]),L2.count(L1[0])) + \
               intersection_size(remove_x(L1[1:],L1[0]),L2)
    
    else:
        return intersection_size(L1[1:],L2)
    


def make_list(s):
    '''Returns a list of integers after consuming a string.
    It removes all the spaces and takes out the integers and 
    converts them into a list.
    
    make_list: Str -> (listof Int)
    
    Examples:
    make_list(' 1 2 3 4') => [1, 2, 3, 4]
    
    make_list(' 6 2 3 5') => [6, 2, 3, 5]
    '''
    
    if len(s)==0:
        return []
    
    elif s[0]==' ':
        return make_list(s[1:])
    
    else:
        return [int(s[0])] + make_list(s[1:])



def mastermind_helper(secret,turns,guess): 
    '''Returns the number of guesses the guesser takes 
    to determine the sequence. If secret is not guessed
    in turns guesses, the function returns None
    and follows all the rules and assumptions of
    the function mastermind given below.
    
    mastermind_helper: (listof Int) Nat Nat->(Anyof None Nat)
    
    '''
    
    if (turns==0):
        print('Sequence of',secret,'not found. Game over.')
        return None
    
    else:
        
        x=input("Enter your guess: ")
        
        k=make_list(x)   
        
        if (k==secret):
            print('Sequence found in',guess - turns + 1,'guesses.')
            return guess - turns + 1
        
        else:
            print('There are',match(k,secret),\
                  'numbers in correct places and',
                  intersection_size(secret,k)-match(k,secret),\
                  'numbers in incorrect places.')
        return mastermind_helper(secret,turns-1,guess) 
    
def mastermind(secret,turns):
    '''Returns the number of guesses the guesser takes 
    to determine the sequence. Given a list of integers 
    secret of size at least 2 and the maximum number 
    of turns the guesser has to determine secretIf secret 
    is not guessed in turns guesses, the function returns None.
    The file prompts the user to input a sequence of number to
    find out the number of elements in two lists that are in
    the same place, and determining the number of elements 
    in two lists that match but are in different locations.
    
    mastermind: (listof Int) Nat -> (Anyof None Nat)
    
    Requires:
    '''
    return mastermind_helper(secret,turns,turns)
              
#Example 1
check.set_input(' 1 2 3 4',' 6 2 3 5',' 1 1 6 4','1 6 1 4')
check.set_print_exact('There are 2 numbers in correct places and 0 numbers \
in incorrect places.','There are 0 numbers in correct places and 1 numbers \
in incorrect places.','There are 2 numbers in correct places and 2 numbers \
in incorrect places.','Sequence found in 4 guesses.')

check.expect('Example1',mastermind([1,6,1,4], 5),4)
