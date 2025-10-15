import random

x = "y"

while x == "y":
    # Roll two dice
    number = random.randint(1, 6)
    number_2 = random.randint(1, 6)
    
    # Print result for the first dice
    if number == 1:
        print("""
        ________
        |      |
        |   0  |
        |      |
        --------
        """)
    elif number == 2:
        print("""
        ________
        |      |
        |0    0|
        |      |
        --------
            """)
    elif number == 3:
        print("""
        ________
        |   0  |
        |   0  |
        |   0  |
        --------
        """)
    elif number == 4:
        print("""
        ________
        |0    0|
        |      |
        |0    0|
        --------
        """)
    elif number == 5:
        print("""
        ________
        |0    0|
        |   0  |
        |0    0|
        --------
        """)
    elif number == 6:
        print("""
        ________
        |0    0|
        |0    0|
        |0    0|
        --------
        """)

    # Print result for the second dice
    if number_2 == 1:
        print("""
        ________
        |      |
        |   0  |
        |      |
        --------
        """)
    elif number_2 == 2:
        print("""
        ________
        |      |
        |0    0|
        |      |
        --------
            """)
    elif number_2 == 3:
        print("""
        ________
        |   0  |
        |   0  |
        |   0  |
        --------
        """)
    elif number_2 == 4:
        print("""
        ________
        |0    0|
        |      |
        |0    0|
        --------
        """)
    elif number_2 == 5:
        print("""
        ________
        |0    0|
        |   0  |
        |0    0|
        --------
        """)
    elif number_2 == 6:
        print("""
        ________
        |0    0|
        |0    0|
        |0    0|
        --------
        """)

    # Ask to roll again
    x = input("Enter y to continue and n to stop: ")


#Here is a shorter way to do it

import random

# Dictionary to store the dice faces
dice_faces = {
    1: """
    ________
    |      |
    |   0  |
    |      |
    --------
    """,
    2: """
    ________
    |      |
    |0    0|
    |      |
    --------
    """,
    3: """
    ________
    |   0  |
    |   0  |
    |   0  |
    --------
    """,
    4: """
    ________
    |0    0|
    |      |
    |0    0|
    --------
    """,
    5: """
    ________
    |0    0|
    |   0  |
    |0    0|
    --------
    """,
    6: """
    ________
    |0    0|
    |0    0|
    |0    0|
    --------
    """
}

x = "y"

while x == "y":
    # Roll two dice
    number = random.randint(1, 6)
    number_2 = random.randint(1, 6)

    # Print the dice face from the dictionary
    print(dice_faces[number])
    print(dice_faces[number_2])

    # Ask to roll again
    x = input("Enter y to continue and n to stop: ")

