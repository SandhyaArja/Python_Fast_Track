class EvenNumberError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "Even numbers are not allowed"
        super().__init__(self.message)

def check_odd_number(number):
    if number % 2 == 0:
        raise EvenNumberError(number)
    return "Number is odd"

try:
    num = int(input("Enter a number: "))
    result = check_odd_number(num)
    print(result)
except EvenNumberError as e:
    print("Error:", e)
except ValueError:
    print("Invalid input. Please enter a valid number.")

