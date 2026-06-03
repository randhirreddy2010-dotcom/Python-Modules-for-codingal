try:
    number = int(input("Enter a number:"))
    print("the number entered is", number)
except ValueError as e:
    print("Execption:",e)