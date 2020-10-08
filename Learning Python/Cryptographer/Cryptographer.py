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
    new_string = "".join(output_list)

    return new_string


# The next function get a list made by the input text and change each letter by a given number of steps; this function
# allows both the encoding and the decoding of simple letter substitution messages; the function ignore special
# characters and blank space.

def EncodeSimpleSubstitution(input_list, steps):

    for i in input_list:
        num = ord(i)
        if num not in range(65, 91) and num not in range(97, 123):
            continue
        else:
            for n in range(steps):
                num += 1
                if num == 91:
                    num = 65
                elif num == 123:
                    num = 97
        i = chr(num)

    return input_list

