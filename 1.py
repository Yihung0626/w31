# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:29:12 2024

@author: student
"""

import random

n = int(input("n: "))
a = int(input("a: "))
b = int(input("b: "))

random_choose_list = []

while len(random_choose_list) < n:
    x = random.randint(a, b)
    random_choose_list.append(x)
    
random_choose_list = set(random_choose_list)
random_choose_list = list(random_choose_list)
random_choose_list.sort()

print(random_choose_list)