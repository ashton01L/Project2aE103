# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/4/2024
# Description: Asks the user for five numbers and then prints out the average of those numbers.

def average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

print("Please enter five numbers.")
numbers = []
for i in range(5):
    while True:
        try:
            num = float(input())
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

result = average(numbers)
print("The average of those numbers is:")
print(result)
