############# ISAAC MUNGUIA, GERARDO PINEDA, SEBASTIAN WONG, JESUS RUIZ ########

print("Are you ready for college? Let's find out!")
from verification import *
age = int(input("How old are you? "))
drive = input("Can you drive? ").lower()
vote = input("Can you vote? ").lower()
drink = input("Can you drink? ").lower()
gpa = float(input("What is your gpa? "))
graduation = input("Have you graduated high school or recieved high school diploma equivalent? ").lower()
verifcation(age, drive, vote, drink, gpa, graduation)