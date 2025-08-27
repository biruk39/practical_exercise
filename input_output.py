 #1. Write a program that takes a user's name and age as input and prints: "Hello [name], you are [age] years old


def user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}, you are {age} years old.")

user()




# 2. Write a program that takes two numbers and prints their sum.

def numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Sum: {a + b}")

numbers()




# 3. Write a program that reads a file and counts the number of words in it.
def words():
    filename = input("Enter the file name to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"The file contains {word_count} words.")
    except FileNotFoundError:
        print("File not found.")

words()


# 4. Write a program that takes a sentence and writes it to a file in reverse order.

def reverse_string():
    s = input("Enter a string to reverse: ")
    print(f"Reversed: {s[::-1]}\n")

reverse_string()


# 5. Write a program that reads a CSV file and converts it into a dictionary.
import csv

def csv_to_dict():
    filename = input("Enter CSV filename: ")
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
            print("CSV converted to dictionary:")
            for item in data:
                print(item)
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print("Error reading CSV:", e)

csv_to_dict()

# 6. Write a script that monitors a log file and alerts if a specific keyword appears.
import os
import time
def monitor_log_file():
    filename = input("Enter log file name to monitor: ")
    keyword = input("Enter keyword to alert on: ")
    
    if not os.path.isfile(filename):
        print("File does not exist.")
        return

    print(f"Monitoring '{filename}' for keyword '{keyword}'... Press Ctrl+C to stop.")
    try:
        with open(filename, 'r') as file:
            file.seek(0, os.SEEK_END)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.5)
                    continue
                if keyword in line:
                    print(f"[ALERT] Keyword '{keyword}' found: {line.strip()}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

monitor_log_file()

