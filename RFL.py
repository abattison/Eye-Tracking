#
####Program Information:
# calculates correction factors for required fixation locations
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
# these are the expected vales for each square that you
# calculated based on PPI and screen resolution.
# Each coordinate is expresed as a percentage of total screen size
#
#                                           
xCenter = 0.5
yCenter = 0.5
xLT = .04
yLT = 0.078
xRT = .9558
yRT = .078
xBL = .04
yBL = .9215
xBR = .9558
yBR = .9215

cxXCenter = 0.5
cxYCenter = 0.5
cx1x = .4278
cx1y = .35032
cx2x = .60399
cx2y = .35032
cx3x = .60399
cx3y = .6688
cx4x = .42748
cx4y = .6688
cx5x = .34474
cx5y = .20592
cx6x = .6854
cx6y = .20592
cx7x = .6854
cx7y = .8237
cx8x = .34474
cx8y = .8237
#
#
#

#############################################
#############################################

xCF = list()
yCF = list()

#############################################
###### FOUR CORNERS CORRECTION FACTORS ######
#############################################


columns = defaultdict(list) # each value in each column is appended to a list
with open('progamtesting.csv') as f:  #CHANGE THIS BE YOUR FILENAME
        reader = csv.reader(f)
        reader.next()

        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)



##### CENTER X FIXATIONS ####
if xCenter != 0:     
    print(columns[3])
    FPOGX_center = columns[3]
    print(FPOGX_center)
    FPOGX_center = [float(i) for i in FPOGX_center]
    print(FPOGX_center)
    for k in range(len(FPOGX_center)):
        FPOGX_center[k] -= xCenter
    #print(FPOGX_lefttop)
    FPOGX_center = map(abs, FPOGX_center)
    print(FPOGX_center)
    lengthXcenter = len(FPOGX_center)
    print(lengthXcenter)
    Xcenter_CF = (sum(FPOGX_center))/lengthXcenter
    print(Xcenter_CF)


   

    center4CornersDuration = columns[6]
    center4CornersDuration = [float(i) for i in center4CornersDuration]
    center4CornersDuration = sum(center4CornersDuration)
    print(center4CornersDuration)
else:
    Xcenter_CF = 0
    print(Xcenter_CF)

xCF.append(Xcenter_CF)

##### CENTER Y FIXATIONS ####
if yCenter != 0:     
    print(columns[4])
    FPOGY_center = columns[4]
    print(FPOGY_center)
    FPOGY_center = [float(i) for i in FPOGY_center]
    print(FPOGY_center)
    for k in range(len(FPOGY_center)):
        FPOGY_center[k] -= yCenter
    #print(FPOGX_lefttop)
    FPOGY_center = map(abs, FPOGY_center)
    print(FPOGY_center)
    lengthYcenter = len(FPOGY_center)
    print(lengthYcenter)
    Ycenter_CF = (sum(FPOGY_center))/lengthYcenter
    print(Ycenter_CF)

    
else:
    Ycenter_CF = 0
    print(Ycenter_CF)

yCF.append(Ycenter_CF)

##### TOP lEFT X FIXATIONS ####
if xLT != 0:     
    print(columns[11])
    FPOGX_lefttop = columns[11]
    print(FPOGX_lefttop)
    FPOGX_lefttop = [float(i) for i in FPOGX_lefttop]
    print(FPOGX_lefttop)
    for k in range(len(FPOGX_lefttop)):
        FPOGX_lefttop[k] -= xLT
    #print(FPOGX_lefttop)
    FPOGX_lefttop = map(abs, FPOGX_lefttop)
    print(FPOGX_lefttop)
    lengthXLT = len(FPOGX_lefttop)
    print(lengthXLT)
    XLT_CF = (sum(FPOGX_lefttop))/lengthXLT
    print(XLT_CF)

    LT4CornersDuration = columns[14]
    LT4CornersDuration = [float(i) for i in LT4CornersDuration]
    LT4CornersDuration = sum(LT4CornersDuration)
    print(LT4CornersDuration)
else:
    XLT_CF = 0
    print(XLT_CF)

xCF.append(XLT_CF)

##### TOP LEFT Y FIXATIONS #####
if yLT != 0:
    print(columns[12])
    FPOGY_lefttop = columns[12]
    print(FPOGY_lefttop)
    FPOGY_lefttop = [float(i) for i in FPOGY_lefttop]
    print(FPOGY_lefttop)
    for k in range(len(FPOGY_lefttop)):
        FPOGY_lefttop[k] -= yLT
    #print(FPOGX_lefttop)
    FPOGY_lefttop = map(abs, FPOGY_lefttop)
    print(FPOGY_lefttop)
    lengthYLT = len(FPOGY_lefttop)
    print(lengthYLT)
    YLT_CF = (sum(FPOGY_lefttop))/lengthYLT
    print(YLT_CF)
else:
    YLT_CF = 0
    print(YLT_CF)

yCF.append(YLT_CF)

##### TOP RIGHT X FIXATIONS ####
if xRT != 0:     
    print(columns[19])
    FPOGX_righttop = columns[19]
    print(FPOGX_righttop)
    FPOGX_righttop = [float(i) for i in FPOGX_righttop]
    print(FPOGX_righttop)
    for k in range(len(FPOGX_righttop)):
        FPOGX_righttop[k] -= xRT
    #print(FPOGX_lefttop)
    FPOGX_righttop = map(abs, FPOGX_righttop)
    print(FPOGX_righttop)
    lengthXRT = len(FPOGX_righttop)
    print(lengthXRT)
    XRT_CF = (sum(FPOGX_righttop))/lengthXRT
    print(XRT_CF)

    RT4CornersDuration = columns[22]
    RT4CornersDuration = [float(i) for i in RT4CornersDuration]
    RT4CornersDuration = sum(RT4CornersDuration)
    print(RT4CornersDuration)
else:
    XRT_CF = 0
    print(XRT_CF)

xCF.append(XRT_CF)

##### TOP RIGHT Y FIXATIONS ####
if yRT != 0:     
    print(columns[20])
    FPOGY_righttop = columns[20]
    print(FPOGY_righttop)
    FPOGY_righttop = [float(i) for i in FPOGY_righttop]
    print(FPOGY_righttop)
    for k in range(len(FPOGY_righttop)):
        FPOGY_righttop[k] -= yRT
    #print(FPOGX_lefttop)
    FPOGY_righttop = map(abs, FPOGY_righttop)
    print(FPOGY_righttop)
    lengthYRT = len(FPOGY_righttop)
    print(lengthYRT)
    YRT_CF = (sum(FPOGY_righttop))/lengthYRT
    print(YRT_CF)

else:
    YRT_CF = 0
    print(YRT_CF)

yCF.append(YRT_CF)
    
##### BOTTOM LEFT X FIXATIONS ####
if xBL != 0:     
    print(columns[27])
    FPOGX_BL = columns[27]
    print(FPOGX_BL)
    FPOGX_BL = [float(i) for i in FPOGX_BL]
    print(FPOGX_BL)
    for k in range(len(FPOGX_BL)):
        FPOGX_BL[k] -= xBL
    #print(FPOGX_lefttop)
    FPOGX_BL = map(abs, FPOGX_BL)
    print(FPOGX_BL)
    lengthXBL = len(FPOGX_BL)
    print(lengthXBL)
    XBL_CF = (sum(FPOGX_BL))/lengthXBL
    print(XBL_CF)

    BL4CornersDuration = columns[30]
    BL4CornersDuration = [float(i) for i in BL4CornersDuration]
    BL4CornersDuration = sum(BL4CornersDuration)
    print(BL4CornersDuration)
else:
    XBL_CF = 0
    print(XBL_CF)

xCF.append(XBL_CF)

##### BOTTOM LEFT Y FIXATIONS ####
if yBL != 0:     
    print(columns[28])
    FPOGY_BL = columns[28]
    print(FPOGY_BL)
    FPOGY_BL = [float(i) for i in FPOGY_BL]
    print(FPOGY_BL)
    for k in range(len(FPOGY_BL)):
        FPOGY_BL[k] -= yBL
    #print(FPOGX_lefttop)
    FPOGY_BL = map(abs, FPOGY_BL)
    print(FPOGY_BL)
    lengthYBL = len(FPOGY_BL)
    print(lengthYBL)
    YBL_CF = (sum(FPOGY_BL))/lengthYBL
    print(YBL_CF)

else:
    YBL_CF = 0
    print(YBL_CF)

yCF.append(YBL_CF)


##### BOTTOM RIGHT X FIXATIONS ####
if xBR != 0:     
    print(columns[35])
    FPOGX_BR = columns[35]
    print(FPOGX_BR)
    FPOGX_BR = [float(i) for i in FPOGX_BR]
    print(FPOGX_BR)
    for k in range(len(FPOGX_BR)):
        FPOGX_BR[k] -= xBR
    #print(FPOGX_lefttop)
    FPOGX_BR = map(abs, FPOGX_BR)
    print(FPOGX_BR)
    lengthXBR = len(FPOGX_BR)
    print(lengthXBR)
    XBR_CF = (sum(FPOGX_BR))/lengthXBR
    print(XBR_CF)

    BR4CornersDuration = columns[38]
    BR4CornersDuration = [float(i) for i in BR4CornersDuration]
    BR4CornersDuration = sum(BR4CornersDuration)
    print(BR4CornersDuration)
else:
    XBR_CF = 0
    print(XBR_CF)

xCF.append(XBR_CF)

##### BOTTOM RIGHT Y FIXATIONS ####
if yBR != 0:     
    print(columns[36])
    FPOGY_BR = columns[36]
    print(FPOGY_BR)
    FPOGY_BR = [float(i) for i in FPOGY_BR]
    print(FPOGY_BR)
    for k in range(len(FPOGY_BR)):
        FPOGY_BR[k] -= yBR
    #print(FPOGX_lefttop)
    FPOGY_BR = map(abs, FPOGY_BR)
    print(FPOGY_BR)
    lengthYBR = len(FPOGY_BR)
    print(lengthYBR)
    YBR_CF = (sum(FPOGY_BR))/lengthYBR
    print(YBR_CF)

else:
    XYB_CF = 0
    print(YBR_CF)

yCF.append(YBR_CF)

####################################
########### CENTER X  ##############
####################################
    
columns2 = defaultdict(list) 
with open('programtesting2.csv') as l:
        reader2 = csv.reader(l)
        reader2.next()

        for row in reader2:
            for (i,v) in enumerate(row):
                columns2[i].append(v)


##### CENTER X FPOGX ####
if cxXCenter != 0:     
    print(columns2[3])
    cxFPOGX_center = columns2[3]
    print(cxFPOGX_center)
    cxFPOGX_center = [float(i) for i in cxFPOGX_center]
    print(cxFPOGX_center)
    for k in range(len(cxFPOGX_center)):
        cxFPOGX_center[k] -= cxXCenter
    #print(FPOGX_lefttop)
    cxFPOGX_center = map(abs, cxFPOGX_center)
    print(cxFPOGX_center)
    cxlengthXcenter = len(cxFPOGX_center)
    print(cxlengthXcenter)
    cxXcenter_CF = (sum(cxFPOGX_center))/cxlengthXcenter
    print(cxXcenter_CF)

    cxcenterDuration = columns2[6]
    cxcenterDuration = [float(i) for i in cxcenterDuration]
    cxcenterDuration = sum(cxcenterDuration)
    print(cxcenterDuration)
else:
    cxXcenter_CF = 0
    print(cxXcenter_CF)

xCF.append(cxXcenter_CF)

##### CENTER Y FIXATIONS ####
if cxYCenter != 0:     
    print(columns2[4])
    cxFPOGY_center = columns2[4]
    print(cxFPOGY_center)
    cxFPOGY_center = [float(i) for i in cxFPOGY_center]
    print(cxFPOGY_center)
    for k in range(len(cxFPOGY_center)):
        cxFPOGY_center[k] -= cxYCenter
    #print(FPOGX_lefttop)
    cxFPOGY_center = map(abs, cxFPOGY_center)
    print(cxFPOGY_center)
    cxlengthYcenter = len(cxFPOGY_center)
    print(cxlengthYcenter)
    cxYcenter_CF = (sum(cxFPOGY_center))/cxlengthYcenter
    print(cxYcenter_CF)

else:
    cxYcenter_CF = 0
    print(cxYcenter_CF)

yCF.append(cxYcenter_CF)

##### CENTER X SQUARE 1 X coordinates ####
if cx1x != 0:     
    print(columns2[11])
    cxFPOGX1_center = columns2[11]
    print(cxFPOGX1_center)
    cxFPOGX1_center = [float(i) for i in cxFPOGX1_center]
    print(cxFPOGX1_center)
    for k in range(len(cxFPOGX1_center)):
        cxFPOGX1_center[k] -= cx1x
    #print(FPOGX_lefttop)
    cxFPOGX1_center = map(abs, cxFPOGX1_center)
    print(cxFPOGX1_center)
    cxlengthX1center = len(cxFPOGX1_center)
    print(cxlengthX1center)
    cx1x_CF = (sum(cxFPOGX1_center))/cxlengthX1center
    print(cx1x_CF)

    cx1Duration = columns2[14]
    cx1Duration = [float(i) for i in cx1Duration]
    cx1Duration = sum(cx1Duration)
    print(cx1Duration)
else:
    cx1x_CF = 0
    print(cx1x_CF)

xCF.append(cx1x_CF)

##### CENTER X SQUARE 1 y coordinates ####
if cx1y != 0:     
    print(columns2[12])
    cxFPOGY1_center = columns2[12]
    print(cxFPOGY1_center)
    cxFPOGY1_center = [float(i) for i in cxFPOGY1_center]
    print(cxFPOGY1_center)
    for k in range(len(cxFPOGY1_center)):
        cxFPOGY1_center[k] -= cx1y
    #print(FPOGX_lefttop)
    cxFPOGY1_center = map(abs, cxFPOGY1_center)
    print(cxFPOGY1_center)
    cxlengthY1center = len(cxFPOGY1_center)
    print(cxlengthY1center)
    cx1y_CF = (sum(cxFPOGY1_center))/cxlengthY1center
    print(cx1y_CF)

else:
    cx1y_CF = 0
    print(cx1y_CF)


yCF.append(cx1y_CF)

##### CENTER X SQUARE 2 X coordinates ####
if cx2x != 0:     
    print(columns2[19])
    cxFPOGX2_center = columns2[19]
    print(cxFPOGX2_center)
    cxFPOGX2_center = [float(i) for i in cxFPOGX2_center]
    print(cxFPOGX2_center)
    for k in range(len(cxFPOGX2_center)):
        cxFPOGX2_center[k] -= cx2x
    #print(FPOGX_lefttop)
    cxFPOGX2_center = map(abs, cxFPOGX2_center)
    print(cxFPOGX2_center)
    cxlengthX2center = len(cxFPOGX2_center)
    print(cxlengthX2center)
    cx2x_CF = (sum(cxFPOGX2_center))/cxlengthX2center
    print(cx2x_CF)

    cx2Duration = columns2[22]
    cx2Duration = [float(i) for i in cx2Duration]
    cx2Duration = sum(cx2Duration)
    print(cx2Duration)
else:
    cx2x_CF = 0
    print(cx2x_CF)

xCF.append(cx2x_CF)

##### CENTER X SQUARE 2 y coordinates ####
if cx2y != 0:     
    print(columns2[20])
    cxFPOGY2_center = columns2[20]
    print(cxFPOGY2_center)
    cxFPOGY2_center = [float(i) for i in cxFPOGY2_center]
    print(cxFPOGY2_center)
    for k in range(len(cxFPOGY2_center)):
        cxFPOGY2_center[k] -= cx2y
    #print(FPOGX_lefttop)
    cxFPOGY2_center = map(abs, cxFPOGY2_center)
    print(cxFPOGY2_center)
    cxlengthY2center = len(cxFPOGY2_center)
    print(cxlengthY2center)
    cx2y_CF = (sum(cxFPOGY2_center))/cxlengthY2center
    print(cx2y_CF)

else:
    cx2y_CF = 0
    print(cx2y_CF)

yCF.append(cx2y_CF)

##### CENTER X SQUARE 3 X coordinates ####
if cx3x != 0:     
    print(columns2[27])
    cxFPOGX3_center = columns2[27]
    print(cxFPOGX3_center)
    cxFPOGX3_center = [float(i) for i in cxFPOGX3_center]
    print(cxFPOGX3_center)
    for k in range(len(cxFPOGX3_center)):
        cxFPOGX3_center[k] -= cx3x
    #print(FPOGX_lefttop)
    cxFPOGX3_center = map(abs, cxFPOGX3_center)
    print(cxFPOGX3_center)
    cxlengthX3center = len(cxFPOGX3_center)
    print(cxlengthX3center)
    cx3x_CF = (sum(cxFPOGX3_center))/cxlengthX3center
    print(cx3x_CF)

    cx3Duration = columns2[30]
    cx3Duration = [float(i) for i in cx3Duration]
    cx3Duration = sum(cx3Duration)
    print(cx3Duration)
else:
    cx3x_CF = 0
    print(cx3x_CF)

xCF.append(cx3x_CF)

##### CENTER X SQUARE 3 y coordinates ####
if cx3y != 0:     
    print(columns2[20])
    cxFPOGY3_center = columns2[20]
    print(cxFPOGY3_center)
    cxFPOGY3_center = [float(i) for i in cxFPOGY3_center]
    print(cxFPOGY3_center)
    for k in range(len(cxFPOGY3_center)):
        cxFPOGY3_center[k] -= cx3y
    #print(FPOGX_lefttop)
    cxFPOGY3_center = map(abs, cxFPOGY3_center)
    print(cxFPOGY3_center)
    cxlengthY3center = len(cxFPOGY3_center)
    print(cxlengthY3center)
    cx3y_CF = (sum(cxFPOGY3_center))/cxlengthY3center
    print(cx3y_CF)

else:
    cx3y_CF = 0
    print(cx3y_CF)

yCF.append(cx3y_CF)


##### CENTER X SQUARE 4 X coordinates ####
if cx4x != 0:     
    print(columns2[35])
    cxFPOGX4_center = columns2[35]
    print(cxFPOGX4_center)
    cxFPOGX4_center = [float(i) for i in cxFPOGX4_center]
    print(cxFPOGX4_center)
    for k in range(len(cxFPOGX4_center)):
        cxFPOGX4_center[k] -= cx4x
    #print(FPOGX_lefttop)
    cxFPOGX4_center = map(abs, cxFPOGX4_center)
    print(cxFPOGX4_center)
    cxlengthX4center = len(cxFPOGX4_center)
    print(cxlengthX4center)
    cx4x_CF = (sum(cxFPOGX4_center))/cxlengthX4center
    print(cx4x_CF)

    cx4Duration = columns2[38]
    cx4Duration = [float(i) for i in cx4Duration]
    cx4Duration = sum(cx4Duration)
    print(cx4Duration)
else:
    cx4x_CF = 0
    print(cx4x_CF)

xCF.append(cx4x_CF)

##### CENTER X SQUARE 4 y coordinates ####
if cx4y != 0:     
    print(columns2[36])
    cxFPOGY4_center = columns2[36]
    print(cxFPOGY4_center)
    cxFPOGY4_center = [float(i) for i in cxFPOGY4_center]
    print(cxFPOGY4_center)
    for k in range(len(cxFPOGY4_center)):
        cxFPOGY4_center[k] -= cx4y
    #print(FPOGX_lefttop)
    cxFPOGY4_center = map(abs, cxFPOGY4_center)
    print(cxFPOGY4_center)
    cxlengthY4center = len(cxFPOGY4_center)
    print(cxlengthY4center)
    cx4y_CF = (sum(cxFPOGY4_center))/cxlengthY4center
    print(cx4y_CF)

else:
    cx4y_CF = 0
    print(cx4y_CF)

yCF.append(cx1y_CF)

##### CENTER X SQUARE 5 X coordinates ####
if cx5x != 0:     
    print(columns2[43])
    cxFPOGX5_center = columns2[43]
    print(cxFPOGX5_center)
    cxFPOGX5_center = [float(i) for i in cxFPOGX5_center]
    print(cxFPOGX5_center)
    for k in range(len(cxFPOGX5_center)):
        cxFPOGX5_center[k] -= cx5x
    #print(FPOGX_lefttop)
    cxFPOGX5_center = map(abs, cxFPOGX5_center)
    print(cxFPOGX5_center)
    cxlengthX5center = len(cxFPOGX5_center)
    print(cxlengthX5center)
    cx5x_CF = (sum(cxFPOGX5_center))/cxlengthX5center
    print(cx5x_CF)

    cx5Duration = columns2[46]
    cx5Duration = [float(i) for i in cx5Duration]
    cx5Duration = sum(cx5Duration)
    print(cx5Duration)
else:
    cx5x_CF = 0
    print(cx5x_CF)

xCF.append(cx5x_CF)

##### CENTER X SQUARE 5 y coordinates ####
if cx5y != 0:     
    print(columns2[44])
    cxFPOGY5_center = columns2[44]
    print(cxFPOGY5_center)
    cxFPOGY5_center = [float(i) for i in cxFPOGY5_center]
    print(cxFPOGY5_center)
    for k in range(len(cxFPOGY5_center)):
        cxFPOGY5_center[k] -= cx5y
    #print(FPOGX_lefttop)
    cxFPOGY5_center = map(abs, cxFPOGY5_center)
    print(cxFPOGY5_center)
    cxlengthY5center = len(cxFPOGY5_center)
    print(cxlengthY5center)
    cx5y_CF = (sum(cxFPOGY5_center))/cxlengthY5center
    print(cx5y_CF)

else:
    cx5y_CF = 0
    print(cx5y_CF)

yCF.append(cx5y_CF)

##### CENTER X SQUARE 6 X coordinates ####
if cx6x != 0:     
    print(columns2[51])
    cxFPOGX6_center = columns2[51]
    print(cxFPOGX6_center)
    cxFPOGX6_center = [float(i) for i in cxFPOGX6_center]
    print(cxFPOGX6_center)
    for k in range(len(cxFPOGX6_center)):
        cxFPOGX6_center[k] -= cx6x
    #print(FPOGX_lefttop)
    cxFPOGX6_center = map(abs, cxFPOGX6_center)
    print(cxFPOGX6_center)
    cxlengthX6center = len(cxFPOGX6_center)
    print(cxlengthX6center)
    cx6x_CF = (sum(cxFPOGX6_center))/cxlengthX6center
    print(cx6x_CF)

    cx6Duration = columns2[54]
    cx6Duration = [float(i) for i in cx6Duration]
    cx6Duration = sum(cx6Duration)
    print(cx6Duration)
else:
    cx6x_CF = 0
    print(cx6x_CF)

xCF.append(cx6x_CF)

##### CENTER X SQUARE 6 y coordinates ####
if cx6y != 0:     
    print(columns2[52])
    cxFPOGY6_center = columns2[52]
    print(cxFPOGY6_center)
    cxFPOGY6_center = [float(i) for i in cxFPOGY6_center]
    print(cxFPOGY6_center)
    for k in range(len(cxFPOGY6_center)):
        cxFPOGY6_center[k] -= cx6y
    #print(FPOGX_lefttop)
    cxFPOGY6_center = map(abs, cxFPOGY6_center)
    print(cxFPOGY6_center)
    cxlengthY6center = len(cxFPOGY6_center)
    print(cxlengthY6center)
    cx6y_CF = (sum(cxFPOGY6_center))/cxlengthY6center
    print(cx6y_CF)

else:
    cx6y_CF = 0
    print(cx6y_CF)

yCF.append(cx6y_CF)

##### CENTER X SQUARE 7 X coordinates ####
if cx7x != 0:     
    print(columns2[59])
    cxFPOGX7_center = columns2[59]
    print(cxFPOGX7_center)
    cxFPOGX7_center = [float(i) for i in cxFPOGX7_center]
    print(cxFPOGX7_center)
    for k in range(len(cxFPOGX7_center)):
        cxFPOGX7_center[k] -= cx7x
    #print(FPOGX_lefttop)
    cxFPOGX7_center = map(abs, cxFPOGX7_center)
    print(cxFPOGX7_center)
    cxlengthX7center = len(cxFPOGX7_center)
    print(cxlengthX7center)
    cx7x_CF = (sum(cxFPOGX7_center))/cxlengthX7center
    print(cx7x_CF)

    cx7Duration = columns2[62]
    cx7Duration = [float(i) for i in cx7Duration]
    cx7Duration = sum(cx7Duration)
    print(cx7Duration)
else:
    cx7x_CF = 0
    print(cx7x_CF)

xCF.append(cx7x_CF)

##### CENTER X SQUARE 7 y coordinates ####
if cx7y != 0:     
    print(columns2[60])
    cxFPOGY7_center = columns2[60]
    print(cxFPOGY7_center)
    cxFPOGY7_center = [float(i) for i in cxFPOGY7_center]
    print(cxFPOGY7_center)
    for k in range(len(cxFPOGY7_center)):
        cxFPOGY7_center[k] -= cx7y
    #print(FPOGX_lefttop)
    cxFPOGY7_center = map(abs, cxFPOGY7_center)
    print(cxFPOGY7_center)
    cxlengthY7center = len(cxFPOGY7_center)
    print(cxlengthY7center)
    cx7y_CF = (sum(cxFPOGY7_center))/cxlengthY7center
    print(cx7y_CF)

else:
    cx7y_CF = 0
    print(cx7y_CF)

yCF.append(cx7y_CF)

##### CENTER X SQUARE 8 X coordinates ####
if cx8x != 0:     
    print(columns2[67])
    cxFPOGX8_center = columns2[67]
    print(cxFPOGX8_center)
    cxFPOGX8_center = [float(i) for i in cxFPOGX8_center]
    print(cxFPOGX8_center)
    for k in range(len(cxFPOGX8_center)):
        cxFPOGX8_center[k] -= cx8x
    #print(FPOGX_lefttop)
    cxFPOGX8_center = map(abs, cxFPOGX8_center)
    print(cxFPOGX8_center)
    cxlengthX8center = len(cxFPOGX8_center)
    print(cxlengthX8center)
    cx8x_CF = (sum(cxFPOGX8_center))/cxlengthX8center
    print(cx8x_CF)

    cx8Duration = columns2[70]
    cx8Duration = [float(i) for i in cx8Duration]
    cx8Duration = sum(cx8Duration)
    print(cx8Duration)
else:
    cx8x_CF = 0
    print(cx8x_CF)

xCF.append(cx8x_CF)

##### CENTER X SQUARE 8 y coordinates ####
if cx8y != 0:     
    print(columns2[70])
    cxFPOGY8_center = columns2[70]
    print(cxFPOGY8_center)
    cxFPOGY8_center = [float(i) for i in cxFPOGY8_center]
    print(cxFPOGY8_center)
    for k in range(len(cxFPOGY8_center)):
        cxFPOGY8_center[k] -= cx8y
    #print(FPOGX_lefttop)
    cxFPOGY8_center = map(abs, cxFPOGY8_center)
    print(cxFPOGY8_center)
    cxlengthY8center = len(cxFPOGY8_center)
    print(cxlengthY8center)
    cx8y_CF = (sum(cxFPOGY8_center))/cxlengthY8center
    print(cx8y_CF)

else:
    cx8y_CF = 0
    print(cx8y_CF)

yCF.append(cx8y_CF)

##### exporting to csv ###
#csv.register_dialect('cfdialect', delim
header = ['4 corners center X', '4 corners center Y', 'Top Left X', 'Top Left Y', 'Top Right X', 'Top Right Y', 'Bottom left X', 'Bottom Left Y', 'Bottom Right X', 'Bottom Right Y', 'xCenter X', 'xCenter Y', '1X', '1Y', '2X', '2Y', '3X', '3Y', '4X', '4Y', '5X', '5Y', '6X', '6Y', '7X', '7Y', '8X', '8Y']  
cfData = [Xcenter_CF, Ycenter_CF, XLT_CF, YLT_CF, XRT_CF, YLT_CF, XBL_CF, YBL_CF, XBR_CF, YBR_CF, cxXcenter_CF, cxYcenter_CF, cx1x_CF, cx1y_CF, cx2x_CF, cx2y_CF, cx3x_CF, cx3y_CF, cx4x_CF, cx4y_CF, cx5x_CF, cx5y_CF, cx6x_CF, cx6y_CF, cx7x_CF, cx7y_CF, cx8x_CF, cx8y_CF]
with open('correctionfactors.csv', 'w') as csvfile:
    csvfile = csv.writer(csvfile, delimiter=',')
    csvfile.writerow(header)
    csvfile.writerow(cfData)
