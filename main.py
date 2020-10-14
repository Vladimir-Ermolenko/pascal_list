
class PascalList:

    def __init__(self, lst):
        self.lst = lst

    def __setitem__(self, key, value):
        self.lst[key - 1] = value

    def __getitem__(self, item):
        if item != 0:
            return self.lst[item - 1]
        else:
            return 'This list starts from 1'

    def __str__(self):
        return str(self.lst)
