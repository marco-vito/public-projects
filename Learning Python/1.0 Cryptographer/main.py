from substitution import Substitution
from transposition import Transposition

test_message = "ABCD abcd ZYXW"
sub_coded_message = Substitution.Encode(test_message, 4)
sub_decoded_message = Substitution.Decode(sub_coded_message, 4)
print("Encoding by Substitution: " + sub_coded_message)
print("Decoding by Substitution: " + sub_decoded_message)
trans_coded_message = Transposition.Encode(test_message, 3)
print("Encoding by Transposition: " + trans_coded_message)
trans_decoded_message = Transposition.Decode(trans_coded_message, 3)
print("Decoding by Transposition: " + trans_decoded_message)

