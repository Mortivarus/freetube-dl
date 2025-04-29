#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 14:34:19 2025

@author: mortivarus
"""     
     
def write_file(file, lst):
    with open(f'{file}.txt', 'w') as f:
        for item in lst:
            f.write(item + '\n')