# The goal of this program is to create a series of simple functions that can code or decode a message following
# some basic cryptography patterns; it's meant to be a simple tool, with a simple interface, that any person can easily
# use to trade some secret messages with friends.

import numpy, math


# The input the users will give is a string; but, to replace letters individually, we need to work with lists; on the
# inverse path, to show the user a clear result, we need to give them back a string, not the manipulated list. The first
# functions in this script are used to transform a string into a List, and vice versa.

def StringToList(text):
    new_list = list(text)

    return new_list


def ListToString(output_list):
    new_string = "".join(output_list)

    return new_string


# The next functions get a list made by the input text and change each letter by a given number of steps; these
# functions allows both the encoding and the decoding of simple letter substitution messages, depending of a boolean
# introduced as a parameter; the function ignore special characters and blank space. The Encoding and Decoding steps
# of the process were put in separated functions to increase readability

def Substitution(input_list, steps, is_encoding=True):
    for i in range(len(input_list)):
        num = ord(input_list[i])
        if not input_list[i].isalpha():
            continue
        else:
            if is_encoding:
                num = EncodingSubstitution(num, steps)
            else:
                num = DecodingSubstitution(num, steps)

        input_list[i] = chr(num)

    return input_list


def EncodingSubstitution(number, steps):
    if number in range(65, 91):
        number += steps
        number = number - (91 - 65) if number >= 91 else number
    elif number in range(97, 123):
        number += steps
        number = number - (123 - 97) if number >= 123 else number
    return number


def DecodingSubstitution(number, steps):
    if number in range(65, 91):
        number -= steps
        number = number + (91 - 65) if number <= 64 else number
    elif number in range(97, 123):
        number -= steps
        number = number + (123 - 97) if number <= 96 else number
    return number


# This function will encode a message by using Transposition, based on a key; that means that the characters of a
# message are distributed inside a matrix, line by line, with a line length defined by a key; then, the message is
# rewritten by putting together the same character column by column (instead of line by line). For this to work,
# we need to transform our list into an array, and then reshape it; but, since arrays cannot be extended,
# first we have to make sure the list to be transformed fits the matrix shape we'll use; to that end, we append extra
# whitespace characters to the list that doesn't fit an exact matrix. The boolean parameter defines if the function
# is encoding or decoding a given message. The Encoding and Decoding steps of the process were put in separated
# functions to increase readability

def Transposition(input_list, key, is_encoding=True):
    list_height = math.ceil(len(input_list) / key)
    while len(input_list) != (list_height * key):
        input_list.append(" ")
    array = numpy.array(input_list)
    if is_encoding:
        new_array = array.reshape(list_height, key)
    else:
        new_array = array.reshape(key, list_height)
    output_list = []

    for i in range(key):
        for j in range(list_height):
            output_list.append(new_array[j, i])

    return output_list