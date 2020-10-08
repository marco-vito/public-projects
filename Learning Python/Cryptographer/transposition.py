# This classes takes care of the Transposition method of cryptography, in which the characters of a
#     # message are distributed inside a matrix, line by line, with a line length defined by a key; then, the message
#     # is rewritten by putting together the same character column by column (instead of line by line). For this to
#     # work, we need to transform our list into an array, and then reshape it; but, since arrays cannot be extended,
#     # first we have to make sure the list to be transformed fits the matrix shape we'll use; to that end,
#     # we append extra whitespace characters to the list that doesn't fit an exact matrix. The Encoding and Decoding
#     steps of the process were put in separated methods to increase readability

import math
import numpy
from tools import Tools


class Transposition:

    @staticmethod
    def Encode(text, key):
        is_encoding = True
        output_list = Transposition.RepositionLetters(text, key, is_encoding)
        encoded_message = Tools.ListToString(output_list)
        return encoded_message

    @staticmethod
    def Decode(text, key):
        is_encoding = False
        output_list = Transposition.RepositionLetters(text, key, is_encoding)
        decoded_message = Tools.ListToString(output_list)
        return decoded_message

    @staticmethod
    def RepositionLetters(text, key, is_encoding):
        input_list = Tools.StringToList(text)
        list_height = math.ceil(len(input_list) / key)
        while len(input_list) != (list_height * key):
            input_list.append(" ")
        array = numpy.array(input_list)
        if is_encoding:
            new_array = array.reshape(list_height, key)
        else:
            new_array = array.reshape(key, list_height)
        print(new_array)
        output_list = []

        for i in range(len(new_array[0])):
            for j in range(len(new_array)):
                output_list.append(new_array[j, i])

        return output_list
