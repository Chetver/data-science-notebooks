# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:13:50 2019

@author: andrew.graham
"""
import numpy as np
# NumPy object creation
# The calculations using NumPy are performed using nd-array object
# which can take any number of dimensions.
# Most commonly used NumPy nd-array is a matrix which takes 2 dimensions.
#
# Array Creation
# A NumPy nd-array inputs a basic Python list as an argument along 
# with an explicit datatype (for typecasting) as shown below:
 
arr = np.array([2,5,6,8], dtype = int)
print(arr)
# [2 5 6 8]
print(type(arr))
# class 'numpy.ndarray'
print(np.result_type(arr))
# int32 
 
# Here, we have used np.array() function which takes 2 arguments,
# the input list, and the corresponding data type (dtype). 
# To check the data type of a particular NumPy object we have used np.result_type() command.
#
# Most of the time, it is not an intuitive way to pass a list of predefined components. 
# Therefore, NumPy offers some frequently used functions to create a NumPy object as shown below:
 
''' Creation of an array with step size 1.33 between 0 - 10 '''
print(np.arange(0, 10, 1.33, dtype = np.float64))
# [ 0.    1.33  2.66  3.99  5.32  6.65  7.98  9.31]
# arange() gives uncertain number of values based on steps
# Hence, we use linspace, which asks for total number of values 
''' Creation of an array with total 5 values between 0 - 160 '''
print(np.linspace(0, 160, 5, dtype = np.float64))
# [   0.   40.   80.  120.  160.] 


 

