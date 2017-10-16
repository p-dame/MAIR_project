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
import sqlite3
from math import *


size_windows = 10
radius = float(size_windows)/50
dist = 1
size = radius + size_windows
save_path_csv ="D:\AI Master\Project MAIR\Test"
paired = True

#connection = sqlite3.connect(os.path.join(path,'experiment.db'))
#cursor = connection.cursor()
#sql_command = """
#CREATE TABLE results ( 
#participant_number INTEGER PRIMARY KEY, 
#name VARCHAR(30), 
#age INT, 
#gender CHAR(1), 
#colour_blindness CHAR(1),
#eyesight CHAR(1),
#native_language CHAR(15),
#blue_dots INT,
#red_dot INT,
#ratio FLOAT,
#answer CHAR(10),
#time FLOAT,
#question CHAR(20));"""
#cursor.execute(sql_command)
#connection.commit()
#connection.close()

name = raw_input('What is your name ? ')
age = input('What is your age ?  ')
gender = raw_input('What is your gender ? (m/f) ')
colour_bld = raw_input('Are you colour blind ? (y/n) ')
eyesight = raw_input('Do you have a corrected or normal eyesight ? (c/n) ')
native_language = raw_input('What is your native language (english, dutch, french, spanish, german) ?) ')    
ratios = [(4,5),(3,5),(2,5),(1,5),(29,71),(17,83),(10,90),(2,98)]
question = ['more than half','most']
exp0 = ((4,5),'more than half',0.56)
exp1 = ((4,5),'most',0.56)
exp2 = ((3,5),'more than half',0.63)
exp3 = ((3,5),'most',0.63)
exp4 = ((2,5),'more than half',0.71)
exp5 =((2,5),'most',0.71)
exp6 =((1,5),'more than half',0.83)
exp7 =((1,5),'most',0.83)
exp8 =((29,71),'more than half',0.71)
exp9 =((29,71),'most',0.71)
exp10 = ((17,83),'more than half',0.83)
exp11 = ((17,83),'most',0.83)
exp12 =( (10,90),'more than half',0.90)
exp13 =((10,90),'most',0.90)
exp14 =( (2,98),'more than half',0.98)
exp15 = ((2,98),'most',0.98)
experiments = [exp0,exp1,exp2,exp3,exp4,exp5,exp6,exp7,exp8,exp9,exp10,exp11,exp12,exp13,exp14,exp15]
index = []
for j in range(5):
    for i in range(16):
        index.append(i)


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

    

def display_image(size,n1,n2,radius,paired,dist,legend) : 
    
    fig, ax = plt.subplots()
    dist_min = dist   
    if paired == False : 
        for red_dot in range(n1):
            x ,y = rd.uniform(-size+radius,size-radius) , rd.uniform(-size+radius,size-radius)
            ax.add_artist(plt.Circle((x,y),radius,color='r'))
        for red_dot in range(n2):
            x ,y = rd.uniform(-size+radius,size-radius) , rd.uniform(-size+radius,size-radius)
            ax.add_artist(plt.Circle((x,y),radius,color='b'))
    
    if paired == True : 
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
            
#    if n1<10 or n2 < 10 :
#    nbr_dots = [n1,n2]
#    list_dots = []
#    for nbr in nbr_dots : 
#        if nbr < 3 :
#            for i in nbr : 
#                check = 0
#                while check < dist_min : 
#                    x1 ,y1 = rd.uniform(-size+dist,size-dist) , rd.uniform(-size+dist,size-dist) 
#                    check = check_distance_dots(x1,y1,list_dots,dist_min)
#                list_dots.append((x1,y1))
            
            
    
    plt.xlabel(legend)
    ax.set_xlim((-size, size))
    ax.set_ylim((-size, size))
    plt.ion()
    plt.show()
    plt.pause(.001)
    

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

#def save_result_to_SQL(path,name,age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,time,question) :
#    connection = sqlite3.connect(os.path.join(path,'experiment.db'))
#    cursor = connection.cursor()
#    sql_command = 'INSERT INTO results (name,age,gender,colour_blindness,eyesight,native_language,blue_dots, red_dots,ratio,answer,time,question) VALUES ( "' +name+'","'+str(age)+'","'+ gender +'","'+colour_blidness+'","'+eyesight+'","'+native_language+'","'+blue_dots+'","'+red_dots+'","'+ratio+'","'+answer+'","'+time'");'
#    cursor.execute(sql_command)
#    connection.commit()
#    connection.close()

def experiment(name,age,gender, colour_bld,eyesight,native_language,exp) :
    ratio = exp[2]
    color = 'blue'
    seed_question = rd.randint(0,1) 
    if seed_question == 1 : 
        color = 'red'
    seed_color = rd.randint(0,1) 
    nbr_blue = exp[0][0]
    nbr_red = exp[0][1]
    if seed_color == 1 : 
        nbr_red,nbr_blue = nbr_blue,nbr_red
    if nbr_blue > nbr_red :
        correct_answer = 'Yes'
    else :
        correct_answer = 'No'
    q = exp[1]
    display_image(size,nbr_red,nbr_blue,radius,paired,dist,'Are '+ q+' of the dots '+color+' ?')
    answer,answer_time = record_RT()
    if answer == correct_answer and color=='blue': 
        answer = 'right'
    elif answer != correct_answer and color=='red':
        answer = 'right'
    else : 
        answer = 'wrong'
    print answer
    save_result_to_csv(save_path_csv,name,age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,answer_time,q)
    plt.close() 
    time.sleep(0.5)
    
def main() : 
    exp = experiments
    ind = index
    while ind != [] :
        print ind
        num = rd.choice(ind)       
        experiment(name,age,gender,colour_bld,eyesight,native_language,exp[num])
        
        ind.remove(num)
    
main()

           
    
    
#to do : 
    # - lower case the inputs