from csv import reader


def read_csv_as_array(filename, delimiter=','):
    arr_data = []
    with open(filename) as csv_file:
        csv_data = reader(csv_file, delimiter=delimiter)
        for row in csv_data:
            arr_data.append(list(row))
        return arr_data
