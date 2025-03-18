def check_number_size(number):
    if number < 100:
        return "Small number"
    else:
        return "Large number"

# Input from the user
num = float(input("Enter a number: "))

# Output the result
print(check_number_size(num))
