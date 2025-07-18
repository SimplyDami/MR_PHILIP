# A simple arithmetic program for kids!

print("Hello! Let's do some math!")

# Get the first number from the user
# int() converts the text input into a whole number
num1_str = input("Please enter your first whole number: ")
num1 = int(num1_str)

# Get the second number from the user
num2_str = input("Please enter your second whole number: ")
num2 = int(num2_str)

# Add the two numbers together
sum_result = num1 + num2

# Print the result in a friendly way
print(f"Great job! {num1} plus {num2} is equal to {sum_result}.")
print("You're a math superstar!")