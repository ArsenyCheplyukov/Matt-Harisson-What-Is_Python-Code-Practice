list_of_hours = [6, 2, 7, 8, 5, 6, 5, 7, 1, 8, 5]
lenght_of_list = len(list_of_hours)
number_sum = 0
for member in list_of_hours:
    number_sum+=member
mid_hour = number_sum/lenght_of_list
print("The middle hour of sleep is: ", mid_hour)