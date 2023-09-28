def is_odd(number):
    """
    Function that checks if this number is odd
    """
    return True if number % 2 else False

def is_prime(number):
    """
    Cheks if this number is prime
    """
    if number > 3:
        for digit in range(2, number):
            if number % digit:
                return False
        return True
    elif number < 0:
        return False
    else:
        return True

def binary_search(some_list, element):
    """
    try to find some element in list
    """
    position = int(len(some_list) / 2)
    step = position
    while step != 0:
        if element == some_list[position-1]:
            return position
        elif element > some_list[position-1]:
            step = int(step/2)
            position+=step
        else:
            step = int(step/2)
            position-=step
    return -1

def translate_into_register(some_string, delemiter):
    """
    remake string into some register
    """
    big_letters_list = []
    for letter in some_string:
        if letter.isupper():
            big_letters_list.append(letter)
    new_string = '{}'.format(some_string)
    for letter in big_letters_list:
        new_string = new_string.replace(letter, '{1}{0}'.format(letter.lower(), delemiter))
    return new_string

print(is_odd(2))
print(is_odd(3))
print(is_prime(2))
print(is_prime(4))
some_list = [1,3,5,7,9,11,13,15,17]
print(binary_search(some_list, 5))
print(translate_into_register("thisIsCamelCased", '_'))