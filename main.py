# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:32:23 2017

@author: Pauline Dame
"""

import keyboard
import time 
import random as rd
import matplotlib.pyplot as plt
import csv
import os
from math import *

# --------- GLOBAL PARAMETERS -----------------------------------------------------


#Parameters of the figure (window and dots)
size_windows = 10
radius = float(size_windows)/50
dist = 1
size = radius + size_windows

#Parameters of the CSV file
save_path_csv ="D:\AI Master\Project MAIR\Test"

#Get these input using PHP
name = raw_input('What is your name ? ')
age = input('What is your age ?  ')
gender = raw_input('What is your gender ? (m/f) ')
colour_bld = raw_input('Are you colour blind ? (y/n) ')
eyesight = raw_input('Do you have a corrected or normal eyesight ? (c/n) ')
native_language = raw_input('What is your native language (english, dutch, french, spanish, german) ?) ')    

#Creating the list of all the 16 types of trials
ratios = [(4,5),(3,5),(2,5),(1,5),(29,71),(17,83),(10,90),(2,98)]
experiments = []
for i in range(2) : 
    for j in range(len(ratios)):
        experiments.append((ratios[j],i))
#Creating a list to keep track of all the 80 trials which should be done during on experiment
index = []
for j in range(5):
    for i in range(16):
        index.append(i)
        

#----------FUNCTIONS -----------------------------------------------------------------

def check_distance_dots(x,y,list_dots,dist_min):
    if list_dots == [] : 
        return dist_min +1
    else : 
        check = True 
        for existing_dot in list_dots : 
            distance = sqrt((x-existing_dot[0])**2+(y-existing_dot[1])**2)
            if distance < dist_min : 
                check = distance 
        if check == True : 
            check = dist_min +1 
        return check

    

def display_image(size,n1,n2,radius,dist,legend) : 
    
    fig, ax = plt.subplots()
    dist_min = dist   
    list_dots = []
    for red_dot in range(n1):
        check = 0
        while check < dist_min : 
            x ,y = rd.uniform(-size+radius,size-radius) , rd.uniform(-size+radius,size-radius)
            check = check_distance_dots(x,y,list_dots,dist_min)
        list_dots.append((x,y))            
        ax.add_artist(plt.Circle((x,y),radius,color='r'))
    for red_dot in range(n2):
        check = 0
        while check < dist_min : 
            x ,y = rd.uniform(-size+radius,size-radius) , rd.uniform(-size+radius,size-radius)
            check = check_distance_dots(x,y,list_dots,dist_min)
        list_dots.append((x,y))                        
        ax.add_artist(plt.Circle((x,y),radius,color='b'))
            
        
    plt.xlabel(legend)
    ax.set_xlim((-size, size))
    ax.set_ylim((-size, size))
    plt.ion()
    plt.show()
    plt.pause(.001)
    return ax

            
def display_image_paired_dots(size,n1,n2,radius,dist,legend) : 

    fig, ax = plt.subplots()
    dist_min = dist   
    list_dots = []   
    nbr_pairs = min(n1,n2)
    list_dots = []
    for pair in range(nbr_pairs) :
        check = 0
        while check < dist_min : 
            x1 ,y1 = rd.uniform(-size+dist,size-dist) , rd.uniform(-size+dist,size-dist) 
            check = check_distance_dots(x1,y1,list_dots,dist_min)
        list_dots.append((x1,y1))
        check = 0
        while check < dist_min : 
            dx , dy = rd.choice([rd.uniform(-300*radius,-dist*100), rd.uniform(300*radius,dist*100)])/100 , rd.choice([rd.uniform(-300*radius,-dist*50),rd.uniform(300*radius,dist*50)])/100
            x2 , y2 = x1 + dx , y1 + dy
            check = check_distance_dots(x2,y2,list_dots,dist_min)
        list_dots.append((x2,y2))
        ax.add_artist(plt.Circle((x1,y1),radius,color='b'))
        ax.add_artist(plt.Circle((x2,y2),radius,color='r'))
    nbr_isolated_dots = abs(n1-n2)
    color_dots = 'b'
    if n1 > n2 : 
        color_dots = 'r'
    for dot in range(nbr_isolated_dots) : 
        check = 0
        while check < dist_min : 
            x ,y = rd.uniform(-size+dist,size-dist) , rd.uniform(-size+dist,size-dist)
            check = check_distance_dots(x,y,list_dots,dist_min)
        ax.add_artist(plt.Circle((x,y),radius,color=color_dots))
        list_dots.append((x,y))           
            
    
    plt.xlabel(legend)
    ax.set_xlim((-size, size))
    ax.set_ylim((-size, size))
    plt.ion()
    plt.show()
    plt.pause(.001)
    return ax
    

def record_RT(): 
    experiment = True 
    beg=time.time()
    while experiment : 
        if keyboard.is_pressed('y') :
            end=time.time()
            experiment = False 
            print('Yes')
            print('Reaction time : '+str(end-beg))
            answer = 'Yes'
        elif keyboard.is_pressed('n') :
            end=time.time()
            experiment = False 
            print('No')
            print('Reaction time : '+str(end-beg))
            answer = 'No'
    return answer, end-beg
    

def save_result_to_csv(path,name,age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,time,question) :
        path_file = os.path.join(path,'test_experiment_final.csv')
        if os.path.exists(path_file) == False : 
            with open(os.path.join(path_file), 'wb',) as csvfile :
                spamwriter = csv.writer(csvfile, delimiter=',',lineterminator='\n')
                spamwriter.writerow( ('Name', 'Age','Gender', 'Colour blindness','Eyesight','Native Language','Blue dots','Red dots','Ratio','Answer', 'Reaction time','Question') )
        with open(os.path.join(path_file), 'a') as csvfile :
            spamwriter = csv.writer(csvfile, delimiter=',',lineterminator='\n')
            spamwriter.writerow( (name, age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,time,question) )


def experiment_mth(name,age,gender, colour_bld,eyesight,native_language,exp) :
    
    nbr_blue = exp[0][1]
    nbr_red = exp[0][0]
    ratio = float("{0:.2f}".format(nbr_blue/nbr_red))
    if exp[1] == 1 : 
        nbr_red,nbr_blue = nbr_blue,nbr_red
    if nbr_blue > nbr_red :
        correct_answer = 'Yes'
    else :
        correct_answer = 'No'
    display_image(size,nbr_red,nbr_blue,radius,dist,'Are more than half of the dots blue ?')
    answer,answer_time = record_RT()
    if answer == correct_answer : 
        answer = 'right'
    else : 
        answer = 'wrong'
    print answer
    save_result_to_csv(save_path_csv,name,age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,answer_time,'more than half')
    plt.close() 
    time.sleep(0.5)
    
def experiment_most(name,age,gender, colour_bld,eyesight,native_language,exp) :

    nbr_blue = exp[0][1]
    nbr_red = exp[0][0]
    ratio = float("{0:.2f}".format(nbr_blue/nbr_red))
    if exp[1] == 1 : 
        nbr_red,nbr_blue = nbr_blue,nbr_red
    if nbr_blue > nbr_red :
        correct_answer = 'Yes'
    else :
        correct_answer = 'No'
    print(correct_answer)
    display_image(size,nbr_red,nbr_blue,radius,dist,'Are most of the dots blue ?')
    answer,answer_time = record_RT()
    if answer == correct_answer : 
        answer = 'right'
    else : 
        answer = 'wrong'
    print answer
    save_result_to_csv(save_path_csv,name,age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,answer_time,'more than half')
    plt.close() 
    time.sleep(0.5)
    
def main() : 
    exp = experiments
    ind = index
    while ind != [] :
        print ind
        num = rd.choice(ind)       
        experiment_most(name,age,gender,colour_bld,eyesight,native_language,exp[num])
        
        ind.remove(num)
        
        
#----- Call the main function to run the code --------------
    
main()

           
