names = ["Kate", "Ariel", "Denis", "Lior"]


#for i in range(len(names)):
#    names[i] = "Nathan"

for name in names:
    if name == "Denis":
        continue
    print(name)

print("")

for name in names:
    if name == "Denis":
        break
    else:
        pass
    print(name)

#a = 0
#while a < 5:
#    print(a)
#    a = a + 1