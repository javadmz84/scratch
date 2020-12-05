number = input("Enter your number: ")
counter = 0
numbers = []
s = 0
while number != '0':
    if number.isdigit():
        numbers.append(number)
        counter += 1
    number = input("Enter your number:")
for n in numbers:
     s = s + int(n)
print(numbers)
print(s)
print(f"you entered{counter}number.")