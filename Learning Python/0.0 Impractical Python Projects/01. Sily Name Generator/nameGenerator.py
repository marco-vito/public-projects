import sys
import random

male_names = ("Alexander", "Timotheus", "Peter", "Kilian", "Rupert", "Robert", "Endian", "Bartolomeu")
female_names = ("Alexandria", "Sistine", "Magnolia", "Lavinia", "Christel", "Floria", "Zumba", "Tricia")
surname = ("The Bloodthirsty", "The Chaste", "The Treacherous", "Blood Moon", "of the Undying Will",
           "Thunder Spear", "Squealer")


def randomName(genre):

    if genre.lower() == "female":
        first_name = random.choice(female_names)
    elif genre.lower() == "male":
        first_name = random.choice(male_names)
    else:
        return "Sorry, we only have male and female names."
    last_name = random.choice(surname)

    return "Your new character is called {} {}".format(first_name, last_name)
