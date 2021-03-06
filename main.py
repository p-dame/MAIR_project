# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:32:23 2017

@author: Pauline Dame
"""

import random as rd
import matplotlib.pyplot as plt
import csv
import os
from math import *
import mpld3 

# --------- GLOBAL PARAMETERS -----------------------------------------------------

#Parameters of the CSV file
save_path_csv ="D:\AI Master\Project MAIR\Test"



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

def get_dots_coordinates(n1,n2,dist) :    
    

    dist_min = dist   
    string_dots_blue = ""
    string_dots_yellow = ""
    list_dots = []
    for blue_dot in range(n1):
        check = 0
        while check < dist_min : 
            x ,y = rd.uniform(-size+radius,size-radius) , rd.uniform(-size+radius,size-radius)
            check = check_distance_dots(x,y,list_dots,dist_min)
        string_dots_blue += '{x:'+str(x)+', y: '+str(y)+', z:3,color : "Blue" },'
        list_dots.append((x,y))
    for yellow_dot in range(n2):
        check = 0
        while check < dist_min : 
            x ,y = rd.uniform(-size+radius,size-radius) , rd.uniform(-size+radius,size-radius)
            check = check_distance_dots(x,y,list_dots,dist_min)
        string_dots_yellow += '{x:'+str(x)+', y: '+str(y)+', z:3,color : "Yellow"},'
        list_dots.append((x,y))
    return string_dots_blue, string_dots_yellow

#def display_image(size,n1,n2,radius,dist,legend) : 
#                    
#    fig, ax = plt.subplots()
#    dist_min = dist   
#    list_dots = []
#    for red_dot in range(n1):
#        check = 0
#        while check < dist_min : 
#            x ,y = rd.uniform(-size+radius,size-radius) , rd.uniform(-size+radius,size-radius)
#            check = check_distance_dots(x,y,list_dots,dist_min)
#        list_dots.append((x,y))            
#        ax.add_artist(plt.Circle((x,y),radius,color='y'))
#    for red_dot in range(n2):
#        check = 0
#        while check < dist_min : 
#            x ,y = rd.uniform(-size+radius,size-radius) , rd.uniform(-size+radius,size-radius)
#            check = check_distance_dots(x,y,list_dots,dist_min)
#        list_dots.append((x,y))                        
#        ax.add_artist(plt.Circle((x,y),radius,color='b'))
#            
#        
#    plt.xlabel(legend)
#    ax.set_xlim((-size, size))
#    ax.set_ylim((-size, size))
#    plt.ion()
#    plt.show()
#    plt.pause(.001)
#    return mpld3.fig_to_html(fig)

            
#def display_image_paired_dots(size,n1,n2,radius,dist,legend) : 
#
#    fig, ax = plt.subplots()
#    dist_min = dist   
#    list_dots = []   
#    nbr_pairs = min(n1,n2)
#    for pair in range(nbr_pairs) :
#        check = 0
#        while check < dist_min : 
#            x1 ,y1 = rd.uniform(-size+dist,size-dist) , rd.uniform(-size+dist,size-dist) 
#            check = check_distance_dots(x1,y1,list_dots,dist_min)
#        list_dots.append((x1,y1))
#        check = 0
#        while check < dist_min : 
#            dx , dy = rd.choice([rd.uniform(-300*radius,-dist*100), rd.uniform(300*radius,dist*100)])/100 , rd.choice([rd.uniform(-300*radius,-dist*50),rd.uniform(300*radius,dist*50)])/100
#            x2 , y2 = x1 + dx , y1 + dy
#            check = check_distance_dots(x2,y2,list_dots,dist_min)
#        list_dots.append((x2,y2))
#        ax.add_artist(plt.Circle((x1,y1),radius,color='b'))
#        ax.add_artist(plt.Circle((x2,y2),radius,color='y'))
#    nbr_isolated_dots = abs(n1-n2)
#    color_dots = 'b'
#    if n1 > n2 : 
#        color_dots = 'y'
#    for dot in range(nbr_isolated_dots) : 
#        check = 0
#        while check < dist_min : 
#            x ,y = rd.uniform(-size+dist,size-dist) , rd.uniform(-size+dist,size-dist)
#            check = check_distance_dots(x,y,list_dots,dist_min)
#        ax.add_artist(plt.Circle((x,y),radius,color=color_dots))
#    return mpld3.fig_to_html(fig)
#            
#    
#    plt.xlabel(legend)
#    ax.set_xlim((-size, size))
#    ax.set_ylim((-size, size))
#    plt.ion()
##    plt.show()
##    plt.pause(.001)
#    return fig 

 



#def record_RT(): 
#    experiment = True 
#    beg=time.time()
#    while experiment : 
#        if keyboard.is_pressed('y') :
#            end=time.time()
#            experiment = False 
#            print('Yes')
#            print('Reaction time : '+str(end-beg))
#            answer = 'Yes'
#        elif keyboard.is_pressed('n') :
#            end=time.time()
#            experiment = False 
#            print('No')
#            print('Reaction time : '+str(end-beg))
#            answer = 'No'
#    return answer, end-beg
    

def save_result_to_csv(path,name,age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,time,question) :
        path_file = os.path.join(path,'test_experiment_final.csv')
        if os.path.exists(path_file) == False : 
            with open(os.path.join(path_file), 'wb',) as csvfile :
                spamwriter = csv.writer(csvfile, delimiter=',',lineterminator='\n')
                spamwriter.writerow( ('Name', 'Age','Gender', 'Colour blindness','Eyesight','Native Language','Blue dots','Red dots','Ratio','Answer', 'Reaction time','Question') )
        with open(os.path.join(path_file), 'a') as csvfile :
            spamwriter = csv.writer(csvfile, delimiter=',',lineterminator='\n')
            spamwriter.writerow( (name, age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,time,question) )


#def experiment_mth(exp) :
#    
#    nbr_blue = exp[0][1]
#    nbr_red = exp[0][0]
#    ratio = float("{0:.2f}".format(nbr_blue/nbr_red))
#    if exp[1] == 1 : 
#        nbr_red,nbr_blue = nbr_blue,nbr_red
##    if nbr_blue > nbr_red :
##        correct_answer = 'Yes'
##    else :
##        correct_answer = 'No'
#    list_blue, list_yellow = get_dots_coordinates(nbr_blue,nbr_yellow,dist)    
##    answer,answer_time = record_RT()
##    if answer == correct_answer : 
##        answer = 'right'
##    else : 
##        answer = 'wrong'
##    save_result_to_csv(save_path_csv,name,age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,answer_time,'more than half')
##    plt.close() 
##    return plot
#    return list_blue, list_yellow
    
def main() :

    nbr_blue = sys.argv[0][1]
    nbr_yellow = sys.argv[0][0]
#    ratio = float("{0:.2f}".format(nbr_blue/nbr_yellow))
    if sys.argv[1] == 1 : 
        nbr_red,nbr_blue = nbr_blue,nbr_yellow
#    if nbr_blue > nbr_red :
#        correct_answer = 'Yes'
#    else :
#        correct_answer = 'No'
#    print(correct_answer)
    list_blue, list_yellow = get_dots_coordinates(nbr_blue,nbr_yellow,dist)    
#    answer,answer_time = record_RT()
#    if answer == correct_answer : 
#        answer = 'right'
#    else : 
#        answer = 'wrong'
#    save_result_to_csv(save_path_csv,name,age,gender, colour_bld,eyesight,native_language,nbr_blue,nbr_red,ratio,answer,answer_time,'more than half')
#    plt.close() 
#    return list_blue, list_yellow
    print list_blue, list_yellow
        
        
        
#----- Call the main function to run the code --------------
    
main()

           
