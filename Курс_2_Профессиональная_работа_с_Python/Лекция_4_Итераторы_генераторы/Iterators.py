#Как я постарался понять
#Когда Python обрабатывает объект (словарь, список, строка) он добавляет ему еще объект или уже содержит в себе объект с названием итератор 
#Этот Итератор имеет два метода(функции) iter() и next() вызвать их можно на этот словарь-список по примеру ниже 
#Можно создавать свои итераторы и добавлять их в другие объекты 

num_list = ['один', 'два', 'три']
for x in num_list:
    print(x)

itr = iter(num_list)

print()
print(next(itr))
print(next(itr))
print(next(itr))
print()

class SimpleIterator:

    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter2 = SimpleIterator(5)
for x in s_iter2:
    print(x)


