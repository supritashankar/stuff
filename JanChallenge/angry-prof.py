"""
Problem Statement

Professor is conducting a course on Discrete Mathematics to a class of N students. He is angry at the lack of discipline shown by students and decided to cancel the class if there are less than K students present after the class starts.

Given the arrival time of each student, your task is to find out if the class gets cancelled or not.

Input Format

First line of the input contains T, the number of testcases to follow. 
Each testcase contains 2 lines. First line of each testcase contains 2 space separated integers N and K. 
Next line contains N space separated integers indicating the arrival time of each student.
s
If the arrival time of a given student is a non-positive integer (less than 0), then the student has entered the class before the class started. If the arrival time of a given student is a positive integer ( >0), the student entered the class after the class started. 
Class begins at time 0. 
If a student enters the class at time = 0, the student is considered to have entered the class before the start-time.

Example

Input
2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Output
YES
NO

For the first testcase, K=3, i.e., professor wants atleast 3 students to be in class but there are only 2 who have arrived on time ( -3, -1 ), hence the class gets gets cancelled. 
For the second testcase, K=2, i.e, professor wants atleast 2 students to be in class and there are 2 who have arrived on time (0, -1), hence the class does not get cancelled.
"""

k = raw_input()
n = []
k = []
for testcase in k:
	n.append(raw_input())
	k.append(raw_input())
	for student in n:
		data.append(raw_input())