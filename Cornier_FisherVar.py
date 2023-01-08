#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 17:40:11 2023

@author: fabioribeiro
"""


import scipy.stats as st

def Cornish_FisherVar(x,skew,kurt):
    z=st.norm.ppf(x)+1/6*(st.norm.ppf(x)**2-1)*(skew)+1/24*(st.norm.ppf(x)**3-3*st.norm.ppf(x))*(kurt-3)-1/36*(2*st.norm.ppf(x)**3-5*st.norm.ppf(x))*(skew**2)
    return z
Cornish_FisherVar(0.975, -0.4, 3.3)



 
st.norm.ppf(0.975)+1/6*(st.norm.ppf(0.975)**2-1)*(-0.4)+1/24*(st.norm.ppf(0.975)**3-3*st.norm.ppf(0.975))*(3.3-3)-1/36*(st.norm.ppf(0.975)**3-5*st.norm.ppf(0.975))*(-0.4**2)
