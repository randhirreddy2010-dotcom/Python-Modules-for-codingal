import random 

print("Starting to generate a new password..")

characters="abcdefghijklmnopqrstuvwxyzYZ1234567890@#$%*"

password_lenght = int(input("Enter desired password lenght"))

password = []

for i in range (password_lenght):

  password.append(random.choice(characters))

password = "".join(password)

print("Your new password is: "+ password)
