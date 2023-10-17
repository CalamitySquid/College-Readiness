def verifcation(age, drive, vote, drink, gpa, graduation):
  if age >= 18 and drive == "yes" and vote == "yes" and drink == "yes" and gpa >= 3.0 and graduation == "yes":
    print("You're ready for college!")
  else:
    print("You're not ready for college.")