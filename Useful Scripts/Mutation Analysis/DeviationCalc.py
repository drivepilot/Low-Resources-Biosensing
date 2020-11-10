#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 00:46:27 2020

@author: martincodyre
"""

#%matplotlib inline
import matplotlib.pyplot as plt

sumDiff = 0
b=0
variation = []
counter = 0

with open("nc_count.txt", 'r') as infile:
    line = infile.readline()
    line = infile.readline().split('\n')[0]
    while line:
        
        line = line.split('\t')
        line = line[1:6]
        
        for i in range(0,5):
            
            if float(line[i]) > b:
                sumDiff = sumDiff + b 
                b = float(line[i])

            else:
                sumDiff = sumDiff + float(line[i])
        
        b = 0
        variation.append(sumDiff)
        sumDiff = 0
        line = infile.readline().split('\n')[0]
        counter = counter + 1
        

counter = 0
plt.plot(variation,'.')
plt.savefig('Variation.eps',format='eps')

with open("Variation.txt", 'w') as outfile:
    for i in variation:
        outfile.write(str(counter+1)+"\t"+str(i)+"\n")
        counter = counter + 1