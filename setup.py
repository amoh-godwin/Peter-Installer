# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:51:01 2019

@author: Ampofo
"""

import os
import subprocess
import sys

path = os.chdir(os.path.join(os.getcwd(), 'installer'))
print(path)
subprocess.Popen('installer.exe', shell=True)

sys.exit(0)
