def get_details(string):
    """
    input: "sina bakhshandeh 17"
    output: ["sina" , "bakhshandeh", 17]
    """
    string = string.split()
    string[2] = int(string[2])
    return string

i = input('Enter Name Family Age respectly: ')
name, family, age = get_details(i)
print(name)
print(family)
print(age)