import re
inp = 17
old = inp >= 18
print(old)

name = "ARSENY"
half_of_alfabet = r"[m-z]"
second_half = bool(re.match(name[0].lower(), half_of_alfabet)) 
print(second_half)

names = []
if names:
    print('Class has enrollments.')
else:
    print('The class is empty!')

car = None
if car:
    print('You have a car!')
else:
    print('Taxi for you!')

