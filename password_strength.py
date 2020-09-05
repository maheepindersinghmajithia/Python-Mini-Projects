import check
import math

def password_length(s) :
    '''
    consumes a string s and returns 1 if length of s is greater than 9
    else it returns 0.
    
    password_length: Str -> Nat
    
    Examples:
    password_length("titile") -> 0
    password_length('haramkhoriyaan1234') -> 1
    '''
    if len(s) > 9:
        return 1
    else :
        return 0
##Tests
check.expect("length less than 9", password_length("titile"), 0)
check.expect("length more than 9", password_length('haramkhoriyaan1234'), 1)
    
def least_one_upper(s) :
    '''
    consumes a string s and returns 1 if the string has atleast 1 uppercase
    alphabet else returns 0
    
    least_one_upper: Str -> Nat
    
    Examples:
    least_one_upper("dumb") -> 0
    least_one_upper("DUmb") -> 1
    least_one_upper("duMb1") -> 1
    '''
    if s == "" :
        return 0
    elif s[0:1].isupper():
        return 1
    else :
        return 0 + least_one_upper(s[1:])
##Tests:
check.expect("one upper case", least_one_upper("duMb1"), 1)
check.expect("more than one upper case", least_one_upper("DUmb"), 1)
check.expect("no upper case", least_one_upper("dumb"), 0)

def least_one_lower(s) :
    '''
    consumes a string s and returns 1 if the string has atleast 1 lowercase
    alphabet else returns 0
    
    least_one_lower: Str -> Nat
    
    Examples:
    least_one_lower("DUMB") -> 0
    least_one_lower("DUmB") -> 1
    least_one_lower("Dumb1") -> 1
    '''

    if s == "" :
        return 0
    elif s[0:1].islower():
        return 1
    else :
        return 0 + least_one_lower(s[1:])
##Tests:
check.expect("no lower case", least_one_lower("DUMB"), 0)
check.expect("one lower case", least_one_lower("DUmB"), 1)
check.expect("more than one lower case", least_one_lower("Dumb1"), 1)
    
def total_non_alphas(s):
    '''
    consumes string s and gives the number of non alphanumeric characters in the
    string.
    
    total_non_alphas: Str -> Nat
    
    Examples:
    total_non_alphas("dumb1234") -> 0
    total_non_alphas('d#mb') -> 1
    total_non_alphas("Dum#%@") -> 3
    '''
    if s == "" :
        return 0
    elif not(s[0:1].isalnum()):
        return 1 + total_non_alphas(s[1:])
    else :
        return total_non_alphas(s[1:])
##Tests:
check.expect("zero nonalphanumerics", total_non_alphas("dumb1234"), 0)
check.expect("one alphanumeric", total_non_alphas('d#mb'), 1)
check.expect("more than one alphanumeric", total_non_alphas("Dum#%@"), 3)

def cond_on_non_alphas(n):
    '''
    consumes a non-negtaive integer value n and retuens 1 if n is greater than 2 
    else returns 0
    
    cond_on_non_alphas: Nat -> Nat
    
    Examples:
    cond_on_non_alphas(0) -> 0
    cond_on_non_alphas(3) -> 1
    '''
    if n > 2 :
        return 1
    else :
        return 0

##Tests:
check.expect("value more than 2", cond_on_non_alphas(3), 1)
check.expect("value less than 2", cond_on_non_alphas(0), 0)

    
def total_digits(s):
    '''
    consumes string s and gives the number of digits in the
    string.
    
    total_digits: Str -> Nat
    
    Examples:
    total_digits("jatt1234") -> 4
    total_digits("jatt") -> 0
    total_digits("") -> 0
    '''
    if s == "" :
        return 0
    elif  s[0:1].isnumeric() :
        return 1 + total_digits(s[1:])
    else :
        return total_digits(s[1:])

##Tests:
check.expect("more than one digit", total_digits("jatt1234"), 4)
check.expect("no digits", total_digits("jatt"), 0)
check.expect("empty string", total_digits(""), 0)
    
def cond_on_numerics(n):
    '''
    consimes a non-negative integer n and returns 1 if n is greater than 1 else
    returns 0
    
    cond_on_numerics: Nat -> Nat
    
    Examples:
    cond_on_numerics(1) -> 0
    cond_on_numerics(3) -> 1
    '''
    if n > 1 :
        return 1 
    else : 
        return 0

##Tests:
check.expect("value less than 1", cond_on_numerics(1), 0)
check.expect("value more than 1", cond_on_numerics(3), 1 )   
    
def spaces(s):
    '''
    consumes a string s and returns 0 if the string contains whitespaces else 
    returns 0
    
    spaces: Str -> Nat
    
    Examples:
    spaces("jaat hun") -> 0
    spaces("hello") -> 1
    '''
    if s == "" :
        return 1
    elif s[0:1].isspace():
        return 0
    else :
        return spaces(s[1:])
    
##Tests: 
check.expect("white space present", spaces("jaat hun"), 0)
check.expect("no white space present", spaces("hello"), 1)  

def what_password(s):
    '''
    consumes a string s and returns "good" if s is meeting all 6 password 
    conditions, returns "fair" if s is meeting 4 or 5 password conditions, 
    returns "weak" if s is meeting less than 4 password conditions.
    
    what_password: Str -> Str
    
    Examples:
    what_password("oodPass12!@@") -> "Good"
    what_password("fairPass !!!") -> "Fair"
    what_password("weak12!") -> "weak"
    '''
    
    if password_length(s) + least_one_upper(s) + least_one_lower(s) + \
       cond_on_non_alphas(total_non_alphas(s)) + \
       cond_on_numerics(total_digits(s)) + spaces(s) == 6 : 
        return "Good"
    elif password_length(s) + least_one_upper(s) + least_one_lower(s) + \
         cond_on_non_alphas(total_non_alphas(s)) + \
         cond_on_numerics(total_digits(s)) + spaces(s) == 5 :
        return "Fair"
    elif password_length(s) + least_one_upper(s) + least_one_lower(s) + \
         cond_on_non_alphas(total_non_alphas(s)) + \
         cond_on_numerics(total_digits(s)) + spaces(s) == 4 :
        return "Fair"
    elif password_length(s) + least_one_upper(s) + least_one_lower(s) + \
         cond_on_non_alphas(total_non_alphas(s)) + \
         cond_on_numerics(total_digits(s)) + spaces(s) < 4 :
        return "Weak"
    
##Tests:    
check.expect("Good password", what_password("oodPass12!@@"), "Good")
check.expect("Fair password", what_password("fairPass !!!"), "Fair")
check.expect("Weak password", what_password("weak12!"), "Weak")
    

        


def new_password():
    '''
    that consumes no values, but prompts the user with the phrase 
    "Enter password:" The  function  returnsNoneand  prints  the  strength 
    of your password. prints  the  strength  of  your  password. If the password
    contains all the critia given, then it prints Good. If password contains 4 
    or 5 criteria then function prints Fair. Otherwise, the function  prints
    Weak.
    
    Effect: Reads input form keyboard
            Prints to Screen
    
    new_password: None -> None
    
    Examples:
    
    Enter  password: goodPass12!@@
    Good
    
    Enter  password: fairPass !!!
    Fair
    
    Enter  password: weak12!
    Weak
    '''
    
    
password = input("Enter password:")
print(what_password(password))

check.set_input("oodPass12!@@")
check.set_print_exact("Good")
check.expect("Test1", new_password(), None)
