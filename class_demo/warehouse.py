import os
import glob
import sys


class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
w2 = Warehouse()
w2.region = 'east'

print(w1.purpose, w1.region)

print(w2.purpose, w2.region)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add_twice(self, x):
        self.add(x)
        self.add(x)


bag = Bag()
bag.add(1)
bag.add_twice(2)

print(bag.data)

# help(os)
print(glob.glob('*.py'))
print(sys.argv)
