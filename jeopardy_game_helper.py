import check
import math


def final_jeopardy(c1, c2, c3):
    '''
    returns  the  amount  that  the  leader  should  bet  in order to guarantee
    victory if they get the question correct.
    
    final_jeopardy: Nat Nat Nat -> Nat
    
    Examples:
    final_jeopardy (5000, 7500,  10000) => 5001
    final_jeopardy (15000 ,  15000,  800) => 15000
    '''
    sechigh = c1 + c2 + c3 - min([ c1, c2, c3]) - max([c1, c2, c3])
    
    if 2 * sechigh < max([c1, c2, c3]):
        return 0
    elif sechigh == max([c1, c2, c3]):
        return max([c1, c2, c3])
    elif 2 * sechigh > max([c1, c2, c3]):
        return  2 * sechigh - max([c1, c2, c3]) + 1

check.expect("Example 1", final_jeopardy (5000, 7500,  10000), 5001)
check.expect("Example 2", final_jeopardy (15000 ,  15000,  800), 15000)
check.expect("Example 3", final_jeopardy (1500 ,  15000,  800), 0)
