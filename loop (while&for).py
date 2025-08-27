# 1) Print numbers from 1 to 10 using a for loop.

def number_printer():
    choice = input("Choose an option:\n1) Print numbers from 1 to 10\n> ")
    if choice == "1":
        for i in range(1, 11):
            print(i)
    else:
        print("Invalid option.")

number_printer()



# 2) Print the multiplication table of a given number using a while loop.
def multiplication_table():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiplication_table()



# 3) Print a pyramid pattern using * 
def pyramid():
    n = int(input("Enter height of pyramid: "))
    for i in range(1, n+1):
        print('*' * i)
pyramid()


# 4) Write a program to find all prime numbers up to a given number.
def prime_numbers():
    limit = int(input("Find primes up to: "))
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            print(num, end=" ")
    print()

prime_numbers()



# 5) Functions (recursion, args/kwargs)

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def sum_args(*args):
    return sum(args)

n = int(input("Enter a number to calculate its factorial (recursion): "))
print("Factorial:", factorial(n))

nums = input("Enter numbers separated by spaces to sum them (*args): ")
nums = list(map(int, nums.split()))
print("Sum:", sum_args(*nums))


# 6) Write a recursive function to compute the factorial of a number.

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

n = int(input("Enter a number to compute its factorial: "))
print(f"Factorial of {n} is {factorial(n)}")



# 7) Write a function that accepts any number of arguments and returns their sum.

def sum_args(*args):
    return sum(args)

nums = input("Enter numbers separated by spaces to sum: ")
nums = list(map(int, nums.split()))
print("The sum is:", sum_args(*nums))


# 8) Write a loop that prints numbers from 1 to 10 but skips 5 using continue.
print("Printing numbers from 1 to 10, skipping 5:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)



# 9) Write a loop that stops when it encounters the number 7 using break.
print("Printing numbers from 1 to 10, stopping at 7:")
for i in range(1, 11):
    if i == 7:
        break
    print(i)


# 10) Write a program to solve the Tower of Hanoi problem recursively.

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        tower_of_hanoi(n-1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n-1, auxiliary, target, source)

n = int(input("Enter number of disks for Tower of Hanoi: "))
tower_of_hanoi(n, 'A', 'C', 'B')



# 11) Simulate a tic-tac-toe game using loops and conditionals.

def tic_tac_toe():
    board = [" "]*9

    def print_board():
        for i in range(0, 9, 3):
            print(" | ".join(board[i:i+3]))
            if i < 6: print("-"*5)

    player = "X"
    for turn in range(9):
        print_board()
        move = int(input(f"Player {player}, choose position (1-9): ")) - 1
        if 0 <= move < 9 and board[move] == " ":
            board[move] = player
            # Check win
            wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            if any(board[a]==board[b]==board[c]==player for a,b,c in wins):
                print_board()
                print(f"Player {player} wins!")
                return
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")
    print_board()
    print("It's a draw!")

tic_tac_toe()