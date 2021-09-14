import matplotlib
matplotlib.use('TKAgg')
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D

def game(lat, size):   # Updates the rules for the game of life
    latnew = lat.copy()
    for i in range(size):
        for j in range(size):
            alive = []
            temp1 = [lat[(i+1)%size, (j+1)%size], lat[(i+1)%size, j], lat[(i+1)%size, (j-1)%size], lat[i, (j+1)%size], lat[i, (j-1)%size], lat[(i-1)%size, (j+1)%size], lat[(i-1)%size, j], lat[(i-1)%size, (j-1)%size]]
            for k in range(len(temp1)):
                if temp1[k] == 1:    
                    alive.append(temp1[k])   #len(alive) gives the number of alive cells around a point 
            num_alive = len(alive)

            if lat[i,j] == 1 and num_alive < 2: #Live cell dying with <2
                latnew[i,j] = 0
               
            elif lat[i,j] == 1 and num_alive > 3:  #Live cell dying with >3
                latnew[i,j] = 0

            if lat[i,j] == 0 and num_alive == 3: #Dead cell coming alive
                latnew[i,j] = 1 
    
    return latnew

def rand(size):  # Creates a random initial condition for the game of life
    lat = np.zeros((size,size), dtype = float)
    for i in range(size):
        for j in range(size):
            r=random.random()
            if(r<0.5): lat[i,j]= 0    #  0 = Dead
            if(r>=0.5): lat[i,j]=1    #  1 = Alive
    return lat



def main():

    # Take the initial inputs from the user
    size = int(input("Give the size of the square lattice: "))
    sweep = size**2
       # if condition == 0:
        #    animate = int(input("Animation(0) or histogram(1)?: "))
         #   if animate == 1:
          #      hist = int(input("Write data(0) or plot data(1)?: "))     

    lat = rand(size)
    active_sites = []
    com = []
    time = []
    count = 0
    for i in range(1000): # Does 1000 sweeps for the game of life
        lat = game(lat, size)

        if(i%2 ==0 ):   # Animates it for every 5 sweeps
  #          xcom, ycom = COM(lat, size) # Finds the center of mass for the lattice
   #         if abs(xcom-ycom)<10 and condition == 2:   #i.e, not going over a boundary
    #            com.append([xcom, ycom])
     ##           print("center of mass of glider is : ", com[count])
       #         time.append(count)
        #        count+=1
         #   elif(abs(xcom-ycom)>10) and condition == 2:  # If the differece is greater than 10, then its going over a boundary
          #      count = 0

            f=open('game_of_life.dat','w')
            for i in range(size):
                for j in range(size):
                    f.write('%d %d %lf\n'%(i,j,lat[i,j]))
            f.close()
            #show animation
            plt.cla()
            im=plt.imshow(lat, animated=True)
            plt.draw()
            plt.pause(0.0001)

    return

main()