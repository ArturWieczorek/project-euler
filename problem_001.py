total_sum = 0

for n in range(1000):
    if (n % 3 == 0 or n % 5 ==0):
        total_sum += n

print(f"Sum is: {total_sum }")


# Using Python's sum built in function

result = sum(n for n in range(1000) if n % 3 == 0 or n % 5 ==0)

print(f"Sum (using different method) is: {result}")
