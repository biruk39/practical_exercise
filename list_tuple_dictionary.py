
# I. Write a program to find the length of a tuple without using len().
def tuple_length():
    t = eval(input("Enter a tuple: "))
    count = 0
    for _ in t:
        count += 1
    print("Length of tuple:", count)

tuple_length()


# II. Create a tuple with numbers and print the maximum and minimum values.\
def tuple_min_max():
    t = eval(input("Enter a tuple of numbers: "))
    print("Min:", min(t))
    print("Max:", max(t))

tuple_min_max()


# III. Write a program to remove duplicates from a list.
def remove_duplicates():
    lst = eval(input("Enter a list: "))
    print("List without duplicates:", list(set(lst)))

remove_duplicates()


# IV. Given a list [1, 2, 3, 4, 5], square each element and store it in a new list.
def square_list():
    lst = [1, 2, 3, 4, 5]
    squared = [x**2 for x in lst]
    print("Original:", lst)
    print("Squared :", squared)

square_list()


# V. Write a program to merge two dictionaries.
def merge_dicts():
    d1 = eval(input("Enter first dictionary: "))
    d2 = eval(input("Enter second dictionary: "))
    merged = {**d1, **d2}
    print("Merged Dictionary:", merged)

merge_dicts()


# VI. Given a dictionary {'a': 1, 'b': 2, 'c': 3}, swap keys and values (output: {1: 'a', 2: 'b', 3: 'c'}).
def swap_dict():
    d = {'a': 1, 'b': 2, 'c': 3}
    swapped = {v: k for k, v in d.items()}
    print("Original:", d)
    print("Swapped :", swapped)

swap_dict()


# VII. Write a function that returns the n-th Fibonacci number using memoization (optimization)
def fib(n, m={}): return m[n] if n in m else n if n<2 else m.setdefault(n, fib(n-1,m)+fib(n-2,m))

name = input("Name: ")
print(f"Hi, {name}!\nFibonacci:")
print(fib(int(input("n = "))))


# VIII. Implement a list comprehension that generates all Pythagorean triplets up to n.
def pythagorean_triplets():
    n = int(input("Generate triplets up to: "))
    triplets = [(a, b, c)
                for a in range(1, n)
                for b in range(a, n)
                for c in range(b, n)
                if a**2 + b**2 == c**2]
    print("Triplets:", triplets)

pythagorean_triplets()


# IX. Write a function that simulates a shopping cart using nested dictionaries (add/remove items, calculate total).
def shopping_cart():
    cart = {}
    while True:
        print("\nShopping Cart Menu")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Checkout")
        choice = input("Choice: ")
        if choice == "1":
            item = input("Item name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            cart[item] = {"price": price, "quantity": qty}
        elif choice == "2":
            item = input("Item to remove: ")
            if item in cart:
                del cart[item]
        elif choice == "3":
            print(cart)
        elif choice == "4":
            total = sum(v["price"] * v["quantity"] for v in cart.values())
            print("Total cost: $", total)
            break
        else:
            print("Invalid choice")

shopping_cart()


# X. Implement a dictionary-based cache system with a max_size (LRU eviction).

from collections import OrderedDict
from mimetypes import init

class LRUCache:
    def __init__(self, max_size=5):
        self.cache = OrderedDict()
        self.max_size = max_size

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)  

init()


# XI. Write a function that takes a tuple of numbers and returns a new tuple with only even numbers.

def even_in_tuple():
    t = eval(input("Enter tuple of numbers: "))
    even_t = tuple(x for x in t if x % 2 == 0)
    print("Even numbers tuple:", even_t)

even_in_tuple()


# XII. Write a program to sort a list of tuples based on the second element (e.g., [('a', 3), ('b', 1)] → [('b', 1), ('a', 3)]).
def sort_tuples():
    lst = eval(input("Enter list of tuples: "))
    sorted_lst = sorted(lst, key=lambda x: x[1])
    print("Sorted list:", sorted_lst)

sort_tuples()


# XIII. Write a function to flatten a nested list (e.g., [[1, 2], [3, 4]] → [1, 2, 3, 4]).
def flatten_list():
    nested = eval(input("Enter nested list: "))
    flat = [x for sub in nested for x in sub]
    print("Flattened list:", flat)

flatten_list()


# XIV. Write a program to remove all occurrences of a specific element from a list.
def remove_all_occurrences():
    lst = eval(input("Enter list: "))
    val = eval(input("Enter value to remove: "))
    filtered = [x for x in lst if x != val]
    print("Resulting list:", filtered)

remove_all_occurrences()


# XV. Write a function that inverts a dictionary (handle duplicate values by storing them in a list).
def invert(d):
    inv = {}
    for k, v in d.items(): inv.setdefault(v, []).append(k)
    return inv

d = {int(input(f"Key {_+1}: ")): int(input("Value: ")) for _ in range(int(input("How many pairs? ")))}
print("Inverted:", invert(d))


# XVI. Given a dictionary of student marks, find the student with the highest average score.
def highest_avg_student():
    students = eval(input("Enter student marks (e.g. {'John': [80,90]}): "))
    avg_scores = {name: sum(marks)/len(marks) for name, marks in students.items()}
    best = max(avg_scores, key=avg_scores.get)
    print(f"Top student: {best} with average {avg_scores[best]:.2f}")

highest_avg_student()
