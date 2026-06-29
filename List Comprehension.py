input = int(input("Enter the number:"))
odd_numbers = [num for num in range(input)]
print("List of the odd numbers", odd_numbers)

fruits = ["apples", "banana", "dates", "cherry"]
capitalized_fruits = [fruits.capitalize() for fruits in fruits]
print("Original list:", fruits)
print("Capital letter fruits:", capitalized_fruits)