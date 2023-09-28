inp = float(input("Enter some number\n"))
print("The identifier of this number is: ", id(inp))
inp += 20
print("The new identifier is: ", id(inp))
# Conclusion is that identifiers of old and updated number is not equal