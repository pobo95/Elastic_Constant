import os
import shutil
import numpy as np
from coefficient import coeff
import average
def cubic_post():
    cwd=os.getcwd()
    os.chdir(cwd+"/"+"C11_C12_I/")
    c11_c12_I=coeff()
    os.chdir(cwd+"/"+"C11_C12_II/")
    c11_c12_II=coeff()
    os.chdir(cwd+"/"+"C44/")
    c44=coeff()
    bulk=c11_c12_II*2/9
    shear=c11_c12_I*0.5
    C11=(3*bulk+4*shear)/3
    C12=(3*bulk-2*shear)/3
    C44=2*c44/3
    
    print("second order coefficients are as follow:")
    print("C11_C12_I/=",c11_c12_I,"\nC12/=",c11_c12_II,"\nC44/=",c44)
    print('''
    ===== Methodology =====
    Bulk=(C11_C12_II/) x 2/9
    shear=(C11_C12_I/) x 1/2
    C11=(3xbulk+4xshear)/3
    C12=(3xbulk-2xshear)/3
    C44=2/3 x C44/
           ''')
    print("C11=",C11,"\nC12=",C12,"\nC44=",C44,"\nbulk_modulus=",bulk)
    print('''
    ==== stiffness matrix ====''')
    stiffness=np.array([[C11,C12,C12,0,0,0],[C12,C11,C12,0,0,0],[C12,C12,C11,0,0,0],[0,0,0,C44,0,0],[0,0,0,0,C44,0],[0,0,0,0,0,C44]])
    print(np.around(stiffness,decimals=2))

    print('''
    check stability criteria
    C11−C12 > 0 ; C11+2C12 > 0 ; C44 > 0
         ''')
    #checking stability
    a=C11-C12
    b=C11+2*C12
    c=C44
    if (a>0)and(b>0)and(c>0):
        print("\033[1m"+"\033[1;32m structure is mechanically stable"+"\033[0m")
    else:
        print("\033[1m"+"\033[1;32m structure is mechanically unstable"+"\033[0m")
    average.avg(stiffness)
    return stiffness
