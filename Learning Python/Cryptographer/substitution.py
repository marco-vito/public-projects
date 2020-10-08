# This classes takes care of the Substitution method of cryptography, in which a message use a number of steps to
# change each of its letters to another letter located further away in the alphabet (a step of 4 would transform an
# 'A' into an 'E'). It's a basic form of cryptography, but that serves to illustrate how Python can handle lists and
# strings, in a fun way.


# The next functions get a list made by the input text and change each letter by a given number of steps; these
    # functions allows both the encoding and the decoding of simple letter substitution messages, depending of a boolean
    # introduced as a parameter; the function ignore special characters and blank space. The Encoding and Decoding steps
    # of the process were put in separated functions to increase readability

class Substitution:

import tools


    def Substitution(input_list, steps, is_encoding=True):
        for i in range(len(input_list)):
            num = ord(input_list[i])
            if not input_list[i].isalpha():
                continue
            else:
                if is_encoding:
                    num = Substitution.EncodingSubstitution(num, steps)
                else:
                    num = DecodingSubstitution(num, steps)

            input_list[i] = chr(num)
            encoded_text = tools.ListToString(input_list)
        return encoded_text

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