M = float(input('What is your mass?'))
H = float(input('What is your height?'))
BMI = M / (H * H)

print(f"Your Body Mass Index is: {BMI:.2f}")
if BMI < 18.6:
    print("you are under weight")
elif 18.5 < BMI and BMI < 25:
    print('your are normal')
elif  25 < BMI and BMI < 30:
    print('your are overwieght')
elif 30 < BMI and BMI < 35:
    print('you are obese')
elif BMI > 35:
    print('you are extremely obese')
