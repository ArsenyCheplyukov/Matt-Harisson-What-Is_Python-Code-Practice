                                                                #
friend_list = ['Roman', 'Danill', 'Krill', 'Sergey', 'Oleg']
mid_len = 0
for name in friend_list:
    mid_len += len(name)
else:
    mid_len /= len(friend_list)
print(int(mid_len))

for name in friend_list:
    if name == 'John':
        break
else:
    print("there is no such name")

people = [('Roman', 'Kazakov', 19), ('Sergey', 'Zverugo', 18), ('Maksim', None, None), ('Vlad', None, None)]
mid_age = 0
counter = 0
for human in people:
    value = human[2] 
    if value is not None:
        mid_age += value
        counter+=1
else:
    mid_age /= counter
    for human in people:
        value = human[2]
        if value and value > mid_age:
            print(human[0])
    for human in people:
        value = human[2]
        if value and value <= mid_age:
            print(human[0])


