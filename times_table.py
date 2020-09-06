import check
import math

def num_list(n):
    '''
    returns a list of numbers from 0 to n
    
    num_list: Nat -> (Listof Nat)
    '''
    return list(range(n + 1))

def mul_list(l, el, n):
    '''
    returns a list which is a mutated version of list l where each element is
    multiplied by number n.
    
    mul_list: (listof Nat) (Listof Nat) Nat -> (listof Nat)
    '''
    if l == []:
        return el
    else :
        return mul_list(l[1:], el + [(n * l[0])], n)
    
def table_list(l, n, sl):
    '''
    returns a list in which all the elements are lists containg natural number.
    
    table_list: (listof Nat) Nat (Listof Nat) -> (Listof (listof Nat))
    '''
    if n == 0:
        sl = [(mul_list(l, [], 0))] + sl
        return sl
    else :
        sl = [(mul_list(l, [], n))] + sl
        return table_list(l, n-1, sl)
    
def times_table(n):
    '''
    returns a times table for all numbers betweeen 0 and n inclusive. A times
    table T is  a  list  of  lists,  of  size (n+1)x(n+1), such that for any 
    numbers x and y, each of which is between 0 and n,T[x][y] == x*y.
    
    times_table: Nat -> (listof (Listof Nat) 
    '''
    return table_list(num_list(n), n, [])

#Examples
check.expect("ex1", times_table (0), [[0]])

check.expect("ex2", times_table (3), [[0, 0, 0, 0],
                                      [0, 1, 2, 3],
                                      [0, 2, 4, 6],
                                      [0, 3, 6, 9]])

check.expect("ex3", times_table (4), [[0, 0, 0, 0, 0],
                                      [0, 1, 2, 3, 4],
                                      [0, 2, 4, 6, 8],
                                      [0, 3, 6, 9, 12],
                                      [0, 4, 8, 12, 16]])


#tests: 

check.expect("Test1", times_table (2), [[0, 0, 0],
                                        [0, 1, 2],
                                        [0, 2, 4]])

check.expect("Test2", times_table (1), [[0, 0],
                                        [0, 1]])
