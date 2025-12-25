import random 
import math
import matplotlib.pyplot as plt

walks = 1000 # Amount of paths taken by the loop
finalPosition = [] # The final position of the paths and puts it into a list

# repeats the task 
for i in range(walks) :
  position = 0 
  direct = 0

  # while loop determines the directions it goes 
  while direct <10000 :
# The movement is turns essentially 
        movement = random.randint(0,1)
        if movement == 0 : # represents a right turn
            position += 1
        else :             # if you dont go right you go left 
         position -= 1
        direct = direct + 1
  # appends final position therefore making it easier to calculate
        finalPosition.append(position) 


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
