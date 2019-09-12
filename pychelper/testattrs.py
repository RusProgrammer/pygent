from random import randrange, uniform


class TestAtrs:

    Checks = []
    Predicts = []

    def __init__(self):
        pass

    def add_check(self, item):
        self.Checks.append(item)

    def get_random(self, val_type, items=[]):
        if val_type == 'string':
            return 'NULL'
        elif val_type == 'int':
            return str(randrange(10000))
        elif val_type == 'float':
            return str(uniform(0.0, 100000.9))
        elif val_type == 'double':
            return str(uniform(0.0, 100000.9))
        else:
            raise Exception(f'Unknown type for random : {val_type}')
