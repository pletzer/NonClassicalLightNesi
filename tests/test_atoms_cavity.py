# -*- coding: utf-8 -*-
"""
Unit tests

"""

#%% Imports
import qutip as qt
import numpy as np
import pytest

def test_atom_cavity():

  # Assign parameters
  eps = 1
  g = 1
  kappa = 0.5
  gamma = 1

  # Get basis size
  Ncav = 15
  Natom = 1

  # Build solve times
  dt = 0.01
  tmax = 10
  tlist = np.arange(0,tmax+dt,dt)

  #%% Build Hamiltonian
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
  cavityModeCommutator = np.round(qt.expect(a*a.dag()-a.dag()*a,rhoss),5)
  print(f"Cavity mode commutator = {cavityModeCommutator}")
  assert abs(cavityModeCommutator - 0.99993) < 1.e-10
