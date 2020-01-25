# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:16:53 2019

@author: sri
"""

a = [1, 3, 5, 30, 42, 43, 500]

q=int(input('Which number do you want to look for?'))
 
while a != []:

    #print(a)

    mid=int(len(a)/2)

    #print(a[mid])

    if q==a[mid]:

        print('The list contains %d.' % q)

        quit()

        

    elif q>a[mid]:

        #print('higher')

        del a[:mid+1]

 

    elif q<a[mid]:

        #print('lower')

        del a[mid:]

 

   
#print(a)

 

print('''The list doesn't contain %d.''' % q)