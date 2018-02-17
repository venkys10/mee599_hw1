#!/usr/bin/env python

import csv
import numpy as np

def scores():
    col_final = []
    lab_name = []
    with open('grades.csv', 'r') as grades:
        reader = csv.reader(grades)
        grade_head = reader.next()          #get the headers of grades.csv

        for i, x in enumerate(grade_head):    # get a column number along with name and take the i value that has name
            if "Final Score" == x:
                lab_name.append(i)
            #save full column in col_final
        for col in reader:
            col_final.append(col[lab_name[0]][0:])
            #get length of the column
        number_of_studs = float(len(col_final))
        col_final_mapped = map(float, col_final)
        sum_final = sum(col_final_mapped)

                    #Average score
        average_final = sum_final / number_of_studs

        #check for above average and below average-----------------------
        count_above = 0
        count_below = 0
        for i in col_final_mapped:
            if i > average_final:
                count_above = count_above + 1
            else:
                count_below = count_below + 1
                    #print percentage of people
        percentage_above = (count_above / number_of_studs) * 100

        #check for median and above median-----------------------------
        median_final = np.median(col_final_mapped)

            #Percentage of peopele above median
        count_med = 0
        for i in col_final_mapped:
            if i > median_final:
                count_med = count_med + 1
            else:
                pass
            #print percentage above median
        percentage_median = (count_med / number_of_studs) * 100
        print "\nAverage score:", round(average_final, 2), "\nAbove Average:", round(percentage_above,2),"%", \
                        "\nMedian Score", median_final, "\nAbove Median:", round(percentage_median,2),"%"


def hardest_assignment(type):
    sum_lab = []
    col_final_norm = []
    col_avg = []
    col_final1=[]
    lab_name = []
    with open('grades.csv', 'r') as grades:
        reader = csv.reader(grades)
        grade_head = reader.next()          #get the headers of grades.csv
        for i, x in enumerate(grade_head):  # get a column number along with name and take the i value that has name
            if type in x:
                lab_name.append(i)

        reader = list(reader)
        for name in lab_name:               #itertaing through all the columns that are named LAB
            col_final = []
            for col in reader:
                try:
                    col_final.append(float(col[name]))  # save full column in col_final
                except ValueError:
                    pass
            col_final1.append(col_final)            #save all columns in col_final1


                    #NORMALIZE EACH COLUMN,
        for x in col_final1:
            col_final_norm_temp = []

            for i in x:
                p = (float(i)/float(max(x)))*100.0          #all numbers are now out of 100 and are in col_final_norm i.e normalized values
                col_final_norm_temp.append(p)

            col_final_norm.append(col_final_norm_temp)      #length of each column after normalizing and removing strings


                    #TAKE SUM AND AVERAGE OF EACH COLUMN-----------------------
        for x in col_final_norm:

            col_avg.append(np.mean(x))                   #average of numbers after removing strings
            sum_lab.append(np.sum(x))                       #sum of numbers are after removing strings are now in lab

        sum_np = []
        for a, b in enumerate(col_final_norm):
            c = b < col_avg[a]
            sum_np.append(np.sum(c))
        max1 = max(sum_np)
        index_s = sum_np.index(max1)
        print "\nHardest",type,":",grade_head[lab_name[index_s]]



def grade_scheme():
    col_final = []
    lab_name = []
    with open('grades.csv', 'r') as grades:
        reader = csv.reader(grades)
        grade_head = reader.next()          #get the headers of grades.csv

        for i, x in enumerate(grade_head):    # get a column number along with name and take the i value that has name
            if "Final Score" == x:
                lab_name.append(i)
            #save full column in col_final
        for col in reader:
            col_final.append(col[lab_name[0]][0:])

        # col_final is a list of numbers as strings. They are converted to float using float
        col_final_mapped = map(float, col_final)
        count_A = 0
        count_a = 0
        count_B_plus = 0
        count_b = 0
        count_b_minus = 0
        count_c_plus = 0
        count_c = 0
        count_c_minus = 0
        count_d_plus = 0
        count_d = 0
        count_d_minus = 0
        count_f = 0
        for i in col_final_mapped:
            if i >= 94.0 and i < 100.0:
                count_A = count_A + 1
            elif i >= 90.0 and i < 94.0:
                count_a = count_a + 1
            elif i >= 87.0 and i < 90.0:
                count_B_plus = count_B_plus + 1
            elif i >= 84.0 and i < 87.0:
                count_b = count_b + 1
            elif i >= 80.0 and i < 84.0:
                count_b_minus = count_b_minus + 1
            elif i >= 77.0 and i < 80.0:
                count_c_plus = count_c_plus + 1
            elif i >= 74.0 and i < 77.0:
                count_c = count_c + 1
            elif i >= 70.0 and i < 74.0:
                count_c_minus = count_c_minus + 1
            elif i >= 67.0 and i < 70.0:
                count_d_plus = count_d_plus + 1
            elif i >= 64.0 and i < 67.0:
                count_d = count_d + 1
            elif i >= 61.0 and i < 64.0:
                count_d_minus = count_d_minus + 1
            elif i >= 0.0 and i < 61.0:
                count_f = count_f + 1


        print "\nA:", count_A, "\nA-:", count_a, "\nB+:", count_B_plus,\
                "\nB:", count_b, "\nB-:", count_b_minus, "\nC+:", count_c_plus,\
                "\nC:", count_c, "\nC-:", count_c_minus, "\nD+:", count_d_plus,\
                "\nD:", count_d, "\nD-:", count_d_minus, "\nF:", count_f

def higher_grade():
    col_final = []
    lab_name = []
    with open('grades.csv', 'r') as grades:
        reader = csv.reader(grades)
        grade_head = reader.next()          #get the headers of grades.csv

        for i, x in enumerate(grade_head):    # get a column number along with name and take the i value that has name
            if "Final Score" == x:
                lab_name.append(i)
            #save full column in col_final
        for col in reader:
            col_final.append(col[lab_name[0]][0:])

        # col_final is a list of numbers as strings. They are converted to float using float
        col_final_mapped = map(float, col_final)
        count_A = 0
        for i in col_final_mapped:
            if (i >= 93.5 and i < 94.0) or (i>= 89.5 and i < 90.0) or \
                    (i>=86.5 and i < 87) or (i>=83.5 and i< 84) or (i>=79.5 and i <80.0) or \
                    (i>=76.5 and i<77.0) or (i>=73.5 and i<74.0) or (i>=69.5 and i<70) or \
                    (i>=66.5 and i<67.0) or (i>=63.5 and i<64) or (i>=60.5 and i<61.0):


                count_A = count_A + 1

        print "\n",count_A, "students will complain about their grade"

def few_grades():
    col_final = []
    number_of_studs = []


    lab_name = []
    with open('grades.csv', 'r') as grades:
        reader = csv.reader(grades)
        grade_head = reader.next()  # get the headers of grades.csv

        for i, x in enumerate(grade_head):  # get a column number along with name and take the i value that has name
            if "Final Score" == x:
                lab_name.append(i)
                # save full column in col_final
        for col in reader:
            col_final.append(col[lab_name[0]][0:])

        number_of_studs = float(len(col_final))
        col_final_mapped = map(float, col_final)
        col_sorted = sorted(col_final_mapped)
                #Division of people -- A Grade
        grade_a = round((10.0 / 100.0)* (number_of_studs))
        grade_a_len = int((number_of_studs) - grade_a)
        cutoff_a = min(col_sorted[grade_a_len:])
                #Division--- B grade
        grade_b = round((20.0 / 100.0) * (number_of_studs))
        grade_b_len = int(grade_a_len - grade_b)
        cutoff_b = min(col_sorted[grade_b_len:grade_a_len])
                #Division --- C grade
        grade_c = round((30.0 / 100.0) * (number_of_studs))
        grade_c_len = int(grade_b_len - grade_c)
        cutoff_c = min(col_sorted[grade_c_len:grade_b_len])
                #Division --- D grade
        grade_d = round((30.0 / 100.0) * (number_of_studs))
        grade_d_len = int(grade_c_len - grade_d)
        cutoff_d = min(col_sorted[grade_d_len :grade_c_len ])
                #Division---F grade
        cutoff_f = min(col_sorted[0:grade_d_len])


        print "\nA:",cutoff_a
        print "B:", cutoff_b
        print "C:", cutoff_c
        print "D:", cutoff_d
        print "F:", cutoff_f

if __name__ == '__main__':
     scores()
     hardest_assignment("Homework")
     hardest_assignment("Lab")
     grade_scheme()
     higher_grade()
     few_grades()
