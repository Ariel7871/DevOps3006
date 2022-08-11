import requests

print("Ariel")
try:
    f = int(input("Enter number: "))
    r = 5 / 0
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")
except BaseException as e:
    print("Something went wrong, here is more")
    print(e.args)
print("Lior")
