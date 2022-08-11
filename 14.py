import ast

my_file = open("config.json")
c = dict(ast.literal_eval(my_file.read()))
if c["name"] == "Nathan":
    print("My name is Ariel")
# configuration = dict(ast.literal_eval(my_file.read()))

# or

with open("names.txt") as my_file:
    for name in my_file.readlines():
        print(name.strip())
