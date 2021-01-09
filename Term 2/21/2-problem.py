def get_info():
    text = input('Enter your information:("name family age")\n')
    return text.split()
    

info = get_info()

template = f"""Name: {info[0]}
Name: {info[0].title()}
Last : {info[1].upper()}
Age : {info[2]}
********************
file = open('names.txt', 'a')
file.write(template)
file.close()