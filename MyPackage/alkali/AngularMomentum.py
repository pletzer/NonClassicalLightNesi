# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:02:24 2023

@author: Alex Elliott
"""
import numpy as np
import sys


def Wigner3j(j1,j,j2,m1,m,m2):
    
    """ 
    Returns Wigner 3j symbol for coupling between two states due to 
    a light field, with the form: 
                                    (j1 j2 j3)
                                    (m1 m2 m3)
    ----------
    j1 : scalar
        Total angular momentum of initial atomic state.
    j2 : scalar
        Total angular momentum of coupling (=1 for a photon).
    j3 : scalar
        Total angular momentum of final atomic state.
    m1 : scalar
        Projected angular momentum of initial atomic state.
    m2 : scalar
        Projected angular momentum of coupling (=0,\pm1 for a photon).
    m3 : scalar
        Projected angular momentum of final atomic state.
    Returns
    W3j      : scalar
    Value of Wigner 3j symbol
    """
    try:
        if (m1+m+m2!=0) or (abs(j1-j)>j2) or (j1+j<j2):
            # print('oops')
            W3j = 0
        else:
            def Delt(a,b,c):
                Delt = np.sqrt(np.math.factorial(int(a+c-b))*np.math.factorial(int(a-c+b))*np.math.factorial(int(-a+c+b))\
                               /np.math.factorial(int(a+c+b+1))) 
                return Delt
            # print(j+m,j-m,j1-m-m2,j1+m+m2)
            term1 = Delt(j1,j2,j) * np.sqrt(np.math.factorial(j2-m2)*np.math.factorial(j2+m2)\
                             /(np.math.factorial(j+m)*np.math.factorial(j-m)*np.math.factorial(j1-m-m2)*np.math.factorial(j1+m+m2)))
            u = j - j1 + j2
            zmax = int(np.min([(j+j2-m-m2),(j2-m2),u]))
            zmin = int(np.max([-(j1 + m+m2),-(j2 + m2-u ),0]))
            # print(zmin,zmax)
            term3 = 0
            if (zmax>=zmin):
                for z in range(zmin,zmax+1):
                    if (z>=0):
                        # print((j+j2-m-m2-z),(j2-m2-z),u-z,(j1 + m+m2)+z,(j2 + m2-u)+z,z)
                        # print(term3)
                        term3 += ((-1.0) ** (2*j -j1-m1 +z) * np.math.factorial(j+j2-m-m2-z) * np.math.factorial(j1 + m+m2+z)\
                            / (np.math.factorial(z)*np.math.factorial(j2-m2-z)*np.math.factorial(u-z)*np.math.factorial(j2 + m2-u + z)))
                        # print(term3)
            # print(term1,term3)
            W3j = term1 * term3
    except:
        W3j=0    
    return W3j


def Wigner6j(a, b, c, d, e, f):
    
    """ 
    Returns Wigner 6j symbol for coupling between two states due to 
    a light field, with the form: 
                                    {a b c}
                                    {d e f}
    ----------
    a : scalar
        Total angular momentum of initial atomic state.
    b : scalar
        Total angular momentum of coupling (=1 for a photon).
    c : scalar
        Total angular momentum of final atomic state.
    d : scalar
        Projected angular momentum of initial atomic state.
    e : scalar
        Projected angular momentum of coupling (=0,\pm1 for a photon).
    f : scalar
        Projected angular momentum of final atomic state.
    Returns
    W3j      : scalar
    Value of Wigner 6j symbol
    """
    if (a<abs(b-c)) or (a>b+c):
        Wig6j =0
    else:
        try:
            def Delt(a,b,c):
                Delt = np.sqrt(np.math.factorial(int(a+c-b))*np.math.factorial(int(a-c+b))*np.math.factorial(int(-a+c+b))\
                               /np.math.factorial(int(a+c+b+1))) 
                return Delt
            
            term1num = (-1) ** (b+c+e+f) * Delt(a,b,c) * Delt(a,e,f) * Delt(c,d,e) * Delt(b,d,f)\
                     * np.math.factorial(int(a+b+c+1)) * np.math.factorial(int(b+d+f+1))
            term1den = np.math.factorial(int(a+b-c)) *np.math.factorial(int(c-d+e))*np.math.factorial(int(c+d-e))\
                      *np.math.factorial(int(a-e+f))*np.math.factorial(int(-a+e+f))*np.math.factorial(int(b+d-f))
            term1 = term1num/term1den
            
            zmax =int( np.min([(2*b),(b+c-e+f),(b+c+e+f+1),(-a+b+c),(b-d+f),(a+b+c+1),(b+d+f+1)]))
            zmin = 0;
            if (zmax>=zmin):
                # print(zmin,zmax)
                term2 = 0
                for z in range(zmin,zmax+1):
                    # print(z)
                    if (z>=0):
                        term2num = (-1) ** z * np.math.factorial(int(2*b-z))* np.math.factorial(int(b+c-e+f-z))* np.math.factorial(int(b+c+e+f+1-z))
                        term2den = np.math.factorial(z)*np.math.factorial(int(-a+b+c-z))* np.math.factorial(int(b-d+f-z))* np.math.factorial(int(a+b+c+1-z))* np.math.factorial(int(b+d+f+1-z))
                        
                        term2 = term2 + term2num/term2den
            else: 
                term2 = 0
            Wig6j = term1 * term2
        except:
            print(a,b,c,d,e,f)
    return Wig6j



def BranchingRatio(F,Fp,J,Jp,L,Lp,mF,mFp,S=1/2,I=3/2):
    term1 = (2*L+1) * (2*Lp + 1) * (2*J+1) * (2*Jp+1) * (2*F+1) * (2*Fp+1)
    term2 = Wigner6j(Lp,Jp,S,J,L,1)**2 \
            * Wigner6j(Jp,Fp,I,F,J,1)**2\
             * Wigner3j(Fp,1,F,-mFp,mFp-mF,mF)**2
    brat = term1 * term2
    return brat

def TransitionDipoleMoment(F,Fp,mF,mFp,J,Jp,I,q):
    TDmoment = (-1)**(2*Fp + J + I + mF)\
        * np.sqrt((2*F+1)*(2*Fp+1)*(2*J+1))\
        * Wigner3j(Fp,1,F,mFp,q,-mF)\
            * Wigner6j(J,Jp,1,Fp,F,I)
    return TDmoment
