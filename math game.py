from random import randrange
import math
level = int(input("level (1 | 2 | 3): "))
operator,x,tries = ["*","/","-","+"],[],3
op = operator[randrange(0,3)]

if level == 1:
    x.append(randrange(0,9))
    x.append(op)
    x.append(randrange(0,9))
    
if level == 2:
    x.append(randrange(10,99))
    x.append(op)
    x.append(randrange(10,99))
    
if level == 3:
    x.append(randrange(100,999))
    x.append(op)
    x.append(randrange(100,999))

if "*" in x:
    final = round(x[0] * x[2],2)
    
if "/" in x:
    final = round(x[0] / x[2],2)
    
if "-" in x:
    final = round(x[0] - x[2],2)
    
if "+" in x:
    final = round(x[0] + x[2],2)

while tries != 0:
    print(f"{x[0]} {x[1]} {x[2]}")
    ans = float(input("Answer: "))
    if ans == final:
        print('correct')
        break
    else:
        tries -= 1
if tries == 0:
    print(f"you lost, answer was {final}" )