def calculator(some_list):
    try:
        number_1 = int(some_list[0])
        number_2 = int(some_list[1])
        operator = some_list[2]
        if operator == '+':
            print(number_1 + number_2)
        elif operator == '-':
            print(number_1 - number_2)
        elif operator == '*':
            print(number_1 * number_2)
        elif operator == '/':
            print(number_1 / number_2)
    except ZeroDivisionError as ex:
        print("Zero division error")
    except Exception:
        print("something else goes wrong")

list_of_used = list(input("Write numbers one and two and write operator in the end\n").split())
print(calculator(list_of_used))