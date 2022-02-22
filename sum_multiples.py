# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:24:51 2022

@author: Dell
"""


#sum of multiples of 3 and 5 below 1000

x = sum(i for i in range(1000) if i % 3 == 0 and i % 5 == 0)
print(x)

#I decided to experiment with the sum of multiples of 2 and 5
y = sum(i for i in range(1000) if i % 2 == 0 and i % 5 ==0)
print(y)

#sum of numbers that are multiples of 3 or 6
y = sum(i for i in range(1000) if i % 3 == 0 or i % 6 == 0)
print(y)