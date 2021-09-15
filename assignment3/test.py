from optparse import Values


def array(*values):
    l=[]
    for i in values:
        l = l.append(values[i])
    print(l)

array(3, 3, 5, 7)