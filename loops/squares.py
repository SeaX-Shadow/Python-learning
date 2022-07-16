#squares = []
#for value in range(1,11):
#	squares.append(value ** 2)
#print(squares)

# List Comprehensions
squares = [value ** 2 for value in range(1,11)]
print(squares)
# 1) We make a list, inside the [] we put the expression we want inside the list (value ** 2), we make the *for loop, it doesn't need :