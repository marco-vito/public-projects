from substitution import Substitution

test_message = "ABCD abcd ZYXW"
print(Substitution.Encode(test_message, 4))
print(Substitution.Decode(test_message, 4))
