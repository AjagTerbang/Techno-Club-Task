# 1. create list into dictionary
list = [
    {
        "No": 1,
        "Nama": "Haikal",
        "Kelas": "IF21B"
    },
    {
        "No": 2,
        "Nama": "Mr. Santai",
        "Kelas": "IF21B"
    },
    {
        "No": 3,
        "Nama": "Kisah",
        "Kelas": "IF22C"
    },
    {
        "No": 4,
        "Nama": "Ajag",
        "Kelas": "IF23B"
    }]

for x in list:
    print("No: ", x["No"])
    print("Nama: ", x["Nama"])
    print("Kelas: ", x["Kelas"])
    print("=====================================")

#  Create output "Saya Teknik Informatika" 100x using while loop

i = 1
while(i <= 100):
    print(i, "Saya Teknik Informatika")
    i += 1

# create 3 example of logical operator
# and

a = 10
b = 20
if a > 5 and b > 10:
    print("a lebih dari 5 dan b lebih dari 10")
else:
    print("a kurang dari 5 atau b kurang dari 10")

# or
a = 10
b = 20
if a > 5 or b > 10:
    print("a lebih dari 5 atau b lebih dari 10")
else:
    print("a kurang dari 5 dan b kurang dari 10")

# not
a = 10
b = 20
if not a > 5:
    print("a kurang dari 5")
else:
    print("a lebih dari 5")

# create 3 example of comparison operator

# equal
a = 10
b = 20
if a == b:
    print("a sama dengan b")
else:
    print("a tidak sama dengan b")

# not equal
a = 10
b = 20
if a != b:
    print("a tidak sama dengan b")
else:
    print("a sama dengan b")


# greater than
a = 10
b = 20
if a > b:
    print("a lebih besar dari b")
else:
    print("a tidak lebih besar dari b")

#  1%2 equal
a = 1
b = 2
print("a + b: ", a%b)

# create 2 function with parameter and without parameter
def with_parameter(a, b):
    print(a + b)

with_parameter(10, 20)

def without_parameter():
    print("Hello World")

without_parameter()

