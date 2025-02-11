def calculate_average(numbers):
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")
    return sum(numbers) / len(numbers)

#Example Usage:
my_list = []
result = calculate_average(my_list)
print(f"Average: {result}")

my_list = [10, 20, 30]
result = calculate_average(my_list)
print(f"Average: {result}")

my_list = [10, 20, 'a']
#This line will throw ValueError as expected
try:
    result = calculate_average(my_list)
    print(f"Average: {result}")
except ValueError as e:
    print(f"Error: {e}")
