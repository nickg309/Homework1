# -*- coding: utf-8 -*-
"""
@author: Nicholas Gallagher
First Assignment: Find the Sum of First 100
Aug 15 20:06:05 2022
"""

import numpy as np

list100 = np.linspace(1, 100, 100)
sum100 = sum(list100).astype(int)
print('Sum of the first hundred numbers using a list and sum() is: {}'.format(sum100))

otherSum = 0

for i in range(101):
    otherSum += i

print('Sum of the first hundred numbers using a for loop and range() :{}'.format(otherSum))