from arit import addition, sub
from get_data import get_number
import datetime

def print_something():
    print("Something")


def dec(function_to_run):

    def wrapper():
        print(datetime.datetime.now())
        function_to_run()
        print(datetime.datetime.now())
    return wrapper