#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 12:41:50 2025

@author: mortivarus
"""

import json

json_file = "/home/mortivarus/Desktop/freetube-playlists-2025-04-27.json"
    
    
def read_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def write_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f)
    return


playlists = read_json(json_file)


eighties = [i for i in playlists if '80s' in i['playlistName']][0]



https://youtu.be/awoFZaSuko4