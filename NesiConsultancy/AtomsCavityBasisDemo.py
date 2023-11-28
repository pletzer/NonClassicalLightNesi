# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:41:28 2023

@author: aell060
"""

#%% Imports
import qutip as qt
import numpy as np
import matplotlib.pyplot as plt
import time
import configparser
import argparse
import sys

parser = argparse.ArgumentParser(
                    prog=sys.argv[0],
                    description='NeSI test case')
parser.add_argument('-c', '--conffile', default='config.ini',
                    help='Path to the configuration file')
args = parser.parse_args()

#%% Read in configs
configs = configparser.ConfigParser()
conffile = args.conffile
try:
    with open(conffile) as f:
        configs.read(conffile)
except IOError:
    raise RuntimeError(f'Config file {conffile} does not exist!')

# Assign parameters
eps = configs['PARAMS'].getfloat('eps')
g = configs['PARAMS'].getfloat('g')
kappa = configs['PARAMS'].getfloat('kappa')
gamma = configs['PARAMS'].getfloat('gamma')

# Get basis size
Ncav = configs['PARAMS'].getint('Ncav')
Natom = configs['PARAMS'].getint('Natom')

# Build solve times
dt = configs['TIMES'].getfloat('dt')
tmax = configs['TIMES'].getfloat('tmax')
tlist = np.arange(0,tmax+dt,dt)

#%% Build Hamiltonian
start_time=time.time()

atomI = qt.tensor([qt.qeye(2) for i in range(Natom)])
cavI = qt.qeye(Ncav)

sm = [qt.tensor([qt.sigmam() if j==i else qt.qeye(2) for j in range(Natom)]) for i in range(Natom)]
sm = [qt.tensor(cavI,i) for i in sm]

a = qt.tensor(qt.destroy(Ncav),atomI)
c_ops = [np.sqrt(2*kappa)*a]

H = eps*(a + a.dag())
for i in range(Natom):
    H = H + g*(a.dag()*sm[i] + a*sm[i].dag())
    c_ops.append(np.sqrt(gamma)*sm[i])
    
#%% Solve master equation
rhoss = qt.steadystate(H,c_ops)
print("Cavity mode commutator = {}".format(np.round(qt.expect(a*a.dag()-a.dag()*a,rhoss),5)))
rho0 = qt.mesolve(H,rhoss,tlist,c_ops,progress_bar=True)
solve_time = np.round(time.time()-start_time,2)
print("Time taken till solver = {}s.".format(solve_time))

fig0,ax0 = qt.hinton(rho0.states[-1])
fig1,ax1 = qt.hinton(rho0.states[-1].ptrace(0))
qt.hinton(rho0.states[-1].ptrace(1))
if Natom >=2:
    qt.hinton(rho0.states[-1].ptrace(2))

#%% Save figure
plt.figure(fig1)
plt.savefig(configs['OUTPUTS']['savefig'],format='png',bbox_inches='tight')
total_time = np.round(time.time()-start_time,2)
print("Total time taken = {}s.".format(total_time))