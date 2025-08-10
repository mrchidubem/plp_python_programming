# Make empty list
my_list = []

# Add 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Put 15 in second spot
my_list.insert(1, 15)

# Add 50, 60, 70
my_list.extend([50, 60, 70])

# Remove last item
my_list.pop()

# Sort list
my_list.sort()

# Find 30's index
print(f"30 is at index {my_list.index(30)}")