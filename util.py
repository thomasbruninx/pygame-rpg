from csv import reader


def read_csv_as_array(filename, delimiter=','):
    arr_data = []
    with open(filename) as csv_file:
        csv_data = reader(csv_file, delimiter=delimiter)
        for row in csv_data:
            arr_data.append(list(row))
        return arr_data


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
