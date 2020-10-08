# This class handle general simple tasks that are used by multiple encrypting processes, in a way to keep the
# readability of the code and reuse the same functions whenever they are needed, without having to rewrite everything.

class Tools:

# When dealing with user input, we get strings; when handling each character of a string as a separated element, we
# need lists; when outputting results, we need strings once again. These two functions will take care of transforming
# strings into lists, and vice versa.

def StringToList(text):
    new_list = list(text)

    return new_list


def ListToString(output_list):
    new_string = "".join(output_list)

    return new_string