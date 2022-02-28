#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:38:25 2022

@author: tylertravis
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-15,15)
y = math.pi ** np.sin(x)
plt.plot(x,y, 'r', linestyle = 'dashed')
plt.title("Given Equation", rotation = 5, loc = 'left')
plt.savefig('equationimg.png')