#!/usr/bin/env python

import csv

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

