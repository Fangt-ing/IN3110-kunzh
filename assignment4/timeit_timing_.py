from ast import expr_context
import test_slow_rectangle as tr
import timeit as tt
import numpy as np
import math


tml=[]
tm1=[]
tm2=[]
tm3=[]

def getlist(textfile):
    wordlist=[]
    with open(textfile) as fm:
        for words in fm.readlines():
            for word in words.split():
                wordlist.append(word.strip('.'))
    return wordlist
manualist=getlist('manual_report.txt')

numl=[]
for word in manualist:
    try:
        number=float(word)
        numl.append(number)
    except ValueError:
        pass

stp='import test_slow_rectangle as tr'
with open('timeit_report.txt', 'w') as f:
    rdt = tt.repeat(stmt='tr.random_array(1e5)', setup=stp, number=1, repeat=5)
    for i in range(len(rdt)):
        f.write('Time consumed for random array is ' + str(rdt[i]) + '.\n')
        f.write('Time costed in manual_timing is ' + str(numl[i]) + '.\n')
    tml=np.append(tml, rdt)
    f.write('\n')
        
    lpt = tt.repeat('tr.loop(tr.random_array(1e5))', stp, number=1, repeat=5)
    for i in range(len(rdt)):
        f.write('Time consumed for loop array is ' + str(lpt[i]) + '.\n')
        f.write('Time costed in manual_timing is ' + str(numl[5+i]) + '.\n')
    tml=np.append(tml, lpt)
    f.write('\n')
        
    snt = tt.repeat('tr.snake_loop(tr.random_array(1e5))', stp, number=1, repeat=5)
    for i in range(len(rdt)):
        f.write('Time consumed for snake array is ' + str(snt[i]) + '.\n')
        f.write('Time costed in manual_timing is ' + str(numl[5*2+i]) + '.\n')
    tml=np.append(tml, snt)
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