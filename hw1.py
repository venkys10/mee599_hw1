#!/usr/bin/env python

import csv
import numpy as np
import pandas as pd
import re

def scores():
    col_final = []
    number_of_studs = []
    with open('grades.csv', 'r') as grades:
        for row in grades:
            if "Final Score" in row[0:]
        re.search()
        # data_reader = csv.reader(grades)
        # next(data_reader, None)   #removes column headers
        for line in data_reader:
            col_final.append(line[91][0:]) #the column headed "Final Score" is appended to col_final
            number_of_studs.append(line[0][0:])  # number of students are appended

        number_studs = map(float, number_of_studs)
        #col_final is a list of numbers as strings. They are converted to float using float
        col_final_mapped = map(float, col_final)
        sum_final = sum(col_final_mapped)

                    #Average score
        average_final = sum_final / float(len(number_studs))

        #check for above average and below average-----------------------
        count_above = 0
        count_below = 0
        for i in col_final_mapped:
            if i > average_final:
                count_above = count_above + 1
            else:
                count_below = count_below + 1
                    #print percentage of people
        percentage_above = (count_above / float(len(number_studs))) * 100

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
        percentage_median = (count_med / float(len(number_studs))) * 100
        print "Average score:", round(average_final, 2), "\nAbove Average:", round(percentage_above,2),"%", \
                        "\nMedian Score", median_final, "\nAbove Median:", round(percentage_median,2),"%"
        #return average_final, percentage_above, median_final, percentage_median


def hardest_assignment():
    lab = []
    lab1 = []
    grades = open('grades.csv', 'r')
    data_reader = csv.reader(grades)
    next(data_reader, None)  # removes column headers

    for i in range(0,4):
        for line in data_reader:
            #for i in range(1, 11):

            lab.append(line[i][0:])  # the column headed "Final Score" is appended to col_final
            #if len(lab) % 164 == 0:
            sum_assi1 = sum(map(float, lab))
            lab1.append(sum_assi1)

        print lab
    print "\n", lab1
    print len(lab)
    print len(lab1)


    # df = pd.read_csv("grades.csv", header = None)
    # test1 = df.Student
    # print test1

def grade_scheme():
    col_final = []
    with open('grades.csv', 'r') as grades:
        data_reader = csv.reader(grades)
        next(data_reader, None)  # removes column headers
        for line in data_reader:
            col_final.append(line[91][0:])  # the column headed "Final Score" is appended to col_final

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
        #
        # percentage_a = (count_A / float(len(number_studs))) * 100
        # percentage_a_minus = (count_a / float(len(number_studs))) * 100
        # percentage_B_plus = (count_B_plus / float(len(number_studs))) * 100
        # percentage_b = (count_b / float(len(number_studs))) * 100
        # percentage_b_minus = (count_b_minus / float(len(number_studs))) * 100
        # percentage_c_plus = (count_c_plus / float(len(number_studs))) * 100
        # percentage_c = (count_c / float(len(number_studs))) * 100
        # percentage_c_minus = (count_c_minus / float(len(number_studs))) * 100
        # percentage_d_plus = (count_d_plus / float(len(number_studs))) * 100
        # percentage_d = (count_d / float(len(number_studs))) * 100
        # percentage_d_minus = (count_d_minus / float(len(number_studs))) * 100
        # percentage_f = (count_f / float(len(number_studs))) * 100

        print "A:", count_A, "\nA-:", count_a, "\nB+:", count_B_plus,\
                "\nB:", count_b, "\nB-:", count_b_minus, "\nC+:", count_c_plus,\
                "\nC:", count_c, "\nC-:", count_c_minus, "\nD+:", count_d_plus,\
                "\nD:", count_d, "\nD-:", count_d_minus, "\nF:", count_f

def higher_grade():
    col_final = []
    with open('grades.csv', 'r') as grades:
        data_reader = csv.reader(grades)
        next(data_reader, None)  # removes column headers
        for line in data_reader:
            col_final.append(line[91][0:])  # the column headed "Final Score" is appended to col_final

        # col_final is a list of numbers as strings. They are converted to float using float
        col_final_mapped = map(float, col_final)
        count_A = 0
        for i in col_final_mapped:
            if (i >= 93.5 and i < 94.0) or (i>= 89.5 and i < 90.0) or \
                    (i>=86.5 and i < 87) or (i>=83.5 and i< 84) or (i>=79.5 and i <80.0) or \
                    (i>=76.5 and i<77.0) or (i>=73.5 and i<74.0) or (i>=69.5 and i<70) or \
                    (i>=66.5 and i<67.0) or (i>=63.5 and i<64) or (i>=60.5 and i<61.0):


                count_A = count_A + 1

        print count_A, "students will complain about their grade"

def few_grades():
    col_final = []
    number_of_studs = []
    grade_a_sorted = []
    with open('grades.csv', 'r') as grades:
        data_reader = csv.reader(grades)
        next(data_reader, None)  # removes column headers
        for line in data_reader:
            col_final.append(line[91][0:])  # the column headed "Final Score" is appended to col_final
            number_of_studs.append(line[0][0:])  # number of students are appended

        number_studs = map(float, number_of_studs)
        col_final_mapped = map(float, col_final)
        col_sorted = sorted(col_final_mapped)
                #Division of people -- A Grade
        grade_a = round((10.0 / 100.0)* len(number_studs))
        grade_a_len = int(len(number_studs) - grade_a)
        cutoff_a = min(col_sorted[grade_a_len:])
                #Division--- B grade
        grade_b = round((20.0 / 100.0) * len(number_studs))
        grade_b_len = int(grade_a_len - grade_b)
        cutoff_b = min(col_sorted[grade_b_len:grade_a_len])
                #Division --- C grade
        grade_c = round((30.0 / 100.0) * len(number_studs))
        grade_c_len = int(grade_b_len - grade_c)
        cutoff_c = min(col_sorted[grade_c_len:grade_b_len])
                #Division --- D grade
        grade_d = round((30.0 / 100.0) * len(number_studs))
        grade_d_len = int(grade_c_len - grade_d)
        cutoff_d = min(col_sorted[grade_d_len :grade_c_len ])
                #Division---F grade
        cutoff_f = min(col_sorted[0:grade_d_len])


        print "A:",cutoff_a
        print "B:", cutoff_b
        print "C:", cutoff_c
        print "D:", cutoff_d
        print "F:", cutoff_f

if __name__ == '__main__':
     #scores()
     #hardest_assignment()
     #grade_scheme()
     #higher_grade()
     few_grades()
