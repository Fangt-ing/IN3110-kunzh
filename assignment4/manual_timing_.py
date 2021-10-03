# import test_slow_rectangle as tr
from test_slow_rectangle import random_array
from test_slow_rectangle import loop
from test_slow_rectangle import snake_loop
import time as tm
import numpy as np
import math


tml=[]
tm1=[]
tm2=[]
tm3=[]
with open('manual_report.txt', 'w') as f:
    for i in range(5):
        t10 = tm.time()
        random_array(1e5)
        t11 = tm.time()
        duration1 = t11-t10
        tm1.append(duration1)
        f.write('Time consumed to execute array round(' + str(i+1) + ')' + ' is ' + str(duration1) + '.\n')
    tml=np.append(tml, tm1)
    f.write('\n')

    for i in range(5):
        t20 = tm.time()
        loop(random_array(1e5))
        t21 = tm.time()
        duration2 = t21 - t20
        tm2.append(duration2)
        f.write('Time consumed to execute filtered_array round(' + str(i+1) + ')' + ' is {}.\n'.format(duration2))
    tml=np.append(tml, tm2)
    f.write('\n')

    for i in range(5):
        t30 = tm.time()
        snake_loop(random_array(1e5))
        t31 = tm.time()
        duration3 = t31 - t30
        tm3.append(duration3)
        f.write('Time consumed to execute filtered_array_snake round(' + str(i+1) + ')' + ' is {}.\n'.format(duration3))
    tml=np.append(tml, tm3)
    f.write('\n')

    maxnum=max(tml)
    maxindex=np.array(tml).argmax()
    fncindex=math.modf(maxindex/5)[1]
    roundindex=maxindex%5

    if fncindex+1 ==1:
        f.write('The slowest function is random_array(), took {}s'.format(maxnum) + 'at the round {}.\n'.format(roundindex+1))
    elif fncindex+1 ==2: 
        f.write('The slowest function is loop(), took {}s'.format(maxnum) + ' at the round {}.\n'.format(roundindex+1))
    elif fncindex+1 ==3:
        f.write('The slowest function is snake_loop(), took {}s'.format(maxnum) + ' at the round {}.\n'.format(roundindex+1))