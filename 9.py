excluded_name = "Michael"
greeting_word = "Hello"


def print_hello(name):
    if name != excluded_name:
        print(f"{greeting_word} {name}")


print_hello("Moshe")
print_hello("Ariel")
print_hello("Michael")


def greet_name(name, excluded_name="Michael", greeting_word="Hello"):
    if name != excluded_name:
        print(f"{greeting_word} {name}")


greet_name("Ariel")
greet_name("Michael")


def multiply(x, y, c):
    result1 = x * y
    result2 = x / y
    return result1, result2


r = multiply(4, 2, 1)
print(r[0])
print(r[1])


user_name = input("enter your name: ")
greet_name(user_name)


user_name = int(input("enter your age: "))
greet_name(user_name)


greet_name("Michael")



