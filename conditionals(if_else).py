# 1. Write a program to check if a number is even or odd.
def even_or_odd():
    n = int(input("Enter a number: "))
    print("Even" if n % 2 == 0 else "Odd")

even_or_odd()


# 2. Given three numbers, find the largest one using if-elif-else.
def largest_of_three():
    a = int(input("Enter first: "))
    b = int(input("Enter second: "))
    c = int(input("Enter third: "))
    print(f"Largest: {max(a, b, c)}")

largest_of_three()


# 3. Write a program that categorizes a given age into child (<13), teen (13-19), adult (20+).
def categorize_age():
    age = int(input("Enter age: "))
    if age < 13:
        print("Child")
    elif age < 20:
        print("Teen")
    else:
        print("Adult")

categorize_age()


# 4. Given three sides of a triangle, determine if it’s equilateral, isosceles, or scalene.
def triangle_type():
    a = int(input("Side A: "))
    b = int(input("Side B: "))
    c = int(input("Side C: "))
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

triangle_type()
