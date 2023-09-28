inp = float(input("Enter some number\n"))
some_list = []
print("The identifier of this number is: ", id(some_list))
some_list.append(inp)
print("The new identifier is: ", id(some_list))
# Conclusion is that identifiers of list is equal