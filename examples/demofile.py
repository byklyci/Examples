import time
import random

from datetime import datetime
odds = [ 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,51,53,57,59 ]
for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("this is odd")
    else:
        print("not odd time ")
    #wait_time = random.randint(1,2)
    #time.sleep(wait_time)

#######################################################
time_now = datetime.today()
right_this_minute1 = time_now.minute
print(right_this_minute1)

#######################################################

vowels = ['a','e','i','o','u']
#word = input("provide a new word to search vowels:")
word = 'aliveli'
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
#########################################################
nums = [1,2,3,4,5]
nums.remove(3)
nums.pop(1)
nums.extend([6,7,8])
nums.insert(1,[2,3])
print(nums)

############################################################

phrase = "dont panic!"
plist = list(phrase)
print(phrase)
print(plist)
print(plist[0:10:3])
new_phrase = ''.join(plist[0:4])
print(new_phrase)

for i in range(4):
    plist.pop()
    print(plist)
plist.remove("d")
print(plist)
print(plist[1])

################################################
first =[1,2,3,4,5,]
second = first
print(second)
second.append(6)
print(first , second)
third = second.copy()
second.extend([7,8])
print(third)

###################################################
yusuf_kalaycı = "yusuf, kalaycı"
letters = list(yusuf_kalaycı)
for char in letters[:5]:
    print('\t', char)
print()
for char in letters[7:]:
    print('\t'*2,char)
print()
##################################################
import pprint
pprint.pprint(letters)
##################################################

# def search4vowels():
#     vowel1 = set('aeiou')
#      word1 = input("provide a word : ")
#     found1 = vowel1.intersection(set(word1))
#     for vowel1 in found1:
#         print(vowel1)
# search4vowels()

######################################################
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info('Math','Art',name='john',age=22)

def student_info1(*args,**kwargs):
    print(args)
    print(kwargs)
courses = ['Math', 'Art']
info = {'name': 'john', 'age': 22}
student_info1(*courses,**info)

#####################################################

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """REturn true for leap or not true for nonleap"""
    return year %4 ==0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
print(is_leap(2017),days_in_month(2017,2))
print(is_leap(2020),days_in_month(2020,2))

##############################################################

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return 'hello flask'
#app.run()

###########################################################

tasks = open('a.txt')
for chore in tasks:
    print(chore)
tasks.close()

with open('a.txt') as tasks1:
    for c in tasks1:
        print(c,end='')

##################################################################

class Dog:
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age

philo = Dog("Philo",5)
mike = Dog("Mickey",6)

print("{} is {} and {} is {}.".format(philo.name,philo.age,mike.name,mike.age))
if philo.species == 'mammal':
    print("{} is {}".format(philo.name,philo.species))

##############################################################

class Sailing:
    boat= 'race_boats'
    def __init__(self,type,ırc):
        self.type = type
        self.ırc = ırc
    def definition(self):
        return "the {} is the ırc {} class".format(self.type,self.ırc)

    def abilities(self):
        if self.ırc >= 3:
            return "the {} has symetric  ".format(self.type)
        else:
            return "the {} has assymetric ".format(self.type)

class Made_of(Sailing):
    def made(self,material):
        return "{} is mades {} ".format(self.type,material)
j24 = Sailing("j24",4)
j70 = Sailing("j70",2)
j40 = Made_of("j40",4)
print(j24.definition())
print(j24.abilities())
print(j70.definition())
print(j70.abilities())
print(j40.made("wood"))
print(isinstance(made,Sailing))


##########################################################