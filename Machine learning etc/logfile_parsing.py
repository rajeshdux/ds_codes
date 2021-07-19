import pandas as pd
import re

with open('log_file.txt') as file:
    lines = file.readlines()[7:]
    newlines = []
    i_c = 0
    w_c = 0
    for i in lines:
        newlines.append(str(i.split('\n')))

        for i in newlines:
            m=re.search('[A-Z]+',i)
    print(m.match())
    #         if e=='INFO':
    #             i_c+=1
    #         else: w_c+=1
    #
    # print('INFO count:',i_c)
    # print('WARN count:',w_c)
