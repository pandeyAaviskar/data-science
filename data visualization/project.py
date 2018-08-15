import csv
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

fName='data.py'
q=1
c=0
while q==1:
    print('---enter 3 colomns name---\n')
    c1=input('first col name:')
    c2=input('second col name:')
    c3=input('third col name:')
    print('\n\n')

    print('---enter 3 data---\n')
    d11=int(input('first col data:'))
    d12=int(input('second col data:'))
    d13=int(input('third col data:'))
    print('\n\n')

    print('---enter 3 data---\n')
    d21=int(input('first col data:'))
    d22=int(input('second col data:'))
    d23=int(input('third col data:'))
    print('\n\n')
    dic={c1:[d11,d21],c2:[d12,d22],c3:[d13,d23]}
    dic=pd.DataFrame(dic)

    dic.plot(kind='bar')
    plt.show()
    c+=1

    q=int(input('press 1 to continue or any other key to exit:'))
    
                
#if c==1:
    with open(os.path.dirname(os.path.abspath(__file__))+'/'+fName, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([c1, c2, c3])
        writer.writerow([d11, d12, d13])
        writer.writerow([d21, d22, d23])
'''else:
    with open(os.path.dirname(os.path.abspath(__file__))+'/'+fName, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([c1, c2, c3])
        writer.writerow([d11, d12, d13])
        writer.writerow([d21, d22, d23])'''
