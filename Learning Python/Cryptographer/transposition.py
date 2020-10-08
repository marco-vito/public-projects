# The goal of this program is to create a series of simple functions that can code or decode a message following
# some basic cryptography patterns; it's meant to be a simple tool, with a simple interface, that any person can easily
# use to trade some secret messages with friends.

import math
import numpy
from tools import Tools


class Transposition:

    # This function will encode a message by using Transposition, based on a key; that means that the characters of a
    # message are distributed inside a matrix, line by line, with a line length defined by a key; then, the message
    # is rewritten by putting together the same character column by column (instead of line by line). For this to
    # work, we need to transform our list into an array, and then reshape it; but, since arrays cannot be extended,
    # first we have to make sure the list to be transformed fits the matrix shape we'll use; to that end,
    # we append extra whitespace characters to the list that doesn't fit an exact matrix. The boolean parameter
    # defines if the function is encoding or decoding a given message. The Encoding and Decoding steps of the process
    # were put in separated functions to increase readability

    @staticmethod
    def Transposition(text, key, is_encoding=True):
        input_list = Tools.StringToList(text)
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
