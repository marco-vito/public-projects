# The goal of this program is to create a series of simple functions that can code or decode a message following
# some basic cryptography patterns; it's meant to be a simple tool, with a simple interface, that any person can easily
# use to trade some secret messages with friends.


# The input the users will give is a string; but, to replace letters individually, we need to work with lists; on the
# inverse path, to show the user a clear result, we need to give them back a string, not the manipulated list. The first
# functions in this script are used to transform a string into a List, and vice versa.

def StringToList(text):
    new_list = list(text)

    return new_list


def ListToString(output_list):
    new_string = ''

    for i in output_list:
        new_string += str(i)

    return new_string
