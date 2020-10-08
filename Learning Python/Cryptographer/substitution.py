# This classes takes care of the Substitution method of cryptography, in which a message use a number of steps to
# change each of its letters to another letter located further away in the alphabet (a step of 4 would transform an
# 'A' into an 'E'). It's a basic form of cryptography, but that serves to illustrate how Python can handle lists and
# strings, in a fun way. The Encoding and Decoding steps of the process were put in separated methods to increase
# readability

from tools import Tools


class Substitution:

    @staticmethod
    def Encode(text, steps):
        encoded_text = Tools.ListToString(Substitution.ReplaceLetters(text, steps))
        return encoded_text

    @staticmethod
    def Decode(text, steps):
        decoded_text = Tools.ListToString(Substitution.ReplaceLetters(text, (steps * -1)))
        return decoded_text

    @staticmethod
    def ReplaceLetters(text, steps):
        input_list = Tools.StringToList(text)
        for i in range(len(input_list)):
            num = ord(input_list[i])
            if not input_list[i].isalpha():
                continue
            else:
                if num in range(65, 91):
                    num += steps
                    num = num - (91 - 65) if num >= 91 else num
                    num = num + (91 - 65) if num <= 64 else num
                elif num in range(97, 123):
                    num += steps
                    num = num - (123 - 97) if num >= 123 else num
                    num = num + (123 - 97) if num <= 96 else num

            input_list[i] = chr(num)
        return input_list
