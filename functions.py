
# 1. Write a function that takes a number and returns its square.
def square_number():
    try:
        n = float(input("Enter a number: "))
        print(f"Square of {n} is {n ** 2}")
    except ValueError:
        print("Please enter a valid number.")

square_number()



# 2. Write a function that checks if a string is a palindrome (e.g., "madam").

def check_palindrome():
    s = input("Enter a string: ")
    if s == s[::-1]:
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")

check_palindrome()



# 3. Write a decorator that logs the execution time of a function.
import time

def log_time(f):
    def w(): s=time.time(); r=f(); print(f"Time: {time.time()-s:.6f}s"); return r
    return w

@log_time
def add():
    print("Sum:", sum(map(int, input("Enter numbers: ").split())))

add()



# 4. Write a generator function that yields an infinite sequence of prime numbers
def primes():
    D, q = {}, 2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]: D.setdefault(p+q, []).append(p)
            del D[q]
        q += 1

n = int(input("How many primes? "))
gen = primes()
for _ in range(n):
    print(next(gen))