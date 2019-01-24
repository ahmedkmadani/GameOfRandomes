#import required libraries 
import random
import matplotlib.pyplot as plt
import numpy as np

csfont = {'fontname':'Comic Sans MS'}

# function to simulate tow players choosing two different random numbers  

def random_game(number_of_try):
   y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10=0,0,0,0,0,0,0,0,0,0,0
   x,y,z=0,0,0
   no0,no1,no2,no3,no4,no5,no6,no7,no8,no9,no10=0,0,0,0,0,0,0,0,0,0,0
   for i in range(number_of_try):
        x = random.randint(0,5)
        y = random.randint(0,5)
        z =x+y
        if z ==0:
            y0 = y0+1
            no0 = float(y0)/ number_of_try
        elif z ==1:
            y1 = y1+1
            no1 = float(y1)/ number_of_try       
        elif z ==2:
            y2 = y2+1
            no2 = float(y2)/ number_of_try            
        elif z ==3:
            y3 = y3+1
            no3 = float(y3)/ number_of_try
        elif z ==4:
            y4 = y4+1
            no4 = float(y4)/ number_of_try
        elif z ==5:
            y5 = y5+1
            no5 = float(y5)/ number_of_try
        elif z ==6:
            y6 = y6+1
            no6 = float(y6)/ number_of_try
        elif z ==7:
            y7 = y7+1
            no7 = float(y7)/ number_of_try
        elif z ==8:
            y8 = y8+1
            no8 = float(y8)/ number_of_try
        elif z ==9:
            y9 = y9+1
            no9 = float(y9)/ number_of_try
        else:
            y10=y10+1 
            no10 = float(y10)/ number_of_try
   return (no0,no1,no2,no3,no4,no5,no6,no7,no8,no9,no10,x,y)
 
 #number of try to run Monte-Carlo method to archive less error in simulation 

number_of_try = 10000
 
for i in range(1):
    hit = random_game(number_of_try)
    print ('probability of 0 is ',hit[0] )
    print ('probability of 1 is ',hit[1] ) 
    print ('probability of 2 is ',hit[2] )
    print ('probability of 3 is ',hit[3] )
    print ('probability of 4 is ',hit[4] )
    print ('probability of 5 is ',hit[5] )
    print ('probability of 6 is ',hit[6] )
    print ('probability of 7 is ',hit[7] )
    print ('probability of 8 is ',hit[8] )
    print ('probability of 9 is ',hit[9] )
    print ('probability of 10 is ',hit[10] )
    probability = [hit[0], hit[1], hit[2], hit[3], hit[4],hit[5],hit[6],hit[7],hit[8],hit[9],hit[10]]
    options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

#plot the probability along side with each number 

pos = np.arange(len(options))
width = 0.5     
ax = plt.axes()
ax.set_xticks(pos + (width /20))
ax.set_xticklabels(options)
plt.bar(pos, probability, width, color='b')
plt.xlabel('Options for players ',**csfont  )
plt.ylabel('Probability for each option %', **csfont)
plt.show()