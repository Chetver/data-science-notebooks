# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:14:20 2019

@author: andrew.graham
"""
import numpy as np
arr1 = np.array([25, 56, 12, 85, 34, 75],dtype=complex)
arr2 = np.array([42, 3, 86, 32, 856, 46],dtype=complex)
narr = np.linspace(0,(np.random.rand()),6, dtype = complex)


arr1_mat=arr1.reshape(2,3)
arr2_mat=arr2.reshape(2,3)

arr2sq=np.square(arr2_mat)
arr1sq=np.square(arr1_mat)

top=arr1sq-arr2sq
bottom=arr1_mat-arr2_mat
narr=np.true_divide(top,bottom)
print(narr)

