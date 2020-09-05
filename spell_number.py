import check
import math

def add_zeros(s,n):
    if  n == 0:
        return s
    else :
        return add_zeros("0" + s, n-1)

def number_to_string(n):
    return str(n)

def three_size_number(n, group_names):
    if n == 0:
        return number_to_string(n)
    elif len(number_to_string(n)) < 3 * len(group_names):
        return  add_zeros(number_to_string(n), len(group_names) - \
                          len(number_to_string(n)))

def three_num_list(s, L):
    if len(s) == 0:
        return L
    else:
        three_num_list(s[3:], L + [s[0:3]])
        
def digit_name(sn):
    if sn == "1" :
        return " one "
    elif sn == "2" :
        return " two "
    elif sn == "3" :
        return " three "
    elif sn == "4" :
        return " four "
    elif sn == "5" :
        return " five "
    elif sn == "6" :
        return " six "
    elif sn == "7" :
        return " seven "
    elif sn == "8" :
        return " eight "
    elif sn == "9" :
        return " nine "

def teen_spelling(tn):
    if tn == "10" :
        return " ten "
    elif tn == "11" :
        return " eleven "
    elif tn == "12" :
        return " twelve "
    elif tn == "13" :
        return " thirteen "
    elif tn == "14" :
        return " fourteen "
    elif tn == "15" :
        return " fifteen "
    elif tn == "16" :
        return " sixteen "
    elif tn == "17" :
        return " seventeen "
    elif tn == "18" :
        return " eighteen "
    elif tn == "19" :
        return " nineteen "
    
def second_digit(dn):  
    if dn == "2" :
        return " twenty "
    elif dn == "3" :
        return " thirty "
    elif dn == "4" :
        return " forty "
    elif dn == "5" :
        return " fifty "
    elif dn == "6" :
        return " sixty "
    elif dn == "7" :
        return " seventy "
    elif dn == "8" :
        return " eighty "
    elif dn == "9" :
        return " ninety "
    
def english_number(sm, S):
    if len(sm) == 3 and not(sm[0:1] == 0):
        return english_number(sm[1:], digit_name(S + sm[0:1]) + " hundred " )
    elif len(sm) == 3 and sm[0:1] == 0 :
        return english_number(sm[1:], S)
    elif len(sm) == 2 and s[0:1] == 1 :
        return S + teen_spelling(sm)
    elif len(sm) == 2 and not (s[0:1] == 1) and s[0:1] == 0 :
        return english_number(sm[1:], S)
    elif len(sm) == 2 and not(s[0:1] == 1) and not( s[0:1] == 0):
        return english_number(sm[1:], S + second_digit(sm[0:1]))
    elif len(sm) == 1 and sm == 0 :
        return S
    elif len(sm) == 1 and not( sm == 0 ):
        return S + digit_name(sm)
    
def three_word_list(L, W):
    if L == []:
        return W
    else :
        return three_word_list(L[1:], W + [english_number(L[0], "")])
    
def append_final_number(W, group_names, Z):
    if len(group_names) == 0:
        return Z
    elif W[0]=='':
        return append_final_number(W[1:], group_names[1:], Z)
    else:
        return append_final_number(W[1:], group_names[1:], Z + \
                                   [W[0] + group_names[0]])
    
def spell_number(n,group_names):
    if n == 0 :
        return "zero"
    else:
        return append_final_number(three_word_list(three_num_list \
                    (three_size_number(n,group_names),[]),[]),group_names,[])

check.expect("ex1", spell_number (0, [""]), "zero")

check.expect("ex2", spell_number (42, [""]), "forty  two")

check.expect("ex3", spell_number (900, [""]), "nine  hundred")

check.expect("ex4", spell_number (42713 , ["thousand", ""]), "forty  two \
thousand  seven  hundred  thirteen")

check.expect("ex5", spell_number (4000000 , ["million", "thousand", "units"]), \
             "four  million")

check.expect("ex5", spell_number (8000010 , ["million", "thousand", ""]), \
             "eight  million  ten")

check.expect("ex6", spell_number (123456789 , ["billion", "million", \
 "thousand", ""]), "one hundred  twenty  three  million  four  hundred  fifty \
 six thous and seven  hundred  eighty  nine")

check.expect("ex7", spell_number (5555, ["flibberty", "floppity"]), "five \
flibberty  five  hundred  fifty  five  floppity")

