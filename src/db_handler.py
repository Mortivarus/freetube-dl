#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 13:15:35 2025

@author: mortivarus
"""
import json
import json_handler as jh


file = "/home/mortivarus/Desktop/freetube-playlists-2025-04-28.db"

 
def load_db(file):
    with open(file, 'r') as f:
      data = [i.strip() for i in f if i.strip()]
      data = [json.loads(i) for i in data]
    return data

def export_playlists(playlists):
    for i in playlists:
        name = i['playlistName']
        name = name.replace("/", "-").replace(" ", "-")
        path = f"../playlists/{name}.json"
        videos = i['videos']
        jh.write_json(videos, path)
    

playlists = load_db(file)

export_playlists(playlists)