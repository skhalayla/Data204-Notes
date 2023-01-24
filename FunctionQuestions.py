print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
n = int(input("Choose a number to see its divisors: "))

def divisors(n):
    result = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return list(result)

print(divisors(n))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
a = int(input("Enter the number whose divisibility needs to be checked: "))
b = int(input("Enter the number with which divisibility needs to be checked: "))

def numbers(a, b):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if a % b == 0:
            result.add(i)
            result.add(a//i)
            return True
        else:
            return False
print(numbers(a, b))

# // is a floor division - divides first argument by second and rounds to nearest whole number

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", " "]

l = str(input("Letter you want to know position of: "))

def alphabet_position(l):
    for ind in l:
        answer = alphabet.index(ind)
        return answer

print(alphabet_position(l))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", " "]

name = str(input("Type your name to produce an ID: "))

def id(name):
    position = ''
    for i in name.lower():
        position += str(alphabet_position(i)) # calling prev funct from 2a

    return position

print('Your ID Number is: ', id(name))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", " "]

pasw = str(input("Type a word to generate a password: "))

def password(pasw):
    a = 0
    b = id(pasw)
    for i in b:
        a += int(i)

    return int(b) - a #have to specify

print('Your password is: ', password(pasw))


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def isPrime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False

print(isPrime(int(input("Enter a number: "))))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def isPrimee(x):
    try: #try except method - good for error handling
        x = int(x)
        if x > 1:
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True
        return False
    except ValueError:
        print("Try again: ")
        print(isPrimee(input("Enter a number: ")))

print(isPrimee(input("Enter a number: ")))


# -------------------------------------------------------------------------------------- #






