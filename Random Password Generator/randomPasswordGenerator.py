import random

print("$$ RANDOM PASSWORD GENERATOR BY Pratham3shT $$")


def again():
    print("Do you want to use our program again? Enter here: ", end="")
    doAgain = str(input())

    if(doAgain.lower() == "yes"):
        inputs()
    elif(doAgain.lower() == "no"):
        print("Thank you for using our program")
    else:
        print("Error : type yes or no")
        again()


def password_generator(char_set,password_times,password_length):

    for i in range(password_times):
        password = ""
        for j in range(password_length):
            password += random.choice(char_set)

        print("Password", i+1, "is", password)
    print("")



def select_level(level):

    print("Select the level of difficulty for password:  \n Enter 1 for easy \n Enter 2 for moderate \n Enter 3 for hard \n Enter 4 for Unbreakable")
    print("Enter here: ", end="")
    level = int(input())

    if(level == 1):
        char_set = small_alphabets
    elif (level == 2):
        char_set = small_alphabets + capital_aplabets
    elif (level == 3):
        char_set = small_alphabets + capital_aplabets + numbers
    elif (level == 4):
        char_set = small_alphabets + capital_aplabets + numbers + special_char
    else:
        print("")
        print("Error : Enter a valid number")
        print("")
        char_set = select_level(level)
    

    return char_set


def inputs():
    print("Select the length of the password: ", end="")
    password_length = int(input())
    print("How many passwords you want to generate ? Enter here: ", end="")
    password_times = int(input())
    level = ""
    char_set = select_level(level)
    password_generator(char_set,password_times,password_length)
    again()





small_alphabets = "abcdefghijklmnopqrstuvwxyz"
capital_aplabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_char = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
inputs()


