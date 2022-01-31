# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# A script to generate exercises to train oneself in factoring
# using the completing the square method

import random
import fractions
import math

wholeNumbers = False
numExercises = 20

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if ((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

i = 0
while (i < numExercises):
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
    x1 = fractions.Fraction(n1, d1)
    if (x1.denominator == 1 and not(wholeNumbers)):
        continue
    x2 = fractions.Fraction(n2, d2)
    if (x1.denominator == 1 and not(wholeNumbers)):
        continue
    if (wholeNumbers):
        a = random.randint(-10,10)
    else:
        a = lcm(x1.denominator, x2.denominator)
    # We want slightly less negative numbers
    s = bool(not(random.randint(0,2)))
    if (s):
        a*=-1
    b = (int)((x1+x2)*a)
    c = (int)(x1*x2*a)
    if (not(b) or not(c)):
        continue
    i+=1
    print(str(i)+".\t"+("-" if (a < 0) else ""), "" if (abs(a)==1) else abs(a), "x²"," - " if (b < 0) else " + ",  "" if (abs(b) == 1) else abs(b), "x", " - " if (c < 0) else " + ", abs(c), sep="")
    print(str(i)+".\t\tResult:\t",  "-" if (a < 0) else "", "" if (abs(a)==1) else abs(a),"(x", " - " if (x1 < 0) else " + ", abs(x1),")", "(x", " - " if (x2 < 0) else " + ", abs(x2),")", sep="")  
    
