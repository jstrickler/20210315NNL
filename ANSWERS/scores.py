#!/usr/bin/env python

FILE_NAME = "../DATA/testscores.dat"

def main():
    student_data = read_data()
    display_grades(student_data)
    print_average(student_data)

def read_data():
    scores_by_student = {}

    with open(FILE_NAME) as scores_in:
        for line in scores_in:
            name, score = line.split(":")
            score = int(score)
            # calculate here
            scores_by_student[name] = score

    return scores_by_student

def by_value(element_tuple):
    return element_tuple[1]

def calculate_grade(score):
    grade = None
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def display_grades(data):
    for student, score in sorted(data.items(), key=by_value, reverse=True):
        grade = calculate_grade(score)
        print("{:20s} {} {}".format(student, score, grade))

def get_average_score(data):
    sum_of_scores = sum(data.values())
    average = sum_of_scores/len(data)
    return average

def print_average(data):
    average = get_average_score(data)
    print("\naverage score is  {:.2f}\n".format(average))

main()
