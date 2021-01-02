import turtle as tr

def get_ID (ID):
    """
    input: "name, family, age, birth place"
    output: ["setayesh", "pasandideh", 13, "tehran"]
    """
    ID = ID.split()
    ID[2] = int(ID[2])
    return ID

s = input("Enter your name, family, age, and birth place: ")

for i in range(4):
    tr.fd(190)
    tr.lt(90)

y = 150
for title, text in zip(['name', "family", "age", "b-p"], get_ID(s)):
    tr.penup()
    tr.goto(10, y)
    tr.pendown()
    tr.write(f"{title}: {text}")
    y -= 40

tr.done()