import manual_timing_ as mlt
import timeit_timing_ as ttt


def getfncname(fncindex):
    if fncindex+1 == 1:
        fncname='random_array()'
    elif fncindex+1 == 2:
        fncname='loop()'
    elif fncindex+1 == 3:
        fncname='snake_loop()'
    return fncname

mltfncname=getfncname(mlt.fncindex)
tttfncname=getfncname(ttt.fncindex)

with open('cProfile_report.txt', 'w') as f:
    f.write('The slowest function in manual_timing is ' + mltfncname + ' took {}s'.format(mlt.maxnum) + '\n')
    f.write('The slowest function in timeit_timing is ' + tttfncname + ' took {}s'.format(ttt.maxnum) + '\n')
