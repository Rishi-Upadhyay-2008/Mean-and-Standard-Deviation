import random 
import math
import matplotlib.pyplot as plt

walks = 1000 # Amount of paths taken by the loop
finalPosition = [] # The final position of the paths and puts it into a list

# repeats the task 
for i in range(walks) :
  LR = 0
  FB = 0
  direct = 0

  # while loop determines the directions it goes 
  while direct <10000 :
# The movement is turns essentially 
        movement = random.randint(0,3)
        if movement == 0 : # represents a right turn
            LR += 1
        elif movement == 1 : # represents a left turn 
          LR -=1.    
        elif movement == 2 : # represents a step forward
          FB += 1  
        else :   # represents a step back           
         FB -= 1
        direct += 1
      
  # appends final position therefore making it easier to calculate
        finalPosition.append(math.sqrt(LR**2 + FB**2)) 


# Calculates Mean, Std Dev, & Variance
mean = sum(finalPosition)/len(finalPosition)
variance = sum ((i - mean)**2 for i in finalPosition)/len(finalPosition)
std = math.sqrt(variance)
print("Mean:",mean)
print('Std.Dev:',std)

# Plots the data on a histogram to help visualise it 

plt.hist(finalPosition,bins=100, color='red' )
plt.show()
# bins is the range of the data so for now it'll go from 0-100
