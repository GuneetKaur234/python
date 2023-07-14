weight = input("enter your weight in kg's = ")
height = input("enter your height in m = ")

Bmi = round(int(weight) / (float(height) **2))

if Bmi < 18:
    print(f"Your BMI is {Bmi} . You are underweight")

elif Bmi < 25:
    print(f"Your BMI is {Bmi} . You are normal weight")

else :
    print(f"Your BMI is {Bmi} . You are overweight")