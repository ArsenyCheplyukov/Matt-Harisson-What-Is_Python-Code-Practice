import os

def writing_in_csv(data, file_name):
    """
    writes list of tuples in csv file
    """
    with open('{0}{1}'.format(file_name, '.csv'), 'w') as fout:
        for row in data:
            for column in row: 
                fout.write('{0}{1}'.format(column, ','))
            fout.write(os.linesep)

def reading_from_csv(file_name):
    """
    read array of list and converts it into list of dictionaries
    """
    out_list = []
    with open('{0}{1}'.format(file_name, '.csv'), 'r') as fout:
        for row in fout:
            if len(row) > 1:
                some_list = row.split(',')
                some_dict = dict([('name', some_list[0]), ('address',some_list[1]), ('age',int(some_list[2]))])
                out_list.append(some_dict)
    return out_list

some_data = [('George', '4312 Abbey Road', 22),
            ('John', '54 Love Ave', 21)]
writing_in_csv(some_data, "Output")
another_data = reading_from_csv("Output")
print(another_data)