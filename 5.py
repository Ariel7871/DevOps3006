is_ture = False
a = 2
b = 2.5
str0ne = "One"
strThree = "Three"
print(type(a == b))
if a < b and (b != 1 or not str0ne == "Three"):
    print("a is smaller then b")
elif a == b:
    print("a equals b")
elif b > 1:
    print("B is bigger then 1")
else:
    print("b smaller then a")

names = ["Kate", "Ariel", "Denis", "Lior"]
other_list = ["Nathan"]
name_to_find = "Nathan"
if name_to_find in names:
    print(f"{name_to_find} is on the list")

if len(other_list) > 0:
    print("other list has values")

else:
    print(f"{name_to_find} is not on the list")

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
if type(k) is int:
    print("I like numbers")
elif type(k) is str:
    print("I like strings")
print(k is f)
print(t == e)
print(t is e)


