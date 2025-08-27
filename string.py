
# 1. Write a Python program to reverse a given string (e.g., "hello" → "olleh").

def reverse_string():
    text = input("Enter a string to reverse: ")
    print("Reversed string:", text[::-1])

reverse_string()


# 2. Write a program that counts the number of vowels (a, e, i, o, u) in a given string.

def count_vowels():
    text = input("Enter a string: ")
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in text if char in vowels)
    print("Number of vowels:", count)

count_vowels()


# 3. Write a function that checks if two strings are anagrams (e.g., "listen" and "silent").

def are_anagrams():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print("Are anagrams?" , sorted(s1) == sorted(s2))

are_anagrams()


# 4. Write a program to count the occurrences of each word in a given sentence.

def word_occurrences():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    counts = {word: words.count(word) for word in set(words)}
    print("Word counts:", counts)

word_occurrences()


# 5. Write a function that implements the Caesar Cipher (shift letters by n positions).

def caesar_cipher():
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    cipher = ''.join(
        chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.islower()
        else chr((ord(c) - ord('A') + shift) % 26 + ord('A')) if c.isupper()
        else c for c in text
    )
    print("Encrypted text:", cipher)

caesar_cipher()


# 6. Write a regex-based program to validate an email address.
import re

def validate_email():
    email = input("Enter an email address: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

validate_email()
