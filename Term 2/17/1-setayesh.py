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
name, family, age, b_p = get_ID(s)


for i in range(4):
    tr.fd(190)
    tr.lt(90)

tr.penup()
tr.goto(10, 150)
tr.pendown()
tr.write(f"name: {name}")

tr.penup()
tr.goto(10, 110)
tr.pendown()
tr.write(f"family: {family}")

tr.penup()
tr.goto(10, 70)
tr.pendown()
tr.write(f"age: {age}")

tr.penup()
tr.goto(10, 30)
tr.pendown()
tr.write(f"birth place: {b_p}")

tr.done()