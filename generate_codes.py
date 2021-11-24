import random, string

foo = []

for i in range(int(input("Enter amount of codes: "))):
    foo.append(''.join(random.choice(string.digits + string.ascii_lowercase) for i in range(5)))


with open("codes.csv", "w") as bar:
    bar.write(",".join(foo))

with open("keep_codes.txt", "w") as bar:
    bar.write("[ ] " + "\n[ ] ".join(foo))
