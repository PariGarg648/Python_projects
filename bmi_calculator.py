# Function to get positive float input
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Taking input
height = get_positive_float("Enter your height in meters: ")
weight = get_positive_float("Enter your weight in kilograms: ")

# BMI calculation
bmi = weight / (height ** 2)
print(f"\nYour BMI is: {bmi:.2f}")

# BMI categories
if bmi <= 16:
    print("You are very underweight.")
elif bmi <= 18.5:
    print("You are underweight.")
elif bmi <= 25:
    print("Congrats! You are healthy.")
elif bmi <= 30:
    print("You are overweight.")
else:
    print(" You are very overweight.")

# Suggestion based on BMI
print("\nHealth Tip:")
if bmi < 18.5:
    print("Try to eat a balanced diet and include more calories.")
elif bmi <= 25:
    print("Maintain your healthy lifestyle! Keep it up.")
else:
    print("Consider regular exercise and a balanced diet.")

print("-" * 40)
print("Thank you for using the BMI Calculator!")
