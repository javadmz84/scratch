def get_bigger(number1, number2):
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    else:
        print('Numbers are Equal')
        return number1

n1 = int(input("Enter your number1: "))
n2 = int(input('ENter your number2: '))

bigger_one = get_bigger(n1, n2)
print(f'The bigger of {n1} & {n2} is: {bigger_one}')