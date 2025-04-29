#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 12:41:50 2025

@author: mortivarus
"""

import json
    
def read_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def write_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
    return




