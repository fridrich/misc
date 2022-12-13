#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# A script to generate exercises to train oneself in factoring
# using the completing the square method

# Usage:
#   python3 completing_square_exercises.py >exercises.txt

import random
import fractions
import math
import argparse

class Exercise:
    x1: fractions.Fraction
    x2: fractions.Fraction
    a: fractions.Fraction
    b: fractions.Fraction
    c: fractions.Fraction

# compute lowest common multiple of two numbers
def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if (not(greater % x) and not(greater % y)):
           lcm = greater
           break
       greater += 1

   return lcm

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fractions", action="store_true", dest="fractions",
                    help="Resultats should be whole numbers or fractions?")
parser.add_argument("-n", "--number-exercises", dest="numex", type=int, default=20,
                    help="Number of exercises to generate", metavar='N')
args = parser.parse_args()

wholeNumbers = not(args.fractions);
numExercises = args.numex

exercises = []

i = 0
while (i < numExercises):
    exercise = Exercise()
    n1 = random.randint(-20, 20)
    if (wholeNumbers):
        d1 = 1
    else:
        d1 = random.randint(-9, 9)
    n2 = random.randint(-20, 20)
    if (wholeNumbers):
        d2 = 1
    else:
        d2 = random.randint(-9, 9)
    if (not(n1) or not(n2) or not(d1) or not(d2)):
        continue
    exercise.x1 = fractions.Fraction(n1, d1)
    if (exercise.x1.denominator == 1 and not(wholeNumbers)):
        continue
    exercise.x2 = fractions.Fraction(n2, d2)
    if (exercise.x2.denominator == 1 and not(wholeNumbers)):
        continue
    if (wholeNumbers):
        exercise.a = fractions.Fraction(random.randint(1,10), 1)
    else:
        exercise.a = lcm(exercise.x1.denominator, exercise.x2.denominator)
    # We want slightly less negative numbers
    s = bool(not(random.randint(0,2)))
    if (s):
        exercise.a*=-1
    exercise.b = (exercise.x1+exercise.x2)*exercise.a
    exercise.c = exercise.x1*exercise.x2*exercise.a
    if (not(exercise.b) or not(exercise.c)):
        continue
    if (exercise.c.denominator > 1):
        exercise.a *= exercise.c.denominator;
        exercise.b *= exercise.c.denominator;
        exercise.c *= exercise.c.denominator;
    exercises.append(exercise)
    i+=1

print("Exercises\n")
i = 0
for exercise in exercises:
    a = exercise.a
    b = exercise.b
    c = exercise.c
    i+=1
    print(str(i), ".\t", "-" if (a < 0) else "", "" if (abs(a)==1) else abs(a), "x²"," - " if (b < 0) else " + ",  "" if (abs(b) == 1) else abs(b), "x", " - " if (c < 0) else " + ", abs(c), sep="")
 
print("\fResults\n")
i = 0
for exercise in exercises:
    a = exercise.a
    x1 = exercise.x1
    x2 = exercise.x2
    i+=1
    print(str(i), ".\t", "-" if (a < 0) else "", "" if (abs(a)==1) else abs(a),"(x", " - " if (x1 < 0) else " + ", abs(x1),")", "(x", " - " if (x2 < 0) else " + ", abs(x2),")", sep="")  
