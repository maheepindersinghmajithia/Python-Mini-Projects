import check
import math

def next_row(l):
    '''
    returns the next row of the bernoulli's triangle when a previous row of the
    triangle gets consumed. It gives the first row of the bernoulli's triangle
    when an empty row is fed. rows are in the form of a list.
    
    next_row: (Listof Nat) -> (listof Nat)
    EXamples:
    next_rows([1,3,4]) -> [1,4,7,8]
    next_rows([]) -> [1]
    '''
    i = []
    while len(i) < len(l) + 1:
        if i == []:
            i = i + [1]
        elif len(i) == len(l):
            i = i + [2*l[-1]]
        else:
            i = i + [l[len(i)] + l[len(i) - 1]]            
    return i
            
def bernoulli_triangle(n):
    '''
    that consumes a positive integernand returns a list of length n, where the 
    first element is a list representing the first row of Bernoulli's Triangle,
    the second element is a list representing the second row of Bernoulli's
    Triangle, etc.
    
    bernoulli_triangle: Nat -> (Listof(listof Nat))
    
    Example:
    bernoulli_triangle (1) => [[1]]
    bernoulli_triangle (4)=> [[1], [1, 2], [1, 3, 4], [1, 4, 7, 8]]
    '''
    lol = []
    while n > 0 :
        if lol == []:
            lol = lol + [next_row([])]
            n=n-1
        else :
            lol = lol + [next_row(lol[-1])]
            n=n-1
    return lol

#example     
check.expect('EX1', bernoulli_triangle(1), [[1]])
check.expect('EX2', bernoulli_triangle(4),  [[1], [1, 2], [1, 3, 4], \
                                             [1, 4, 7, 8]])        
#tests
check.expect('test1', bernoulli_triangle(2), [[1], [1, 2]])
check.expect('test2', bernoulli_triangle(3),  [[1], [1, 2], [1, 3, 4]])   
