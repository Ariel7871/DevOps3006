x = 5
y = 7
if x > y:
    print("Big")

if x == y:
    print("Same")

if y > x:
    print("Small")

for i in range(5):
    print(i)

weather = 1
if weather == 1:
    print("Summer")
elif weather == 2:
    print("Winter")
elif weather == 3:
    print("Fall")
elif weather == 4:
    print("Spring")

count = 1
while count < 11:
    print(count)
    count = count + 1

age = 22
letter = "A"
currency = 4.2
flew = True
apartment_number = 16

print(age)
print(letter)
print(currency)
print(flew)
print(apartment_number)
print(currency + age)

phonenumber: int = int(input("enter your phone number: "))
print("Phone number", phonenumber)

Hello = "Hello"


def printHello():
    print(f"{Hello}")


printHello()
calculateanwser = 5 + 3.2


def calculate():
    print(f"{calculateanwser}")


calculate()

name = input("enter your name: ")
num = int(input("enter number: "))


def print_name(name):
    print(name)


print_name(name)


def divide_number(num):
    print(num / 2)


divide_number(num)


# Didn't know how to really complete that

def return_sum(x, y):
    return x + y


def add_space(word_a, word_b):
    return word_a + " " + word_b
