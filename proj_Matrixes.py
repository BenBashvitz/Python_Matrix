# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

def MyMatMul(a, b):
    #הפעולה מקבלת שתי מטריצות שבנויות כך שמספר העמודות במטריצה הראשונה הוא מספר השורות במטריצה השנייה
    c = np.zeros((np.shape(a)[0],np.shape(b)[1]))
    for i in range(np.shape(a)[0]):
        for j in range(np.shape(b)[1]):
            for k in range(np.shape(a)[1]):
                c[i,j] += a[i,k]*b[k,j]
    return c

def AddMinMat(a, b):
    minA = min(np.shape(a)[0],np.shape(a)[1])
    minB = min(np.shape(b)[0],np.shape(b)[1])
    c = np.zeros((minA, minB))
    for i in range(minA):
        for j in range(minB):
            c[i,j] = a[i,j] + b[i,j]
    return c

def AddMaxMat(a, b):
    maxA = max(np.shape(a)[0],np.shape(a)[1])
    maxB = max(np.shape(b)[0],np.shape(b)[1])
    minA = min(np.shape(a)[0],np.shape(a)[1])
    minB = min(np.shape(b)[0],np.shape(b)[1])
    c = np.zeros((maxA, maxB))
    for i in range(maxA):
        for j in range(maxB):
            if i < minA and j < minB:
                c[i,j] = a[i,j] + b[i,j]
    return c
            
def main():
    a = np.array([[1,2,3],[4,5,6]])
    b = np.array([[7,8,7,8],[9,1,9,1],[2,3,2,3]])
    c = AddMinMat(a, b)
    d = AddMaxMat(a, b)
    e = MyMatMul(a, b)
    print(c)
    print(d)
    print(e)
    
if __name__ == "__main__":
    main()
