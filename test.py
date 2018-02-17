#!/usr/bin/env python

import csv
import numpy as np
import pandas as pd
import re

def scores():
    col_final = []
    number_of_studs = []
    lab_name = []
    with open('grades.csv', 'r') as grades:
        reader = csv.reader(grades)
        grade_head = reader.next()    #get the headers of grades.csv
        #j = str(grade_head)
        print grade_head
        #matching = [s for s in grade_head if "Final Score" in s]
        #print matching
        for i, x in enumerate(grade_head):    # get a column number along with name and take the i value that has name
            print i, x
            if "Final Score" == x:
                lab_name.append(i)        #get indices of Final Score into lab_name
        print lab_name
        for col in reader:
            col_final.append(col[lab_name[-1]][0:])
        print col_final
        number_of_studs = float(len(col_final))    # we get 164 as length of the column is 164


if __name__ == '__main__':
    scores()

'''
with open('grades.csv', 'r') as grades:
    reader = csv.reader(grades)
    grade_head = reader.next()
    j = str(grade_head)
    print grade_head
    matching = [s for s in grade_head if "Lab" in s]
    print matching
    for i,x in enumerate(grade_head):
        #print i, x
        if "Lab" in x:
            print i


    # gen = (i for i, x in enumerate(grade_head) if x == matching)
    # for i in gen:
    #     print i
    # #rest = [row for row in reader]
    # if 'Student' in i:
    #
    #     print "True"

'''