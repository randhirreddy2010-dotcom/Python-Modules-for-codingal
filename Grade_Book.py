students = {
    "Jack":95,
    "Alice": 93,
    "Sarah":94,
    "James": 92,
    "Randy": 91
}
total = 0
for score in students.values():
    total += score
    print("average", total/len(students))
top= max(students, key=students.get)
print(top)
bottom = min(students, key=students.get)
print(bottom)
