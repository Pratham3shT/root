import string
import pyautogui
import itertools
import time


def again():
    print("Do you want to run the program gain? Type yes or no: ",end="")
    doAgain = str(input())

    if(doAgain == 'yes'):
        inp()
    elif(doAgain == 'no'):
        print("Thank you for using the Program")


def brute_force(password, char_list):
    guess_password = ""
    begin = time.time()
    while((guess_password) != (password)):
        for xs in itertools.product(char_list, repeat=len(password)):
            print("<==D=====E=====N====", list(xs), "====I=====E=====D==>")
            guess_password = list(xs)
            if(guess_password) == (password):
                print("Your password is: "+"".join(guess_password))
                end = time.time()
                print(f"Your password got cracked in {end - begin}")
                pyautogui.alert("Your password is: " + "".join(guess_password))
                pyautogui.alert(f"Your password got cracked in {end - begin} secs")
                again()
                break

def inp():
    all_chars = string.printable
    char_list = list(all_chars)
    passwd = pyautogui.password("Enter password (text will be hidden)")
    password = list(passwd)
    
    
    if (len(password)>8):
        print("The Password will take a long time to crack. Do you want to continue? Type yes or no : ")
        cont = str(input())

        if(cont == 'yes'):
            brute_force(password)
        elif(cont=='no'):
            print("Run again")
        else:
            print("Error type again")
    else:
        brute_force(password,char_list)      


inp()

