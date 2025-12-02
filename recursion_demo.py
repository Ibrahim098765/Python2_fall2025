# recursion '
def func():
    x=10
    func()
from sys import getrecursionlimit
from sys import setrecursionlimit
def get_recursion_limit():
    print(f'Recursion limit: {getrecursionlimit()}')
get_recursion_limit()
def set_recursion_limit(num):
    setrecursionlimit(num)
    print(f'Recursion limit has been set to:{getrecursionlimit()}')

rec_limit  = 2000
set_recursion_limit(rec_limit)
####################count down examplke
# iterative way 
def count_down(n):
    """ iterative count down """
    for i in range(n, -1, -1):
        print(f'count from to:{i}')
print(f'\niterative count down:')
count_down(5)
# recusrive
def count_down_re(n):
    """recusrive count down""" 
    # base case
    if n < 0:
        return
    print(f'count down to:{n}')
    count_down_re(n-1)
print(f'\nRecursive count down:')
count_down_re(5)
###################### sum digits
def sum_digit(num):
    """ sum all digits of a number"""
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total 
print(f'\niterative sum digit:')
num = 12345
total = sum_digit(num)

print(f' sum of all digits of {num}:{total}')
# rucusive way 
def sum_digit_re(num):
    """ recursive sum digit """
    if num % 10 == num:
        return num 
    return num % 10 + sum_digit_re(num // 10)
print(f'\nRecursive sum digit:')
print(f'Sum of all digit of {num}:{sum_digit_re(num)}')
########### factorial
def factorial(n):
    """ iterative factorial"""
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print(f'\n iterative factorial()')
result = factorial(5)
print(f' factorial(5) = {result}')
# recusive way
def factorial_re(n):
    """ mrecusive factorial """
    # base case
    print(f'factorial() called with n= {n}')
    result = 1 if n <= 1 else n * factorial_re(n-1)
    print(f' factorial({n}) returns {result} ')
    return result
print(f'\nRecusive factorial()')
n = 5
result = factorial_re(n)
print(f'n= {n}, factorial of {n} = {result}')
