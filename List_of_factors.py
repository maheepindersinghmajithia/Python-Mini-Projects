import check
import math

def helper_1(n, i):
    if n % i == 0 :
        return [i]
    else :
        return []
    
def helper_2(n, i):
    my_list = []
    for i in range(1,n+1):
        my_list = my_list + helper_1(n,i)
    return my_list

def factors(n):
    return helper_2(n,1)

check.expect("Ex1",factors (3), [1, 3])
check.expect('Ex',factors(12), [1, 2, 3, 4, 6, 12])




def helper_4(s):
    my_string = ""
    third_char=s[2]
    for i in s:
        if i== third_char:
            my_string=my_string+'#'
        else:
            my_string=my_string+i
    return my_string[0:2] + s[2] + my_string[3:]
    
def new_word(s) :
    if len(s) < 3 :
        return s
    else :
        return helper_4(s)
check.expect("ex3", new_word("bubble"), "#ub#le")
check.expect('ex4',new_word("me"), "me")
        
