# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:41:28 2023

@author: aell060
"""

import qutip as qt
import numpy as np
import time

start_time=time.time()
natoms = 1

eps = 1
g = 1
kappa = 1/2
gamma = 1

Ncav = 15
Nat = 2

dt = 1/100
tmax = 100
tlist = np.arange(0,tmax+dt,dt)

idcav = qt.qeye(Ncav); idatom = qt.qeye(Nat)

if (natoms ==1):
    a = qt.tensor(qt.destroy(Ncav),idatom)
    sm = qt.tensor(idcav,qt.sigmam())
    
    H = g * (a.dag() * sm + sm.dag() * a) + eps * (a.dag() + a )
    c_ops = [np.sqrt(2*kappa)*a,np.sqrt(gamma) * sm]
    
    rhoss = qt.steadystate(H,c_ops)
    print("Cavity mode commutator = {}".format(np.round(qt.expect(a*a.dag()-a.dag()*a,rhoss),5)))
    rho0 = qt.mesolve(H,rhoss,tlist,c_ops,progress_bar=True)
    print('done')
    qt.hinton(rho0.states[-1])
    qt.hinton(rho0.states[-1].ptrace(0))
    qt.hinton(rho0.states[-1].ptrace(1))
elif (natoms ==2):
    a = qt.tensor(qt.destroy(Ncav),idatom,idatom)
    sm = qt.tensor(idcav,qt.sigmam(),idatom)
    sm2 = qt.tensor(idcav,idatom,qt.sigmam())
    
    H = g * (a.dag() * sm + sm.dag() * a) + g * (a.dag() * sm2 + sm2.dag() * a)+ eps * (a.dag() + a )
    c_ops = [np.sqrt(2*kappa)*a,np.sqrt(gamma) * sm,np.sqrt(gamma) * sm2]
    
    rhoss = qt.steadystate(H,c_ops)
    print("Cavity mode commutator = {}".format(np.round(qt.expect(a*a.dag()-a.dag()*a,rhoss),5)))
    rho0 = qt.mesolve(H,rhoss,tlist,c_ops,progress_bar=True)
    print('done')
    qt.hinton(rho0.states[-1])
    qt.hinton(rho0.states[-1].ptrace(0))
    qt.hinton(rho0.states[-1].ptrace(1))
    qt.hinton(rho0.states[-1].ptrace(2))
elif (natoms ==4):
    a = qt.tensor(qt.destroy(Ncav),idatom,idatom,idatom,idatom)
    sm = qt.tensor(idcav,qt.sigmam(),idatom,idatom,idatom)
    sm2 = qt.tensor(idcav,idatom,qt.sigmam(),idatom,idatom)
    sm3 = qt.tensor(idcav,idatom,idatom,qt.sigmam(),idatom)
    sm4 = qt.tensor(idcav,idatom,idatom,idatom,qt.sigmam())
    
    H = g * (a.dag() * sm + sm.dag() * a) + g * (a.dag() * sm2 + sm2.dag() * a)\
        +g * (a.dag() * sm3 + sm3.dag() * a) + g * (a.dag() * sm4 + sm4.dag() * a)\
        + eps * (a.dag() + a )
    c_ops = [np.sqrt(2*kappa)*a,np.sqrt(gamma) * sm,np.sqrt(gamma) * sm2\
             ,np.sqrt(gamma) * sm3,np.sqrt(gamma) * sm4]
    
    rhoss = qt.steadystate(H,c_ops)
    print("Cavity mode commutator = {}".format(np.round(qt.expect(a*a.dag()-a.dag()*a,rhoss),5)))
    rho0 = qt.mesolve(H,rhoss,tlist,c_ops,progress_bar=True)
    print('done')
    qt.hinton(rho0.states[-1])
    qt.hinton(rho0.states[-1].ptrace(0))
    qt.hinton(rho0.states[-1].ptrace(1))
    qt.hinton(rho0.states[-1].ptrace(2))
else:
    print("You chose and invalid number of atoms (1,2, or 4 allowed).")
total_time = np.round(time.time()-start_time,2)
print("Time taken = {}s.".format(total_time))