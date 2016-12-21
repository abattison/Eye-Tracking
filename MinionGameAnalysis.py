#
####Program Information:
# calculates correction factors for the minion game
# Alix Battison, July 2016 alexandria.battison@uconn.edu
#

import csv
from collections import defaultdict
import numpy as np
import operator
import functools
from operator import sub
import sys

#############################################
#############################################

### EDIT THESE PARAMETERS
#
### EXPECTED COORDINATES
#
leftMinionX = 0.25
centerMinionX = 0.5
rightMinionX = 0.75

minionY = 0.5

#
#
#

#############################################
#############################################

xCF = list()
yCF = list()

#############################################
#
## CHANGE FILENAME HERE 
#
#############################################
columns = defaultdict(list) 

with open('progamtesting.csv') as f:  #CHANGE THIS LINE INCLUDE YOUR FILENAME
        reader = csv.reader(f)
        reader.next()

        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)



##### LEFT MINION X ANALYSIS ####
if leftMinionX != 0:     
    print(columns[3])
    leftX = columns[3]
    print(leftX)
    leftX = [float(i) for i in leftX]
    print(leftX)
    for k in range(len(leftX)):
        leftX[k] -= leftMinionX
    #print(FPOGX_lefttop)
    leftX = map(abs, leftX)
    print(leftX)
    lengthleftX = len(leftX)
    print(lengthleftX)
    Xleft_CF = (sum(leftX))/lengthleftX
    print(Xleft_CF)

xCF.append(Xleft_CF)

##### CENTER MINION X ANALYSIS ####
if centerMinionX != 0:     
    print(columns[11])
    centerX = columns[11]
    print(centerX)
    centerX = [float(i) for i in centerX]
    print(centerX)
    for k in range(len(centerX)):
        centerX[k] -= centerMinionX
    #print(FPOGX_lefttop)
    centerX = map(abs, centerX)
    print(centerX)
    lengthcenterX = len(centerX)
    print(lengthcenterX)
    Xcenter_CF = (sum(centerX))/lengthcenterX
    print(Xcenter_CF)

xCF.append(Xcenter_CF)


##### RIGHT MINION X ANALYSIS ####
if rightMinionX != 0:     
    print(columns[19])
    rightX = columns[19]
    print(rightX)
    rightX = [float(i) for i in rightX]
    print(rightX)
    for k in range(len(rightX)):
        rightX[k] -= rightMinionX
    #print(FPOGX_lefttop)
    rightX = map(abs, rightX)
    print(rightX)
    lengthrightX = len(rightX)
    print(lengthrightX)
    Xright_CF = (sum(rightX))/lengthrightX
    print(Xright_CF)

xCF.append(Xright_CF)

##### LEFT MINION Y ANALYSIS ####
if minionY != 0:     
    print(columns[4])
    leftY = columns[4]
    print(leftY)
    leftY = [float(i) for i in leftY]
    print(leftY)
    for k in range(len(leftY)):
        leftY[k] -= minionY
    #print(FPOGX_lefttop)
    leftY = map(abs, leftY)
    print(leftY)
    lengthleftY = len(leftY)
    print(lengthleftY)
    Yleft_CF = (sum(leftY))/lengthleftY
    print(Yleft_CF)

yCF.append(Yleft_CF)

##### CENTER MINION Y ANALYSIS ####
if minionY != 0:     
    print(columns[12])
    centerY = columns[12]
    print(centerY)
    centerY = [float(i) for i in centerY]
    print(centerY)
    for k in range(len(centerY)):
        centerY[k] -= minionY
    #print(FPOGX_lefttop)
    centerY = map(abs, centerY)
    print(centerY)
    lengthcenterY = len(centerY)
    print(lengthcenterY)
    Ycenter_CF = (sum(centerY))/lengthcenterY
    print(Ycenter_CF)

yCF.append(Ycenter_CF)

##### RIGHT MINION Y ANALYSIS ####
if minionY != 0:     
    print(columns[20])
    rightY = columns[20]
    print(rightY)
    rightY = [float(i) for i in rightY]
    print(rightY)
    for k in range(len(rightY)):
        rightY[k] -= minionY
    #print(FPOGX_lefttop)
    rightY = map(abs, rightY)
    print(rightY)
    lengthrightY = len(rightY)
    print(lengthrightY)
    Yright_CF = (sum(rightY))/lengthrightY
    print(Yright_CF)

yCF.append(Yright_CF)

####calculating x and y correction factors ###


    
    

##### exporting to csv ###
header = ['Left X', 'Left Y', 'Center X', 'Center Y', 'Right X', 'Right Y']
data4csv = [Xleft_CF, Yleft_CF, Xcenter_CF, Ycenter_CF, Xright_CF, Yright_CF]
with open('MinionGamecorrectionfactors.csv', 'w') as csvfile:
    csvfile = csv.writer(csvfile, delimiter=',')
    csvfile.writerow(header)
    csvfile.writerow(data4csv)


