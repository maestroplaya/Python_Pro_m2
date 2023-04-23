class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Удаление экземпляра {id(self)}')


my_point = Point(1, 2)
print(id(my_point))
my_point = Point(3, 5)
print(id(my_point))