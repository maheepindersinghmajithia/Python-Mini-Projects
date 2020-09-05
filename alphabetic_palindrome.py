import check
import math

def just_alph(s):
    ''' 
    consumes a string s and returns a string which contains only alphabets 
    of the original string in the same order of the entered string.
     
    just_alph: Str -> Str    
    '''
    x = ""
    if s == "":
        return x
    elif s[0:1].isalpha():
        return x + s[0:1] + just_alph(s[1:])
    else:
        return x + just_alph(s[1:])
    
#Tests                        
check.expect('Example1',just_alph('89mB*'),'mB')
check.expect("Example2", just_alph(" "), "")
check.expect("Example3", just_alph(""), "")

def reversed_string(s):
    '''
    consumes a string and returns a String whose characters are in reverse order
    
    reversed_string: Str -> Str
    '''
    x = ""
    if s == "":
        return x
    else :
        x = reversed_string(s[1:]) + s[0:1]
        return x

#Tests
check.expect("rev1", reversed_string(""), "")
check.expect("rev2", reversed_string("Mb3"), "3bM")

def alphabetic_palindrome(phrase):
    '''
    that consumes a string phrase and returns True if it is an alphabetic 
    palindrome and False otherwise.
    
    alphabetic_palindrome: Str -> Bool
    
    Examples: 
    alphabetic_palindrome("moM") -> True
    alphabetic_palindrome("computers") -> False
    alphabetic_palindrome("rAce .car 12") -> True
    '''
    if just_alph(phrase.upper()) == reversed_string(just_alph(phrase.upper())):
        return True
    else:
        return False
    
##Examples:
check.expect("1", alphabetic_palindrome("moM"), True)
check.expect("2", alphabetic_palindrome("computers"), False)
check.expect("3", alphabetic_palindrome("rAce .car 12"), True)

##Tests:
check.expect("4", alphabetic_palindrome("jat o taj"), True)
check.expect("5", alphabetic_palindrome("not3?"), False)
