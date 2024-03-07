import os
import shutil
import numpy as np
from target import calc_gen
def cubic_pre():
    #===========C11_C12_I===============
    con=['C11_C12_I','C11_C12_II','C44']
    no_const=len(con)
    for folder in con:
     file='output.txt'
     cwd=os.getcwd()
     li=os.listdir()
     if folder in li:
         shutil.rmtree(cwd+'/'+folder)
     if file in li:   
         os.remove('output.txt')
     os.mkdir(folder)
     with open('strain.dat') as f:
         st = f.readlines()
     f.close()
     st[0]= st[0].strip().rstrip("\n")
     strain=st[0].split(",")
     for i in range(0,len(strain)):
       num=float(strain[i])
       os.mkdir(folder+'/'+'strain_'+strain[i])
       if folder=='C11_C12_I':
           calc_gen(num,-1*num,0.0,0.0,0.0,0.0)
       elif folder=='C11_C12_II':
           calc_gen(num,num,num,0.0,0.0,0.0)
       elif folder=='C44':
           calc_gen(0,0,0,num,num,num)
    
       shutil.copy(cwd+"/output.txt",cwd+"/"+folder+"/"+"strain_"+strain[i]+"/POSCAR")
       os.remove('output.txt')
    return
