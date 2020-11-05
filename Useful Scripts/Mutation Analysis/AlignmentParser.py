#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 00:06:46 2020

@author: martincodyre
"""

import numpy as np
from IPython.display import clear_output

degeneratedNucleotides = True #Change for counting degenerated nucleotides or not

aCounter = 0
tCounter = 0
gCounter = 0
cCounter = 0
pCounter = 0
counter = 0
seq = 0
nset = 0
 
def countNucleotide(c):
    
    global aCounter
    global tCounter
    global gCounter
    global cCounter
    global pCounter
    
    if c == "a":
        aCounter = aCounter + 1
    elif c == "t":
        tCounter = tCounter + 1
    elif c == "g":
        gCounter = gCounter + 1
    elif c == "c":
        cCounter = cCounter + 1
    elif c == "-":
        pCounter = pCounter + 1
    elif degeneratedNucleotides:
        if c == "r":
            aCounter = aCounter + 0.5
            gCounter = gCounter + 0.5
        elif c == "y":
            cCounter = cCounter + 0.5
            tCounter = tCounter + 0.5
        elif c == "s":
            cCounter = cCounter + 0.5
            gCounter = gCounter + 0.5
        elif c == "w":
            aCounter = aCounter + 0.5
            tCounter = tCounter + 0.5
        elif c == "k":
            tCounter = tCounter + 0.5
            gCounter = gCounter + 0.5
        elif c == "m":
            cCounter = cCounter + 0.5
            aCounter = aCounter + 0.5
        elif c == "b":
            cCounter = cCounter + 0.33
            gCounter = gCounter + 0.33
            tCounter = tCounter + 0.33
        elif c == "d":
            aCounter = aCounter + 0.33
            gCounter = gCounter + 0.33
            tCounter = tCounter + 0.33
        elif c == "h":
            cCounter = cCounter + 0.33
            aCounter = aCounter + 0.33
            tCounter = tCounter + 0.33
        elif c == "v":
            cCounter = cCounter + 0.33
            gCounter = gCounter + 0.33
            aCounter = aCounter + 0.33
        else:
            aCounter = aCounter + 0.25
            tCounter = tCounter + 0.25
            cCounter = cCounter + 0.25
            gCounter = gCounter + 0.25


def resetCounters():
    global aCounter
    global tCounter
    global gCounter
    global cCounter
    global pCounter
    
    aCounter = 0
    tCounter = 0
    gCounter = 0
    cCounter = 0
    pCounter = 0
    
    
    

with open("align.aln", 'r') as infile:
    for i in range(0,3):
        infile.readline()
        
    buff = infile.readline()
    fseq = buff.split(" ")[0] #first sequence

    
    with open("nc_count.txt", 'w') as outfile:
        outfile.write("Nt\tA\tT\tG\tC\t-\n")


        while buff:
            
            clear_output(wait=True)
            data = []
            
            while buff and buff != '\n': #reading the complete 60 nucleotides set alingment 
                #parsing just the sequence
                if len(buff.split(" ")) == 2:
                    buff = buff.split(" ")
                    buff = buff[len(buff)-1] 
                    data.append(buff)
                    
                buff = infile.readline()
                  
            buff = " "
            i = 0
            if data:
                #Iterating throw columns
                while buff != '\n': 
                    #Iterating throw rows
                    for j in data:
                        buff = j[i].lower()

                        if buff != '\n':
                            countNucleotide(buff)
                    if buff != '\n':
                        outfile.write(str(1+i+(nset*60)) + "\t" + str(aCounter) + "\t" + str(tCounter) + "\t" + str(gCounter) + "\t" + str(cCounter) + "\t" + str(pCounter) + "\n")
                    resetCounters()
                    i = i + 1


                nset = nset + 1
                print ("base pair:" + str(nset*60))
            
            while buff == '\n':
                buff = infile.readline()


#     print("A:" + str(aCounter) + " T:" + str(tCounter) + " G:" + str(gCounter) + " C:" + str(cCounter) + " -:" + str(pCounter))
#     print("\n "+ str(aCounter+tCounter+gCounter+cCounter+pCounter))