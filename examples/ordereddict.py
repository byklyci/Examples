# from collections import OrderedDict
#
# dict1 = {"name": "ali","age": 21, "national": "turk"}
#
# print("ordinary dict")
#
# for k,v in dict1.items():
#     print(k,v)
#
# ordered_dict = OrderedDict()
#
# ordered_dict['name'] = "veli"
# ordered_dict['age'] = 20
# ordered_dict['national'] = "bulgaria"
#
# print('ordered ordered')
#
# for k,v in ordered_dict.items():
#     print(k,v)
#
# d = {'banana':3, 'apple':4, 'pear':1, 'orange':2}
#
# print(OrderedDict(sorted(d.items(),key=lambda t:t[0])))
#
# class LastUpdatedOrderedDict(OrderedDict):
#     'Store items in the order the keys were last added'
#
#     def __setitem__(self, key, value):
#         if key in self:
#             del self[key]
#         print(OrderedDict.__setitem__(self, key, value))
#
# LastUpdatedOrderedDict(d)

from collections import deque
dict2 = {"name": "ali","age": 21, "national": "turk"}
dict1 = {"none": "ney","kep":"now"}
my_list = set(['ali','veli','selami','ysf'])
deq1 = deque()
deq2 = deque()
deq3 = deque(maxlen=3)
#dict2.update(dict1)
my_list.union(dict1)
def my_deque():
         deq1.append(dict2.keys())
         deq2.append(dict2.values())
         deq3.append(my_list)

my_deque()

deq1.appendleft('school')
deq2.appendleft('bogazici')
deq3.appendleft('aliye')

deq1.pop()
deq2.rotate()
deq1.popleft()
deq2.clear()
deq1.extend('name school')

print(list(deq2))
print(list(deq1))


from collections import defaultdict

s = [('yellow',1),('blue',1),('red',3),('yellow',4),('blue',4)]
d = defaultdict(list)

for k,v in s:
    d[k].append(v)

print(d.items())

from collections import namedtuple

Boat = namedtuple('Boat',['name','type','made_year'])
boat1 = Boat('delphia24','race',2004)

print('name:',boat1.name)


