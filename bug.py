def calculate_average(numbers):
    if not numbers: 
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage (demonstrates the bug):
my_list = []
result = calculate_average(my_list)
print(f"Average: {result}")  # Correctly handles empty list

my_list = [10, 20, 30]
result = calculate_average(my_list)
print(f"Average: {result}")  # Correct average

my_list = [10, 20, 'a']
result = calculate_average(my_list) #Bug: this will throw TypeError
print(f"Average: {result}")