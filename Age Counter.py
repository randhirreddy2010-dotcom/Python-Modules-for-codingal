try:
    age = int(input("Enter the age:"))
    if age < 0:
        print("Age cant be negative")
    elif age == 0:
        print("Age cant be zero")
    else:
        print("Age is correct")

    if age%2==0:
        print("f/ The age entered is even")
    else:
        print("f/ The age entered is odd")
except ValueError as e:
    print("Exception: the age entered must be in numbers and not in string")