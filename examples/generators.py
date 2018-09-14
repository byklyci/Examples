
a_set = {1, 2, 3}
b_iterator = iter(a_set)
next(b_iterator)

print(type(a_set))
print(type(b_iterator))

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
population = people.union(vampires)
victims = people.intersection(vampires)


class Series(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

n_list = Series(5,10)
a_list = Series(1,4)
print(list(n_list))


def series_generator(low,high):
    while low <= high:
        yield low
        low += 1

m_list = []

for num in series_generator(1,5):
    m_list.append(num)
print(m_list)

import itertools
a = []
b = list(itertools.chain(n_list,a_list))
a.append(b)
print(a)

def range(n):
    i = 0
    while i < n:
        yield i
        i += 1

y = range(3)
for items in y:
    print(items)

m = list([1,2,3])
n = m
id(n) == id(m)
m.pop()
id(n) == id(m)
