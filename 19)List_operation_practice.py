def is_palindrome(word):
    """
    This function checks if this word edual if we read it from left and right
    """
    return word == word[::-1]

name = 'Arseny'
print("First symbol is: ", name[0], " last symbol is: ", name[-1])

filename = 'README.txt'
print("File type is: ", filename[-3:])

print(is_palindrome("ABBA"))
