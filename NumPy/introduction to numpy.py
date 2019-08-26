# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:01:33 2019

@author: andrew.graham
"""

print("Problem statement 1:\nGiven a list lst perform elementwise addition with 5.")
lst = [5, 10, 0, 200] 
import numpy as np
arr = np.array(lst)
print(arr + 5)
# Output:
# [10, 15, 5, 205] 
 
print("Problem Statement 2:\nGiven a list lst do a homogeneity test on each element.")
lst = [1, 2, 3, 'text', True, 3+2j] 
import numpy as np
arr = np.array(lst)
print(type(arr[0]),type(arr[4]), type(arr[5]))
# Output:
# <class 'numpy.str_'> <class 'numpy.str_'> <class 'numpy.str_'> 
 
print("Problem statement 3:\nGiven a list lst find its complete size in bytes. Hint: use sys.getsizeof(lst)")
lst = [56, 45, 12, 6]
import numpy as np
arr = np.array(lst)
print(arr.nbytes)
# Output:
# 16 
