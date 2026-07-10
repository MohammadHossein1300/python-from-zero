# Example 1
# Print a square

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

print("-" * 20)

# Example 2
# Print a triangle

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("-" * 20)

# Example 3
# Print increasing numbers

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("-" * 20)

# Example 4
# Print decreasing numbers

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()