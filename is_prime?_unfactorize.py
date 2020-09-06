import check
import math

def is_prime(p, d):
    '''
    Returns True if and only if p has no divisors from 2 to d and false 
    otherwise.
    
    is_prime: Nat Nat -> Bool
    '''
    if d == 0:
        return False
    if d == 1:
        return True
    if p % d == 0 :
        return False
    return is_prime(p, d-1)

def number_prime(i):
    '''
    returns i in a list if i is prime otherwise returns an empty list.
    
    number_prime: Nat -> (Listof Nat)
    '''
    if is_prime(i, i-1):
        return [i]
    else :
        return []
    

def prime_number_length_list(i, L, L0):
    '''
    returns a list of prime numbers, which has same number of prime numbers 
    as the number of elements in  List L0.
    
    prime_number_length_list: Nat (Listof Nat) (Listof Nat) -> (Listof Nat)
    '''
    if len(L0) == 0:
        return [] 
    elif len(L0) == len(L) :
        return L
    elif len(L) < len(L0) :
        return prime_number_length_list(i+1 ,L + number_prime(i), L0)
    
def final_product(L0, L, n):
    '''
    returns the final value of n which is calculated by raising the value of 
    each element in L to each corrosponding element in L0 and then multiplying 
    all of them together.
    
    final_product: (listof Nat) (Listof Nat) Nat -> Nat
    
    '''
    if L == [] :
        return n
    else :
        return final_product(L0[1:], L[1:], n * (L[0] ** L0[0]))
    
def unfactorize(factors):
    '''
    returns a natural number, where factors describes the prime factors of 
    the result. The value for each index i of factors is the number of factors 
    of the i'th prime  number  in  the  result.
    
    unfactorize : (Listof Nat) -> Nat
    '''
    return final_product(factors, prime_number_length_list(2, [], factors), 1)

#Examples
check.expect("ex1", unfactorize ([2, 0, 1]), 20)

check.expect("ex2", unfactorize ([2, 1]), 12)

check.expect("ex3", unfactorize ([0, 1, 2, 0, 0, 0, 0, 0, 1]), 1725)


#tests


check.expect("Test1", unfactorize ([]), 1)

check.expect("Test2", unfactorize ([1, 1, 0, 0]), 6)
