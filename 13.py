def save_name(names_file):
    my_file = open(names_file, "a")
    current_name = input("Enter your name: ")
    my_file.write(current_name + "\n")
    my_file.close()


def moshe(david):
    print(david)


def haim(avi):
    print(avi)


def show_name(names_file, blabla):
    my_file = open(names_file, "r")
    for name in my_file.readlines():
        print(name, end='')
    my_file.close()


for i in range(5):
    save_name("names.txt")
show_name("names.txt")


def moshe(david):
    print(david)
